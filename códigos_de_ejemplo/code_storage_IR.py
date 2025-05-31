# Tomás de Camino Beck
# Universidad CENFOTEC

# Módulo para manejar almacenamiento interno (para guardar archivos)
import storage

# Importa la clase IdeaBoard que facilita el acceso a sensores y pines del ESP32
from ideaboard import IdeaBoard

# Módulo para manejo de pausas (esperas en segundos)
from time import sleep

# Acceso a los pines físicos del microcontrolador
import board

# Librería para sensores ultrasónicos HCSR04 (aunque en este código no se usa)
from hcsr04 import HCSR04

# Inicializa la IdeaBoard
ib = IdeaBoard()

# Define los pines analógicos donde están conectados los sensores infrarrojos (IR)
sen1 = ib.AnalogIn(board.IO36)  # SENSOR 1 (frontal izquierdo)
sen2 = ib.AnalogIn(board.IO39)  # SENSOR 2 (frontal derecho)
sen3 = ib.AnalogIn(board.IO34)  # SENSOR 3 (trasero izquierdo)
sen4 = ib.AnalogIn(board.IO35)  # SENSOR 4 (trasero derecho)

# Crea una lista con todos los sensores IR para facilitar su uso
infrarrojos = [sen1, sen2, sen3, sen4]

# Función que convierte un arreglo de bits (lista de 0 y 1) a un número entero
# usando desplazamiento de bits
def arreglo_a_entero(bits):
    valor = 0
    for bit in bits:
        valor = (valor << 1) | bit  # Desplaza a la izquierda y agrega el nuevo bit
    return valor

# Función para leer los sensores infrarrojos
# Devuelve una lista de 0s y 1s donde 0 es superficie clara (blanco) y 1 es oscura (negro)
# El parámetro valor_critico define el umbral entre claro y oscuro
def leer_sensores(infrarrojos, valor_critico=3000):
    return [int(sen.value < valor_critico) for sen in infrarrojos]

# Función para guardar datos en un archivo CSV
# Cada línea es una lista de valores separados por comas
def guardar_datos(archivo: str, datos):
    """
    Guarda una lista de datos en un archivo CSV, añadiendo cada nueva entrada en una nueva línea.

    Args:
        archivo (str): El nombre del archivo donde se guardarán los datos.
        datos (list): Lista de datos (cualquier tipo que pueda ser convertido a string).

    Returns:
        None
    """   
    with open(archivo, "a") as f:
        f.write(",".join(str(d) for d in datos) + "\n")

# Bucle principal del programa
# Lee los valores actuales de los sensores IR y los guarda en un archivo
while True:
    try:
        # Lee los valores crudos (entre 0 y 65535) de los sensores
        estado = [sen.value for sen in infrarrojos]
        # Guarda los datos en el archivo datos.csv
        guardar_datos("datos.csv", estado)
    except RuntimeError as e:
        # En caso de error al leer un sensor, imprime el error
        print("Error al leer el sensor:", e)
