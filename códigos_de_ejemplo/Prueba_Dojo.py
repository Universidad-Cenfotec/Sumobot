# ==========================================
# SUMOBOT – MODO PRUEBA DOJO (4 SENSORES IR)
# Universidad CENFOTEC
#Fiorella Pérez
# NO competitivo – SOLO PRUEBAS
# ==========================================

import board
import keypad
from time import sleep
from ideaboard import IdeaBoard
from hcsr04 import HCSR04

# ------------------------------------------
# Inicialización
# ------------------------------------------
ib = IdeaBoard()

# Sensores infrarrojos
ir_front_left  = ib.AnalogIn(board.IO36)
ir_front_right = ib.AnalogIn(board.IO39)
ir_back_left   = ib.AnalogIn(board.IO34)
ir_back_right  = ib.AnalogIn(board.IO35)

# Sensor ultrasónico
sonar = HCSR04(board.IO26, board.IO25)

# Botón 0 (BOOT)
keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)

# ------------------------------------------
# Parámetros ajustables
# ------------------------------------------
UMBRAL_IR = 3000        # Ajustar según el dojo
DISTANCIA_MANO = 25    # cm
VEL = 0.4

# ------------------------------------------
# Funciones de movimiento
# ------------------------------------------
def stop():
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    ib.pixel = (0, 0, 0)

def forward(speed):
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    ib.pixel = (0, 255, 0)

def backward(speed, t=0.4):
    ib.pixel = (255, 100, 0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    sleep(t)
    stop()

def turn_random():
    ib.pixel = (0, 0, 255)
    ib.motor_1.throttle = 0.4
    ib.motor_2.throttle = -0.4
    sleep(0.4)
    stop()

def small_forward():
    ib.motor_1.throttle = 0.3
    ib.motor_2.throttle = 0.3
    sleep(0.25)
    stop()

# ------------------------------------------
# Esperar botón 0
# ------------------------------------------
ib.pixel = (255, 0, 0)
print("Esperando botón 0...")

while True:
    event = keys.events.get()
    if event and event.released:
        break

sleep(0.5)
ib.pixel = (0, 255, 255)
print("Modo prueba iniciado")

# ------------------------------------------
# Loop principal
# ------------------------------------------
while True:

    # Lectura IR (True = blanco)
    fl = ir_front_left.value  < UMBRAL_IR
    fr = ir_front_right.value < UMBRAL_IR
    bl = ir_back_left.value   < UMBRAL_IR
    br = ir_back_right.value  < UMBRAL_IR

    # Lectura ultrasónico
    try:
        dist = sonar.dist_cm()
    except RuntimeError:
        dist = -1

    # ----------------------------------
    # BORDE DELANTERO
    # ----------------------------------
    if fl or fr:
        print("⚠️ Borde delantero")
        backward(0.5)
        turn_random()
        continue

    # ----------------------------------
    # BORDE TRASERO
    # ----------------------------------
    if bl or br:
        print("⚠️ Borde trasero")
        small_forward()
        continue

    # ----------------------------------
    # MANO / OBJETO AL FRENTE
    # ----------------------------------
    if dist != -1 and dist < DISTANCIA_MANO:
        print("✋ Objeto detectado:", dist, "cm")
        stop()
        ib.pixel = (255, 0, 255)
        sleep(0.2)
        continue

    # ----------------------------------
    # AVANCE NORMAL
    # ----------------------------------
    forward(VEL)
    sleep(0.05)

