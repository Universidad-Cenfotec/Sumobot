#Tomás de Camino Beck, Ph.D.
#Universidad CECNFOTEC

```
Ver documento explicativo:
https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/Control_Movimientos.md

```

import board
import time
import math
from ideaboard import IdeaBoard
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

# Inicialización
ib = IdeaBoard()
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, 0x6b)

# Constantes
RAD_A_GRADOS = 180 / math.pi

def calibrar_drift(sensor, segundos=2):
    print("Calibrando giroscopio...")
    suma = 0
    muestras = 0
    t0 = time.monotonic()
    while time.monotonic() - t0 < segundos:
        suma += sensor.gyro[2]
        muestras += 1
        time.sleep(0.005)
    drift = suma / muestras
    print(f"Drift promedio: {drift:.4f} rad/s")
    return drift

def girar_grados(sensor, grados, drift, velocidad=0.25):
    """Gira el robot cierta cantidad de grados usando el giroscopio"""
    sentido = 1 if grados > 0 else -1
    grados = abs(grados)
    acumulado = 0
    t_anterior = time.monotonic()

    # Inicia con velocidad normal
    ib.motor_1.throttle = velocidad * sentido
    ib.motor_2.throttle = -velocidad * sentido

    while acumulado < grados:
        t_actual = time.monotonic()
        dt = t_actual - t_anterior
        t_anterior = t_actual

        vel_angular = sensor.gyro[2] - drift
        delta_grados = vel_angular * dt * RAD_A_GRADOS
        acumulado += abs(delta_grados)

        # Desacelera si está a menos de 45 grados del objetivo
        if grados - acumulado <= 45:
            ib.motor_1.throttle = 0.1 * sentido
            ib.motor_2.throttle = -0.1 * sentido

        time.sleep(0.005)

    # Detener motores
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

def straight_move(velocidad, duracion, drift, Kp=0.9, Ki=0.3, Kd=0.8):
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
    max_correccion = 0.15  # Límite para evitar sobrecorrección

    t_anterior = time.monotonic()

    while time.monotonic() - t0 < duracion:
        t_actual = time.monotonic()
        dt = t_actual - t_anterior
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

    # Detener motores al final
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0




# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------

ib.pixel = (255,0,0)
drift = calibrar_drift(sensor,5)
ib.pixel = (0,0,0)

while True:
    #girar_grados(sensor, 180, drift)
    #time.sleep(1)
    #Avanza recto 2 segundos
    straight_move(0.3, 5, drift)
    time.sleep(1)
    
