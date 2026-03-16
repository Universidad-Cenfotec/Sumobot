# =========================================================
# SUMOBOT BLE + PDI RECTO + GIROS 90°
# =========================================================

import time
import board
import math

from ideaboard import IdeaBoard
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement


# =========================================================
# INICIALIZACIÓN
# =========================================================

ib = IdeaBoard()

i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, 0x6b)

RAD_A_GRADOS = 180 / math.pi

ble = BLERadio()
ble.name = "Sumobot_BLE"

uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

stop_flag = False


# =========================================================
# LED
# =========================================================

def led(color):
    ib.pixel = color


# =========================================================
# CALIBRAR GIROSCOPIO (SIN ERROR)
# =========================================================

def calibrar_drift(sensor, segundos=4):

    print("Calibrando giroscopio...")

    led((255,0,0))

    suma = 0
    muestras = 0

    t0 = time.monotonic()

    while time.monotonic() - t0 < segundos:

        data = sensor.gyro[2]

        if abs(data) < 0.05:

            suma += data
            muestras += 1

        time.sleep(0.005)

    if muestras == 0:
        drift = 0
    else:
        drift = suma / muestras

    print("Drift:", drift)

    led((0,0,0))

    return drift


drift = calibrar_drift(sensor,4)

led((0,255,0))

print("Robot listo")


# =========================================================
# STOP
# =========================================================

def stop():

    global stop_flag

    stop_flag = True

    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

    led((255,255,0))

    print("STOP")


# =========================================================
# GIRO POR GRADOS
# =========================================================

def girar_grados(grados, velocidad=0.35):

    global drift, stop_flag

    stop_flag = False

    sentido = 1 if grados > 0 else -1

    grados = abs(grados) - 2
    acumulado = 0

    t_anterior = time.monotonic()

    ib.motor_1.throttle = velocidad * sentido
    ib.motor_2.throttle = -velocidad * sentido

    while acumulado < grados:

        if stop_flag:
            break

        t_actual = time.monotonic()
        dt = t_actual - t_anterior
        t_anterior = t_actual

        vel = sensor.gyro[2] - drift

        delta = vel * dt * RAD_A_GRADOS

        acumulado += abs(delta)

        if grados - acumulado < 45:

            ib.motor_1.throttle = 0.18 * sentido
            ib.motor_2.throttle = -0.18 * sentido

        time.sleep(0.005)

    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0


# =========================================================
# AVANZAR RECTO CON PDI ORIGINAL
# =========================================================

def avanzar_recto(velocidad, duracion):

    global drift, stop_flag

    stop_flag = False

    t0 = time.monotonic()

    base = abs(velocidad)
    direccion = 1 if velocidad > 0 else -1

    Kp = 0.15
    Ki = 0.8
    Kd = 0.05

    error_anterior = 0
    error_integral = 0

    if velocidad > 0:
        led((0,255,0))
    else:
        led((255,0,0))

    while time.monotonic() - t0 < duracion:

        if stop_flag:
            break

        # STOP inmediato desde BLE
        if ble.connected and uart.in_waiting:

            raw = uart.readline()

            if raw:

                try:

                    text = raw.decode("utf-8").strip()

                    cmd, vel_str = text.split(",")

                    if cmd.upper() == "S":
                        stop()
                        break

                except:
                    pass

        error = sensor.gyro[2] - drift

        error_integral += error

        error_deriv = error - error_anterior

        correccion = Kp*error + Ki*error_integral + Kd*error_deriv

        correccion = max(-0.3, min(0.3, correccion))

        # PDI ORIGINAL (funciona adelante y atrás)
        v1 = base * direccion + correccion
        v2 = base * direccion - correccion

        v1 = max(-1, min(1, v1))
        v2 = max(-1, min(1, v2))

        ib.motor_1.throttle = v1
        ib.motor_2.throttle = v2

        error_anterior = error

        time.sleep(0.01)

    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0


# =========================================================
# MOVIMIENTOS
# =========================================================

def forward(vel=0.5):

    print("FORWARD")

    avanzar_recto(vel,5)


def backward(vel=0.5):

    print("BACKWARD")

    avanzar_recto(-vel,5)


def left(vel=0.35):

    print("LEFT")

    led((0,255,255))

    girar_grados(-90,vel)


def right(vel=0.35):

    print("RIGHT")

    led((0,255,255))

    girar_grados(90,vel)


# =========================================================
# BLE LOOP ESTABLE (SIN MEMORY ERROR)
# =========================================================

print("Esperando BLE")

ble.start_advertising(advertisement)

while True:

    while not ble.connected:

        led((255,255,0))
        time.sleep(0.5)

        led((0,0,0))
        time.sleep(0.5)

    print("BLE conectado")

    led((0,255,0))

    ble.stop_advertising()

    while ble.connected:

        raw = uart.readline()

        if raw:

            try:

                text = raw.decode("utf-8").strip()

                cmd, vel_str = text.split(",")

                vel = float(vel_str)

                if cmd.upper() == "F":
                    forward(vel)

                elif cmd.upper() == "B":
                    backward(vel)

                elif cmd.upper() == "L":
                    left(vel)

                elif cmd.upper() == "R":
                    right(vel)

                elif cmd.upper() == "S":
                    stop()

            except:
                pass

    print("BLE desconectado")

    led((255,255,0))

    ble.start_advertising(advertisement)
