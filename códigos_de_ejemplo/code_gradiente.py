# Tomás de Camino Beck, Ph.D
# Universidad CENFOTEC

import math

# Clase que representa un vector con magnitud y ángulo
class Vector:
    def __init__(self, mag=0.0, ang=0.0):
        self.mag = mag  # Magnitud del vector
        self.ang = ang  # Ángulo del vector en radianes

def gradient(s1, s2, s3, s4):
    """
    Calcula la magnitud y dirección del gradiente usando cuatro sensores.
    Técnica: Wombling (detección de bordes o gradientes a partir de datos espaciales).
    Disposición esperada de los sensores:
        s2 --- s1   (parte frontal del robot)
         |     |
        s4 --- s3   (parte posterior del robot)

    Parámetros:
        s1, s2, s3, s4: Lecturas de sensores colocados en una cuadrícula de 2x2.
    Retorna:
        Vector con la magnitud y ángulo (en radianes) del gradiente detectado.
    """

    # Estimación del componente en x del gradiente (dirección horizontal)
    dx = s4 - s3 + 0.5 * (s3 - s4 + s2 - s1)   
    # Estimación del componente en y del gradiente (dirección vertical)
    dy = s1 - s3 + 0.5 * (s3 - s4 + s2 - s1)
    # Magnitud del gradiente (teorema de Pitágoras)
    mag = math.sqrt(dx**2 + dy**2)
    # Dirección del gradiente en radianes (de dx respecto a dy)
    ang = math.atan2(dx, dy)  # Se puede agregar +π si se desea invertir la orientación
    return Vector(mag, ang)

