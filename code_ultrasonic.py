import board #Librerías para accesar a I/O de la placa
from ideaboard import IdeaBoard # Librería de funciones varias del ideaboard
from time import sleep # Para utilizar función que detiene el código
from hcsr04 import HCSR04 # Librerías para el sensor de Ultrasonido

sonar = HCSR04(board.IO26,board.IO25) # Crea una instanciación del sensor ultrasonido

while True:
    dist = sonar.dist_cm()
    print(dist)
    sleep(0.5)