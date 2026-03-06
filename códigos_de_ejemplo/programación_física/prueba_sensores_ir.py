import board
import time
from ideaboard import IdeaBoard

ib = IdeaBoard()

# Sensores infrarrojos
sen1 = ib.AnalogIn(board.IO27)  # Delantero izquierdo
sen2 = ib.AnalogIn(board.IO33)  # Delantero derecho
sen3 = ib.AnalogIn(board.IO32)  # Trasero izquierdo
sen4 = ib.AnalogIn(board.IO35)  # Trasero derecho

archivo = "datos_bits.txt"

UMBRAL_BLANCO = 3500
UMBRAL_NEGRO = 5000


def sensor_a_bit(valor):

    if valor < UMBRAL_BLANCO:
        return 1

    elif valor > UMBRAL_NEGRO:
        return 0

    else:
        return -1


def guardar(texto):
    with open(archivo, "a") as f:
        f.write(texto)


print("Iniciando registro de sensores...\n")

while True:

    v1 = sen1.value
    v2 = sen2.value
    v3 = sen3.value
    v4 = sen4.value

    b1 = sensor_a_bit(v1)
    b2 = sensor_a_bit(v2)
    b3 = sensor_a_bit(v3)
    b4 = sensor_a_bit(v4)

    binario = f"{b1}{b2}{b3}{b4}"

    bloque = (
        "------ Lectura de sensores ------\n"
        f"Sensor 1 (Delantero izquierdo) : valor={v1} -> bit={b1}\n"
        f"Sensor 2 (Delantero derecho)   : valor={v2} -> bit={b2}\n"
        f"Sensor 3 (Trasero izquierdo)   : valor={v3} -> bit={b3}\n"
        f"Sensor 4 (Trasero derecho)     : valor={v4} -> bit={b4}\n"
        f"Combinación binaria detectada: {binario}\n"
        "---------------------------------\n\n"
    )

    print(bloque)

    guardar(bloque)

    time.sleep(3)
