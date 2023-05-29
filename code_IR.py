import board
from ideaboard import IdeaBoard

ib = IdeaBoard()
irSensor = ib.DigitalIn(board.IO33)

while True:
    print(irSensor.value)