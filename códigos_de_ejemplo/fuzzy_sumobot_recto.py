
# fuzzy_sumobot_recto.py
# Ejemplo: Control difuso para mantener movimiento recto con Sumobot

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
    suma = 0
    muestras = 0
    t0 = time.monotonic()
    while time.monotonic() - t0 < segundos:
        data = sensor.gyro[2]
        if abs(data) < 0.008:
            suma += data
            muestras += 1
        time.sleep(0.005)
    return suma / muestras if muestras > 0 else 0

# Dominio difuso para error angular [-90, 90]
error_domain = FuzzyDomain(nset=3)
error_domain.set_domain(-90, 90)

def correccion_difusa(error_grados):
    error_domain.truth_degree(error_grados)
    return error_domain.defuzzify_weighted_average()

# Movimiento recto con corrección difusa continua
def avanzar_recto(sensor, tiempo=5):
    drift = calibrar_drift(sensor)
    print("Drift:", drift)
    t0 = time.monotonic()
    orientacion = 0
    sensor.reset()

    while time.monotonic() - t0 < tiempo:
        giro_z = sensor.gyro[2] - drift
        orientacion += giro_z * 0.1 * RAD_A_GRADOS  # estimación orientada (simplificada)

        error = orientacion
        correccion = correccion_difusa(error)

        # Aplicar corrección proporcional a velocidad
        base_speed = 0.3
        delta = (correccion / 90) * base_speed

        ib.motores(base_speed - delta, base_speed + delta)
        time.sleep(0.1)

    ib.motores(0, 0)

# Ejecutar el ejemplo
avanzar_recto(sensor)
