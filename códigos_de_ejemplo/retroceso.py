# Importa las librerías necesarias
import board                 # Maneja las conexiones de hardware (aunque aquí no se usa directamente)
from time import sleep       # Permite pausar el programa durante cierto tiempo
from ideaboard import IdeaBoard  # Importa la clase IdeaBoard para controlar el robot

# Crea un objeto IdeaBoard para controlar los motores y el LED
ib = IdeaBoard()

# Define una función para detener el robot
def stop():
    # Apaga el LED
    ib.pixel = (0,0,0)
    # Detiene los motores (throttle en 0 significa apagado)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

# Define una función para mover el robot hacia atrás
def backward(t, speed):
    # Enciende el LED en color azul para indicar que va hacia atrás
    ib.pixel = (0,0,255)
    # Ajusta los motores para ir hacia atrás (velocidad negativa)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    # Espera el tiempo indicado mientras se mueve
    sleep(t)
    # Luego de moverse, detiene el robot
    stop()

# Bucle principal: se repite para siempre
while True:
    # Mueve el robot hacia atrás durante 1 segundo a velocidad máxima (1)
    backward(1, 1)
    # Espera 3 segundos antes de volver a moverse
    sleep(3)
    # Se asegura de que el robot esté detenido (esto es redundante aquí porque backward ya lo detiene)
    stop()
    # Espera otros 3 segundos antes de repetir
    sleep(3)
