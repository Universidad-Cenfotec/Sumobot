# Tomás de Camino Beck, Ph.D.
# Universidad CENFOTEC

"""
Control de movimiento y navegación de un robot Sumobot con sensores IR y giroscopio
permite navegar en una cuadrícula de lineas negras, reconociendo intersecciónes
Ver documentación complementaria:
https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/Control_Movimientos.md
"""

import board
import time
import math
from ideaboard import IdeaBoard
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Inicializacion de BLE
ble = BLERadio()

# Inicialización de hardware
ib = IdeaBoard()
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, address=0x6B)

# Constante de conversión
RAD_A_GRADOS = 180 / math.pi

# Nombre BLE
ble.name = "Sumobot_BLE_1"

# Servicio UART
uart = UARTService()

# Advertising
advertisement = ProvideServicesAdvertisement(uart)

# Sensores IR conectados a pines analógicos
sen1 = ib.AnalogIn(board.IO36)  # Delantero izquierdo
sen2 = ib.AnalogIn(board.IO39)  # Delantero derecho
sen3 = ib.AnalogIn(board.IO34)  # Trasero izquierdo
sen4 = ib.AnalogIn(board.IO35)  # Trasero derecho
infrarrojos = [sen1, sen2, sen3, sen4]

# -------------------------------
# FUNCIONES DE UTILIDAD
# -------------------------------

def leer_sensores(sensores, umbral=10000):
    """
    Lee los sensores IR y retorna una lista binaria:
    1 = línea negra detectada (valor < umbral), 0 = blanco.
    """
    return [int(sensor.value < umbral) for sensor in sensores]

def stop():
    """Detiene todos los motores y apaga el LED RGB."""
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    ib.pixel = (0, 0, 0)

def execute(commandlist: list, commands: dict):
    """
    Ejecuta una lista de comandos utilizando un diccionario que mapea nombres de comandos a funciones.
    """
    for cmd in commandlist:
        cmd = cmd.strip().upper()
        if cmd in commands:
            try:
                commands[cmd]()
            except Exception as e:
                print(f"Error al ejecutar '{cmd}': {e}")
        else:
            print(f"Comando '{cmd}' no encontrado.")

def str_to_list(secuencia: str) -> list:
    """
    Convierte una cadena de texto con palabras separadas por comas en una lista de strings.
    """
    return [palabra.strip() for palabra in secuencia.split(',') if palabra.strip()]

# -------------------------------
# MOVIMIENTOS BÁSICOS
# -------------------------------

def forward(t, speed):
    """Avanza hacia adelante por `t` segundos a velocidad `speed`."""
    ib.pixel = (0, 255, 0)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    time.sleep(t)
    stop()

