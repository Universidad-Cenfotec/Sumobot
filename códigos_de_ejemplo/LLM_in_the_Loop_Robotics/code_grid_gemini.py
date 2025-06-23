# Tomás de Camino Beck, Ph.D.
# Universidad CENFOTEC
#
# Combina navegación en cuadrícula y generación dinámica de comandos vía Gemini.
# El robot solicita a Gemini una lista de movimientos (F, L, R) para desplazarse
# de un punto de inicio a uno final en una malla cartesiana. El resultado se
# ejecuta inmediatamente en el Sumobot.

# Código experimental

"""
Requisitos externos
-------------------
- secrets.py con las claves:
    secrets = {
        "ssid": "TU_WIFI",
        "password": "TU_PASS",
        "api_key": "TU_API_KEY_GEMINI"
    }
- Librerías CircuitPython:
    wifi, socketpool, ssl, adafruit_requests, ideaboard, adafruit_lsm6ds, keypad
- Infraestructura física: Sumobot CENFOTEC con IdeaBoard + LSM6DS3TRC
"""

import board
import time
import math
import socketpool
import ssl
import wifi
import adafruit_requests as requests
import keypad

from ideaboard import IdeaBoard
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC
from secrets import secrets  # ssid, password, api_key

# -----------------------------------------------------------------------------
# CONEXIÓN WiFi Y CONFIGURACIÓN DE GEMINI
# -----------------------------------------------------------------------------
ib = IdeaBoard()

API_KEY = secrets["api_key"]
ENDPOINT = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-1.5-flash:generateContent?key=" + API_KEY
)

def preguntar_gemini(prompt: str, max_tokens: int = 64) -> str:
    """Envía un prompt a Gemini y devuelve el texto de respuesta."""
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": max_tokens},
    }
    headers = {"Content-Type": "application/json"}

    print("\nEnviando prompt a Gemini…")
    response = https.post(ENDPOINT, headers=headers, json=payload)

    if response.status_code == 200:
        texto = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        print("Gemini respondió:", texto)
        return texto.strip()
    print("Error", response.status_code, response.text)
    return ""


def obtener_movimientos(inicio: tuple[int, int], final: tuple[int, int]) -> str:
    """
    Construye un prompt claro y estructurado para solicitar al modelo de lenguaje
    una secuencia mínima de comandos que permita al robot llegar del punto inicial
    al punto final en una cuadrícula cartesiana.
    
    Argumentos:
    - inicio: tupla (x₀, y₀)
    - final: tupla (x₁, y₁)

    Retorna:
    - Una cadena con los comandos separados por comas, sin texto adicional.
    """
    prompt = f"""
    Objetivo
    Devuelve solo una secuencia separada por comas con los comandos mínimos que llevan al robot
    desde {inicio} hasta {final} sobre una cuadrícula cartesiana.
    
    reglas:
    1.La cuadrícula cartesiana (x,y), tiene su punto (0,0) a la izquierda abajo

    2. El robot siempre inicia mirando hacia el eje "y" positivo

    3. Comandos permitidos
    F – Avanza 1 unidad en la dirección actual  
    L – Gira 90° a la izquierda en su lugar  
    R – Gira 90° a la derecha en su lugar  

    4. Restricciones de salida
    - Sin texto adicional, títulos, comillas ni espacios.
    - Usa mayúsculas.  
    - Los comandos debe ser uno a uno, y estar separados solo por coma
      (ej.: L,F,F,R,F).

    5. Parámetros de entrada
    - inicio = {inicio}  ➜  tupla (x₀, y₀) 
    - final  = {final}   ➜  tupla (x₁, y₁)  

    6. El robot siempre temina mirando hacia el eje "y" positivo igual que como comenzó


    Ejemplo de salida con inicio (0,0) y final (3,2) válida es:  
    R,F,F,F,L,F,F
    """

    return preguntar_gemini(prompt)


# -----------------------------------------------------------------------------
# HARDWARE Y FUNCIONES DE MOVIMIENTO
# -----------------------------------------------------------------------------

i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, address=0x6B)
RAD_A_GRADOS = 180 / math.pi

# Sensores infrarrojos
sen1 = ib.AnalogIn(board.IO36)
sen2 = ib.AnalogIn(board.IO39)
sen3 = ib.AnalogIn(board.IO34)
sen4 = ib.AnalogIn(board.IO35)

# Botón de activación (BOOT en IdeaBoard)
keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)

# --------------- Utilidades IR y motores ---------------

def leer_sensores(sensores, umbral: int = 10000):
    return [int(s.value < umbral) for s in sensores]

