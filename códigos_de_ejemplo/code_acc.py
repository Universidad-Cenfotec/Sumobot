from ideaboard import IdeaBoard
from time import sleep
import board
from adafruit_msa3xx import MSA311
from hcsr04 import HCSR04 # Librerías para el sensor de Ultrasonido
import random  # Librerías de números aleatorios
import storage #para guardar datos en memoria

sonar = HCSR04(board.IO26,board.IO25) # Crea una instanciación del sensor ultrasonido
ib = IdeaBoard() # Instanciación I/O y funcione sdel Ideboard
irSensor =  ib.DigitalIn(board.IO33) # Instanciación del sensor infrarojo
i2c = board.I2C()  # uses board.SCL and board.SDA# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
msa = MSA311(i2c)


#############

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
    #sleep(0.01)
    return dist





def detect_movement_direction(samples,msa, threshold=0.1):
    sum_x, sum_y = 0, 0
    
    # Tomar muestras y sumar las aceleraciones
    for _ in range(samples):
        x, y, _ = msa.acceleration  # Ignora el valor en z
        sum_x += x 
        sum_y += y 
       # time.sleep(0.1)  # Pequeña pausa para no saturar el acelerómetro

    # Calcular los promedios
    avg_x = sum_x / samples
    avg_y = sum_y / samples

    # Determinar la dirección del movimiento en X
    if abs(avg_x) > threshold:
        direction_x = 0 if avg_x > 0 else -1
    else:
        direction_x = 0  # Sin movimiento significativo en X
    
    # Determinar la dirección del movimiento en Y
    if abs(avg_y) > threshold:
        direction_y = 1 if avg_y > 0 else -1
    else:
        direction_y = 0  # Sin movimiento significativo en Y

    return direction_x, direction_y




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

def acceleration_xyz(samples, msa):
    sumx, sumy, sumz = 0, 0, 0
    for _ in range(samples):
        x, y, z = msa.acceleration
        sumx += x
        sumy += y
        sumz += z
    return round(sumx / samples,1), round(sumy / samples,1), round(sumz / samples,1)


def guardar_datos(datos):
    with open("datos.csv", "a") as f:
        f.write(",".join(str(d) for d in datos) + "\n")
             
###### CODIGO PRINCIPAL   #######

sleep(10) # da 3 segundoas para arrancar el código principal

while True:
    ax =acceleration_xyz(5,msa)
    print(f"{ax[0]:.1f}, {ax[1]:.1f},{ax[2]:.1f}")
    guardar_datos(ax)
   # print(lookForward())
    #print("-----")
    #sleep(0.01)