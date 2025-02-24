# Tomás de Camino Beck
# Escuela de Sistemas Inteligentes
# Universidad Cenfotec

#Ejemplo de uso del sensor ultrasónico

import board #Librerías para accesar a I/O de la placa
from ideaboard import IdeaBoard # Librería de funciones varias del ideaboard
from time import sleep # Para utilizar función que detiene el código
from hcsr04 import HCSR04 # Librerías para el sensor de Ultrasonido

# TRIG conectado al pin IO26, y ECHO al Pin IO25
sonar = HCSR04(board.IO26,board.IO25) # Crea una instanciación del sensor ultrasonido

while True:
    dist = sonar.dist_cm()
    print(dist)
    sleep(0.5)
