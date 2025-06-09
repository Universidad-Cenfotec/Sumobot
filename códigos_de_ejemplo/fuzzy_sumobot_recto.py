# Tomás de Camino BEck
# fuzzy_sumobot_recto_v2.py
# Control difuso para mantener trayectoria recta en el Sumobot
# EXPERIMENTAL REQUIERE REVISION

import time
import board
import math
from ideaboard import IdeaBoard
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC
from fuzzy import FuzzyDomain

# Inicialización de hardware
ib = IdeaBoard()
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, 0x6b)

RAD_A_GRADOS = 180 / math.pi

def calibrar_drift(sensor, segundos=2):
    print("Calibrando drift del giroscopio...")
    suma = 0
    muestras = 0
    t0 = time.monotonic()
    while time.monotonic() - t0 < segundos:
        data = sensor.gyro[2]
        if abs(data) < 0.008:
            suma += data
            muestras += 1
        time.sleep(0.005)
    drift = suma / muestras if muestras > 0 else 0
    print(f"Drift estimado: {drift:.5f} rad/s")
    return drift

# Dominio difuso del error de orientación
error_domain = FuzzyDomain(nset=3)
error_domain.set_domain(-90, 90)

def correccion_difusa(error_grados):
    error_domain.truth_degree(error_grados)
    return error_domain.defuzzify_weighted_average()

def avanzar_recto(sensor, drift, duracion=0.1, base_speed=0.5):
    global orientacion
    giro_z = sensor.gyro[2] - drift
    orientacion += giro_z * duracion * RAD_A_GRADOS  # estimación de orientación acumulada
    error = orientacion
    correccion = correccion_difusa(error)

    # Normalizamos la corrección dentro del rango [-1, 1]
    delta = (correccion / 90.0) * base_speed
    velocidad_izq = max(min(base_speed - delta, 1.0), -1.0)
    velocidad_der = max(min(base_speed + delta, 1.0), -1.0)

    ib.motor_1.throttle = velocidad_izq
    ib.motor_2.throttle = velocidad_der

    print(f"Error: {error:.2f}°, Corrección: {correccion:.2f}°, Velocidades: {velocidad_izq:.2f}, {velocidad_der:.2f}")
    time.sleep(duracion)

# Programa principal
drift = calibrar_drift(sensor)
orientacion = 0

print("Iniciando movimiento recto...")
while True:
    avanzar_recto(sensor, drift)

