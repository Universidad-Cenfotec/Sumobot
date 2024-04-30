#Tomás de Camino Beck
#Universidad CENFOTEC

import storage
from ideaboard import IdeaBoard
import time
import board
from adafruit_msa3xx import MSA311
from hcsr04 import HCSR04 #

sonar =  HCSR04(board.IO26,board.IO25)



# Función para guardar datos
def guardar_datos(archivo: str, datos):
    with open(archivo, "a") as f:
        f.write(",".join(str(d) for d in datos) + "\n")

# Loop principal
while True:
    try:
        distancia = sonar.dist_cm()
        print("Distancia:", distancia, "cm")
        guardar_datos("datos.csv",[distancia,distancia])
    except RuntimeError as e:
        print("Error al leer el sensor:", e)
    time.sleep(0.2)  # Esperar un segundo antes de la próxima medición
