# Tomás de Camino Beck
# Escuela de Sistemas Inteligentes
# Universidad Cenfotec

# Ejemplo de uso del sensor infrarrojo conectado al IO33

import board
from ideaboard import IdeaBoard

ib = IdeaBoard()
irSensor = ib.AnalogIn(board.IO36)

while True:
    print(irSensor.value)