def backward(t, speed):
    """Retrocede por `t` segundos a velocidad `speed`."""
    ib.pixel = (150, 255, 0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    time.sleep(t)
    stop()

def left(t, speed):
    """Gira a la izquierda por `t` segundos."""
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = speed
    time.sleep(t)
    stop()

def right(t, speed):
    """Gira a la derecha por `t` segundos."""
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = -speed
    time.sleep(t)
    stop()

# -------------------------------
# CONTROL CON GIROSCOPIO
# -------------------------------

def calibrar_drift(sensor, segundos=2):
    """
    Mide el promedio del drift del eje Z del giroscopio durante `segundos`.
    """
    print("Calibrando giroscopio...")
    suma = 0
    muestras = 0
    t0 = time.monotonic()

    while time.monotonic() - t0 < segundos:
        valor = sensor.gyro[2]
        if abs(valor) < 0.008:
            suma += valor
            muestras += 1
        time.sleep(0.005)

    drift = suma / muestras if muestras > 0 else 0
    print(f"Drift promedio: {drift:.4f} rad/s")
    return drift

def girar_grados(sensor, grados, drift, velocidad=0.3):
    """
    Gira `grados` usando el giroscopio para medir la rotación acumulada.
    grados > 0  -> derecha
    grados < 0  -> izquierda
    """
    sentido = 1 if grados > 0 else -1
    meta = abs(grados) - 2.5  # pequeña compensación por sobregiro

    acumulado = 0
    t_anterior = time.monotonic()

    ib.pixel = (0, 0, 255)
    ib.motor_1.throttle = velocidad * sentido
    ib.motor_2.throttle = -velocidad * sentido

    while acumulado < meta:
        t_actual = time.monotonic()
        dt = t_actual - t_anterior
        t_anterior = t_actual

        vel_angular = sensor.gyro[2] - drift
        delta = vel_angular * dt * RAD_A_GRADOS
        acumulado += abs(delta)

        # desacelera en la segunda mitad
        if meta - acumulado <= meta / 2:
            ib.motor_1.throttle = 0.2 * sentido
            ib.motor_2.throttle = -0.2 * sentido

        time.sleep(0.005)

    stop()

def move_straight_gyro(
    velocidad,
    duracion,
    drift,
    Kp=0.15,
    Ki=0.8,
    Kd=0.05,
    max_correccion=0.2
):
    """
    Mueve el robot en línea recta usando control PID sobre el eje Z del giroscopio.
    Si velocidad > 0 avanza, si velocidad < 0 retrocede.
    """
    t0 = time.monotonic()
    t_anterior = t0

    velocidad_base = abs(velocidad)
    direccion = 1 if velocidad >= 0 else -1

    error_anterior = 0
    error_integral = 0

    if direccion > 0:
        ib.pixel = (0, 255, 0)   # verde = adelante
    else:
        ib.pixel = (255, 180, 0) # ámbar = atrás

    while time.monotonic() - t0 < duracion:
        t_actual = time.monotonic()
        dt = t_actual - t_anterior
        t_anterior = t_actual

        if dt <= 0:
            time.sleep(0.005)
            continue

        # Error de rotación en Z
        error = sensor.gyro[2] - drift

        # PID
        error_integral += error * dt
        error_derivativo = (error - error_anterior) / dt

        correccion = Kp * error + Ki * error_integral + Kd * error_derivativo
        correccion = max(-max_correccion, min(max_correccion, correccion))

        # Para ambos casos se conserva la misma lógica:
        # motor_1 = base + corrección
        # motor_2 = base - corrección
        # y el signo de dirección define si es adelante o atrás.
        v1 = direccion * velocidad_base + correccion
        v2 = direccion * velocidad_base - correccion

        v1 = max(-1, min(1, v1))
        v2 = max(-1, min(1, v2))

        ib.motor_1.throttle = v1
        ib.motor_2.throttle = v2

        error_anterior = error
        time.sleep(0.01)

    stop()

def forward_gyro(duracion, velocidad, drift):
    """Avance recto con control PID y giroscopio."""
    move_straight_gyro(velocidad, duracion, drift)

def backward_gyro(duracion, velocidad, drift):
    """Retroceso recto con control PID y giroscopio."""
    move_straight_gyro(-abs(velocidad), duracion, drift)

# -------------------------------
# SEGUIDOR DE LÍNEA CON DETENCIÓN
# -------------------------------

def forward_line_stop(th=2950, speed=0.5, corr=0.1, drift=0):
    """
    Sigue una línea con sensores delanteros. Se detiene si sensores traseros detectan fondo blanco.
    """
    while True:
        front = leer_sensores([sen1, sen2], th)
        back = leer_sensores([sen3, sen4], th)

        izq, der = front
        tras_izq, tras_der = back

        print(f"Front: {izq, der} | Back: {tras_izq, tras_der}")

        if tras_izq == 0 and tras_der == 0:
            move_straight_gyro(speed, 0.1, drift)
            stop()
            ib.pixel = (255, 0, 0)
            print("¡Intersección detectada! Salida de función.")
            return

        if izq == 1 and der == 1:
            move_straight_gyro(speed, 0.05, drift)
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
            move_straight_gyro(speed, 0.05, drift)
            stop()

# -------------------------------
# WRAPPERS PARA COMANDOS BLE
# -------------------------------

# Duraciones base de cada movimiento comandado
STEP_TIME = 0.60      # tiempo de avance o retroceso por comando
TURN_SPEED = 0.30     # velocidad de giro 90°
MOVE_SPEED = 0.25     # velocidad de avance/retroceso

def f():
    """Comando F: avanzar recto con giroscopio."""
    print("Comando F")
    forward_gyro(STEP_TIME, MOVE_SPEED, drift)
    ib.pixel = (0, 200, 200)

def b():
    """Comando B: retroceder recto con giroscopio."""
    print("Comando B")
    backward_gyro(STEP_TIME, MOVE_SPEED, drift)
    ib.pixel = (200, 200, 0)

def l():
    """Comando L: giro 90 grados a la izquierda."""
    print("Comando L")
    girar_grados(sensor, -90, drift, velocidad=TURN_SPEED)
    ib.pixel = (200, 0, 200)

def r():
    """Comando R: giro 90 grados a la derecha."""
    print("Comando R")
    girar_grados(sensor, 90, drift, velocidad=TURN_SPEED)
    ib.pixel = (200, 0, 200)

# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

ib.pixel = (255, 0, 0)  # LED rojo durante calibración
drift = calibrar_drift(sensor, 5)
ib.pixel = (0, 0, 0)

th = 3500
speed = 0.25
corr = 0.1

# Asocia comandos con funciones
comandos = {
    "F": f,
    "B": b,
    "L": l,
    "R": r
}

# Ciclo principal
while True:
    print("Advertising BLE services")
    ble.start_advertising(advertisement)

    while not ble.connected:
        pass

    ble.stop_advertising()
    print("BLE connected")

    while ble.connected:
        raw_bytes = uart.readline()
        if raw_bytes:
            text = raw_bytes.decode("utf-8").strip()
            print(f"Got text from central: {text}")
            com = str_to_list(text)
            execute(com, comandos)

    print("BLE disconnected")