#Tomás de Camino Beck, Ph.D
#Universidad CENFOTEC

import math

class Vector:
    def __init__(self, mag=0.0, ang=0.0):
        self.mag = mag
        self.ang = ang

def gradient(s1, s2, s3, s4):
    """
    Calcula la magnitud y dirección del gradiente usando cuatro sensores.

    Disposición (sensores Sumobot):
        Top:    s2, s1
        Bottom: s4, s3
    """
    dx = s4 - s3 + 0.5 * (s3 - s4 + s2 - s1)
    dy = s1 - s3 + 0.5 * (s3 - s4 + s2 - s1)
    mag = math.sqrt(dx**2 + dy**2)
    ang = math.atan2(dx, dy) #+ math.pi
    return Vector(mag, ang)