def stop():
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    ib.pixel = (0, 0, 0)

# --------------- Movimientos básicos -------------------

def forward(t: float, speed: float):
    ib.pixel = (0, 255, 0)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    time.sleep(t)
    stop()

def backward(t: float, speed: float):
    ib.pixel = (150, 255, 0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    time.sleep(t)
    stop()

def left_turn(t: float, speed: float):
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = speed
    time.sleep(t)
    stop()

def right_turn(t: float, speed: float):
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = -speed
    time.sleep(t)
    stop()

# --------------- Giroscopio -----------------------------

def calibrar_drift(segundos: int = 2):
    print("Calibrando giroscopio…")
    suma = 0
    muestras = 0
    t0 = time.monotonic()
    while time.monotonic() - t0 < segundos:
        val = sensor.gyro[2]
        if abs(val) < 0.008:
            suma += val
            muestras += 1
        time.sleep(0.005)
    drift = suma / muestras if muestras else 0
    print(f"Drift promedio: {drift:.4f} rad/s")
    return drift


def girar_grados(grados: float, drift: float, vel: float = 0.25):
    sentido = 1 if grados > 0 else -1
    objetivo = abs(grados) - 2.5  # evita sobregiro
    acumulado = 0
    t_prev = time.monotonic()
    ib.motor_1.throttle = vel * sentido
    ib.motor_2.throttle = -vel * sentido
    while acumulado < objetivo:
        t_act = time.monotonic()
        dt = t_act - t_prev
        t_prev = t_act
        omega = sensor.gyro[2] - drift
        acumulado += abs(omega * dt * RAD_A_GRADOS)
        if objetivo - acumulado <= objetivo / 2:
            ib.motor_1.throttle = 0.15 * sentido
            ib.motor_2.throttle = -0.15 * sentido
        time.sleep(0.005)
    stop()

# --------------- Seguidor de línea ----------------------

def forward_line_stop(th=2950, speed=0.5, corr=0.1):
    while True:
        front = leer_sensores([sen1, sen2], th)
        back = leer_sensores([sen3, sen4], th)
        izq, der = front
        tras_izq, tras_der = back
        if tras_izq == 0 and tras_der == 0:
            forward(0.15, speed)
            stop()
            return
        if izq == 1 and der == 1:
            forward(0.05, speed)
        elif izq == 1 and der == 0:
            ib.motor_1.throttle = speed + corr
            ib.motor_2.throttle = speed - corr
            time.sleep(0.05)
            stop()
        elif izq == 0 and der == 1:
            ib.motor_1.throttle = speed - corr
            ib.motor_2.throttle = speed + corr
            time.sleep(0.05)
            stop()
        else:
            forward(0.05, speed)
            stop()

# --------------- Helper wrappers ------------------------

th = 2950
speed = 0.3
corr = 0.1


def f():
    forward_line_stop(th, speed, corr)

def l():
    girar_grados(-90, DRIFT)

def r():
    girar_grados(90, DRIFT)

COMMANDS = {"F": f, "L": l, "R": r}


def execute(commandlist: list[str]):
    for cmd in commandlist:
        func = COMMANDS.get(cmd.upper())
        if func:
            func()
        else:
            print("Comando no reconocido:", cmd)


def str_to_list(seq: str) -> list[str]:
    return [s.strip() for s in seq.split(',') if s.strip()]

# -----------------------------------------------------------------------------
# LOOP PRINCIPAL
# -----------------------------------------------------------------------------

# conecta al Wifi
ib.pixel = (0, 0, 255)  # Azul: conectando
print("Conectando al WiFi…")
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Conectado a", secrets["ssid"], "IP:", wifi.radio.ipv4_address)
ib.pixel = (0, 255, 0)  # Verde: conectado


socket = socketpool.SocketPool(wifi.radio)
https = requests.Session(socket, ssl.create_default_context())

time.sleep(0.3)


ib.pixel = (255, 0, 0)  # Rojo: calibrando drift
DRIFT = calibrar_drift(5)
ib.pixel = (0, 0, 0)

# Coordenadas de ejemplo — reemplazar según necesidad
inicio = (0, 0)
final = (3, 2)

while True:
    event = keys.events.get()
    if event and event.released:
        ib.pixel = (128, 0, 128)
        cadena = obtener_movimientos(inicio, final)
        if cadena:
            comandos = str_to_list(cadena.replace(" ", ""))
            print("Ejecutando:", comandos)
            ib.pixel = (0, 0, 0)
            execute(comandos)
        else:
            print("No se obtuvo una secuencia válida.")

    time.sleep(0.1)
