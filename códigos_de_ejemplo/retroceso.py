import board
from time import sleep
from ideaboard import IdeaBoard

ib = IdeaBoard()

def stop():
    ib.pixel = (0,0,0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

def backward(t,speed):
    # Mueve el robot hacia atrás
    # por tiempo t, a velocidad speed = [0,1]    
    ib.pixel = (0,0,255)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    sleep(2)
    stop()

while True:
    backward(1,1)
    sleep(3)
    stop()
    sleep(3)