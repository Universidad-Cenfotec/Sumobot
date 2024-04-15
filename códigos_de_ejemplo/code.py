# Tomás de Camino Beck
# Escuela de Sistemas Inteligentes
# Universidad Cenfotec

import board #Librerías para accesar a I/O de la placa
from ideaboard import IdeaBoard # Librería de funciones varias del ideaboard
from time import sleep # Para utilizar función que detiene el código
from hcsr04 import HCSR04 # Librerías para el sensor de Ultrasonido
import random  # Librerías de números aleatorios

sonar = HCSR04(board.IO26,board.IO25) # Crea una instanciación del sensor ultrasonido


ib = IdeaBoard() # Instanciación I/O y funcione sdel Ideboard
irSensor =  ib.DigitalIn(board.IO33) # Instanciación del sensor infrarojo

def wiggle(t,n,speed):
# Hace que el robot se mueva izquierda y derecha
# por tiempo t, a velocidad speed = [0,1]
#lo hace n veces
    for i in range(n):
        ib.pixel = (0,0,255)
        ib.motor_1.throttle = -speed
        ib.motor_2.throttle = speed
        sleep(t)
        ib.motor_1.throttle = speed
        ib.motor_2.throttle = -speed
        sleep(t)
        stop()
        sleep(t)
        ib.pixel = (0,0,255)
        ib.motor_1.throttle = speed
        ib.motor_2.throttle = -speed
        sleep(t)
        ib.motor_1.throttle = -speed
        ib.motor_2.throttle = speed
        sleep(t)
        
def forward(t,speed):
    # Mueve el robot hacia adelante
    # por tiempo t, a velocidad speed = [0,1]
    ib.pixel = (0,255,0)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    sleep(t)
    
def backward(t,speed):
    # Mueve el robot hacia atrás
    # por tiempo t, a velocidad speed = [0,1]    
    ib.pixel = (150,255,0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    sleep(t)
    
def left(t,speed):
    # Mueve el robot hacia la izquierda
    # por tiempo t, a velocidad speed = [0,1]    
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = speed
    sleep(t)
    
def right(t,speed):
    # Mueve el robot hacia la derecha
    # por tiempo t, a velocidad speed = [0,1]    
    ib.pixel = (50,55,100)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = -speed
    sleep(t)

def stop():
    # detiene los motores
    ib.pixel = (0,0,0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    
def randomTurn(t,speed):
    #Escoge izq o der al azar y rota
    # por tiempo t, a velocidad speed = [0,1]
    dir = random.choice([-1,1])
    ib.pixel = (255,0,0)
    ib.motor_1.throttle = dir*-speed
    ib.motor_2.throttle = dir*speed
    sleep(t)
    
def lookForward():
    # con el sensor ultrasonico mide la distancia al objeto de enfrente
    # retorna la distancia en centímetros
    stop()
    dist = sonar.dist_cm()
    sleep(0.2)
    return dist

def scan():
    # Se mueve hacia un lado buscando objetos delante
    # Se detiene luego de un número fijo de rotaciones
    # o cuando encuentra un objeto a la distancia indicada
    stop()
    maxCount=10
    count = 0
    dist= lookForward()
    while count <maxCount and (dist>30 or dist==-1):
        left(0.2,0.2)
        count+=1
        dist= lookForward()
    stop()
    if count==maxCount:
        return False
    else:
        return True
    
def forwardCheck(t, speed):
    # Mueve el robot hacia adelante
    # por tiempo t, a velocidad speed = [0,1]
    # Pero revisando el sensor IR para evitar salir del Dojo
     d = int(t / 0.1)
     for i in range(d):
         if irSensor.value :
             forward(0.1,speed)
         else:
             stop()
             sleep(0.3)
             backward(1,0.3)
             randomTurn(1,0.3)
             
###### CODIGO PRINCIPAL   #######

sleep(3) # da 3 segundoas para arrancar el código principal

while True:
    if scan():
        sleep(0.2)
        forwardCheck(0.5,0.2)
    else:
        sleep(0.2)
        randomTurn(1,0.2)
        forwardCheck(0.5,0.2)
    sleep(0.2)
    






