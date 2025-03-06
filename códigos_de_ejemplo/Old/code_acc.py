from ideaboard import IdeaBoard
from time import sleep
import board
from adafruit_msa3xx import MSA311 #https://github.com/adafruit/Adafruit_CircuitPython_MSA301 
from hcsr04 import HCSR04 # Librerías para el sensor de Ultrasonido
import random  # Librerías de números aleatorios
import storage #para guardar datos en memoria

sonar = HCSR04(board.IO26,board.IO25) # Crea una instanciación del sensor ultrasonido
ib = IdeaBoard() # Instanciación I/O y funcione sdel Ideboard
irSensor =  ib.DigitalIn(board.IO33) # Instanciación del sensor infrarojo
i2c = board.I2C()  # uses board.SCL and board.SDA# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
msa = MSA311(i2c)


#############

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
