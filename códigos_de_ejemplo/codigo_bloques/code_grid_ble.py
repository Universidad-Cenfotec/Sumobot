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

# By default, your device will have some name like CIRCUITPYxxxx; let's make that more user friendly
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

    Parámetros:
    -----------
    commandlist : list
        Lista de strings, donde cada string representa el nombre de un comando a ejecutar.

    commands : dict
        Diccionario que asocia nombres de comandos (strings) con funciones de Python (callables) que no reciben argumentos.

    Ejemplo:
    --------
    def saludar():
        print("Hola")

    def despedir():
        print("Adiós")

    comandos = {
        "hola": saludar,
        "adios": despedir
    }

    execute(["hola", "adios", "otro"], comandos)

    # Salida esperada:
    # Hola
    # Adiós
    # Comando 'otro' no encontrado.
    """
    for cmd in commandlist:
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
    return [palabra.strip() for palabra in secuencia.split(',')]


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
        if abs(valor) < 0.008:  # Filtra valores extremos
            suma += valor
            muestras += 1
        time.sleep(0.005)

    drift = suma / muestras if muestras > 0 else 0
    print(f"Drift promedio: {drift:.4f} rad/s")
    return drift

def girar_grados(sensor, grados, drift, velocidad=0.3):
    """
    Gira `grados` usando el giroscopio para medir la rotación acumulada.
    """
    sentido = 1 if grados > 0 else -1
    grados = abs(grados) - 2.5  # Corrección para evitar sobregiro

    acumulado = 0
    t_anterior = time.monotonic()

    ib.motor_1.throttle = velocidad * sentido
    ib.motor_2.throttle = -velocidad * sentido

    while acumulado < grados:
        t_actual = time.monotonic()
        dt = t_actual - t_anterior
        t_anterior = t_actual

        vel_angular = sensor.gyro[2] - drift
        delta = vel_angular * dt * RAD_A_GRADOS
        acumulado += abs(delta)

        if grados - acumulado <= grados / 2:
            ib.motor_1.throttle = 0.2 * sentido
            ib.motor_2.throttle = -0.2 * sentido

        time.sleep(0.005)

    stop()


def straight_move(velocidad, duracion, drift, Kp=0.15, Ki=0.8, Kd=0.05):
    """
    Mueve el robot en línea recta durante `duracion` segundos con control PDI discreto.
    Corrige desviaciones usando el giroscopio (eje Z) ajustando ambos motores.
    
    Kp: Ganancia proporcional
    Ki: Ganancia integral
    Kd: Ganancia derivativa
    """
    t0 = time.monotonic()
    velocidad_base = abs(velocidad)
    direccion = 1 if velocidad > 0 else -1

    error_anterior = 0
    error_integral = 0
    max_correccion = 0.2  # Límite para evitar sobrecorrección

    t_anterior = time.monotonic()

    while time.monotonic() - t0 < duracion:
        t_actual = time.monotonic()
        dt = 1 #t_actual - t_anterior
        t_anterior = t_actual

        if dt == 0:
            continue  # Evita división por cero

        # Error actual: velocidad angular corregida
        error = sensor.gyro[2] - drift

        # Término integral acumulado
        error_integral += error * dt

        # Término derivativo
        error_derivativo = (error - error_anterior) / dt

        # Control PDI discreto
        correccion = Kp * error + Ki * error_integral + Kd * error_derivativo

        # Límite de corrección
        correccion = max(-max_correccion, min(max_correccion, correccion))

        # Ajuste de velocidades
        v1 = velocidad_base * direccion + correccion
        v2 = velocidad_base * direccion - correccion

        # Saturación entre -1 y 1
        v1 = max(-1, min(1, v1))
        v2 = max(-1, min(1, v2))

        ib.motor_1.throttle = v1
        ib.motor_2.throttle = v2

        error_anterior = error
        time.sleep(0.01)
        #ib.motor_1.throttle = 0
        #ib.motor_2.throttle = 0
        #time.sleep(0.01)

    # Detener motores al final
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

# -------------------------------
# SEGUIDOR DE LÍNEA CON DETENCIÓN
# -------------------------------

def forward_line_stop(th=2950, speed=0.5, corr=0.1,drift=0):
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
            straight_move(speed,0.1, drift)
            stop()
            ib.pixel = (255, 0, 0)  # LED rojo: detenido
            print("¡Intersección detectada! Salida de función.")
            return

        if izq == 1 and der == 1:
            straight_move( speed, 0.05, drift)
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
            straight_move(speed,0.05, drift)
            stop()

#------------------------------------------
# funciones "wrapers" para simplificar el loop principal

def f():
    #forward
    forward_line_stop(th, speed, corr,drift)
    ib.pixel = (0, 200, 200)

def l():
    # left
    girar_grados(sensor, -90, drift)
    ib.pixel = (200, 0, 200)
    
def r():
    # right
    girar_grados(sensor, 90, drift)
    ib.pixel = (200, 0, 200)
    
    

# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

# definiciones
ib.pixel = (255, 0, 0)  # LED rojo durante calibración
drift = calibrar_drift(sensor, 5)
ib.pixel = (0, 0, 0)    # Apaga LED

th = 3500       # Umbral para sensores IR
speed = 0.25     # Velocidad base
corr = 0.1      # Corrección de dirección

#Asocia comandos con funciones
comandos = {
    "F": f,
    "L": l,
    "R": r
}

#ciclo pricipal

while True:
    print("Advertising BLE services")
    # start advertising
    ble.start_advertising(advertisement)
    # keep going until we get a connection
    while not ble.connected:
        pass

    # if we got here, we have a connection. Stop advertising!
    ble.stop_advertising()
    print("BLE connected")

    # do some work as long as we're connected
    while ble.connected:
        # try reading some text from the UART, e.g. typed into the app
        raw_bytes = uart.readline()
        if raw_bytes:
            text = raw_bytes.decode("utf-8")
            print(f"Got text from central: {text}")
            com = str_to_list(text)
            execute(com, comandos)
 

    # we no longer have a connection, so we'll go back to the top of the loop
    print("BLE disconnected")


