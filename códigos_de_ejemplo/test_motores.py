# Gabriela Urbina Hernández
# Escuela de Sistemas Inteligentes
# Universidad Cenfotec

import board
from ideaboard import IdeaBoard
from time import sleep

ib = IdeaBoard()  # Instancia del IdeaBoard

# Funciones de movimiento

def forward(t=1, speed=0.5):
    ib.pixel = (0, 255, 0)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    sleep(t)
    stop()

def backward(t=1, speed=0.5):
    ib.pixel = (255, 255, 0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    sleep(t)
    stop()

def left(t=1, speed=0.5):
    ib.pixel = (0, 0, 255)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = speed
    sleep(t)
    stop()

def right(t=1, speed=0.5):
    ib.pixel = (255, 0, 255)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = -speed
    sleep(t)
    stop()

def stop():
    ib.pixel = (0, 0, 0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    sleep(0.5)

def wiggle(n=2, t=0.5, speed=0.5):
    for i in range(n):
        left(t, speed)
        right(t, speed)
    stop()

# Código principal para test
sleep(2)  # Pausa antes de iniciar test

print("Iniciando test de motores...")

forward(1, 0.6)
backward(1, 0.6)
left(1, 0.6)
right(1, 0.6)
wiggle(3, 0.4, 0.5)

print("Test finalizado.")

