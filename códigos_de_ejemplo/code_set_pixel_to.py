# Juan P. Zepeda
# C.C.B Reina de Los Ángeles

# Funcion para cambiar el color del NeoPixel del IdeaBoard usando un input de texto

from ideaboard import IdeaBoard # Librería de funciones varias del ideaboard
from time import sleep # Para utilizar función que detiene el código
ib = IdeaBoard() # Instanciación I/O y funcione sdel Ideboard

def set_pixel_to(color):
    """
    Cambia el color del NeoPixel del IdeaBoard usando un input de texto

    Args:
        color (str): El color a establecer en el LED. Los colores deben ser ingresados en español y en mayúsculas.
        Debe ser uno de los siguientes:
            - ROJO
            - VERDE
            - AZUL
            - NARANJA
            - MORADO
            - ROSADO (o MAGENTA)
            - CYAN
            - AMARILLO
            - BLANCO
            - APAGAR (o OFF)            
    Returns:
        None
    
    """
    if color == 'ROJO':
        ib.pixel = (255, 0, 0)
    elif color == 'VERDE':
        ib.pixel = (0, 255, 0)
    elif color == 'AZUL':
        ib.pixel = (0, 0, 255)
    elif color == 'NARANJA':
        ib.pixel = (255, 165, 0)
    elif color == 'MORADO':
        ib.pixel = (160, 32, 240)
    elif color == 'ROSADO' or color == 'MAGENTA':
        ib.pixel = (255, 0, 255)
    elif color == 'CYAN':
        ib.pixel = (0, 255, 255)
    elif color == 'AMARILLO':
        ib.pixel = (255, 255, 0)
    elif color == 'BLANCO':
        ib.pixel = (255, 255, 255)
    elif color == 'APAGAR' or color == 'OFF':
        ib.pixel = (0, 0, 0)
    else:
        print("Color no reconocido. Por favor, ingresa un color válido.")
        ib.pixel = (0, 0, 0)

###### CODIGO PRINCIPAL   #######

##################################################
# Cambiar color del LED del IdeaBoard directamente
##################################################

set_pixel_to('ROJO')  # Cambia el color del LED a rojo
sleep(1)  # Espera 1 segundo antes de cambiar al siguiente color

set_pixel_to('VERDE')  # Cambia el color del LED a verde
sleep(1)  # Espera 1 segundo antes de cambiar al siguiente color

set_pixel_to('APAGAR')  # Apaga el LED

##################################################################
# Cambiar color del LED del IdeaBoard usando un arreglo de colores
##################################################################

# Lista de colores a probar
arreglo_arcoiris = ['ROJO', 'VERDE', 'AZUL', 'NARANJA', 'MORADO', 'ROSADO', 'CYAN', 'AMARILLO', 'BLANCO']

# Bucle para cambiar el color del LED según los colores en el arreglo usando la función set_pixel_to
for color in arreglo_arcoiris:
    set_pixel_to(color)  # Cambia el color del LED
    print(f"Color del LED cambiado a: {color}")
    sleep(1)  # Espera 1 segundo antes de cambiar al siguiente color

set_pixel_to('APAGAR')  # Apaga el LED al final del bucle
print("Programa finalizado. El LED ha sido apagado.")