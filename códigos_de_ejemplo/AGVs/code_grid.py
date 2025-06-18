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

# Inicialización de hardware
ib = IdeaBoard()
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, address=0x6B)

# Constante de conversión
RAD_A_GRADOS = 180 / math.pi

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

def girar_grados(sensor, grados, drift, velocidad=0.25):
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
            ib.motor_1.throttle = 0.15 * sentido
            ib.motor_2.throttle = -0.15 * sentido

        time.sleep(0.005)

    stop()

# -------------------------------
# MOVIMIENTO RECTO CON PDI
# -------------------------------

def straight_move(velocidad, duracion, drift, Kp=0.15, Ki=0.8, Kd=0.05):
    """
    Mantiene movimiento recto por `duracion` segundos usando control PDI.
    """
    t0 = time.monotonic()
    velocidad_base = abs(velocidad)
    direccion = 1 if velocidad > 0 else -1

    error_anterior = 0
    error_integral = 0
    max_correccion = 0.3

    while time.monotonic() - t0 < duracion:
        error = sensor.gyro[2] - drift
        error_integral += error
        error_derivativo = error - error_anterior

        correccion = Kp * error + Ki * error_integral + Kd * error_derivativo
        correccion = max(-max_correccion, min(max_correccion, correccion))

        v1 = max(-1, min(1, velocidad_base * direccion + correccion))
        v2 = max(-1, min(1, velocidad_base * direccion - correccion))

        ib.motor_1.throttle = v1
        ib.motor_2.throttle = v2

        error_anterior = error
        time.sleep(0.01)

    stop()

# -------------------------------
# SEGUIDOR DE LÍNEA CON DETENCIÓN
# -------------------------------

def forward_line_stop(th=2950, speed=0.5, corr=0.1):
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
            forward(0.15, speed)
            stop()
            ib.pixel = (255, 0, 0)  # LED rojo: detenido
            print("¡Intersección detectada! Salida de función.")
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

#------------------------------------------
# funciones "wrapers" para simplificar el loop principal

def f():
    #forward
    forward_line_stop(th, speed, corr)
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

ib.pixel = (255, 0, 0)  # LED rojo durante calibración
drift = calibrar_drift(sensor, 5)
ib.pixel = (0, 0, 0)    # Apaga LED

th = 2950       # Umbral para sensores IR
speed = 0.3     # Velocidad base
corr = 0.1      # Corrección de dirección

while True:
    f()
    f()
    l()