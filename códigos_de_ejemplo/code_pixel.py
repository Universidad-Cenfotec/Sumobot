# Tomás de Camino Beck
# Escuela de Sistemas Inteligentes
# Universidad Cenfotec

#Ejemplo de uso del Led RGB

import board
from ideaboard import IdeaBoard

ib = IdeaBoard()

## CODIGO PRINCIPAL ##

while True:
    #Neopixel   R   G    B
    ib.pixel = (  0,100,255)
