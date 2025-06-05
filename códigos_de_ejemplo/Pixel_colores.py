# Fiorella Pérez López.
# Universidad Cenfotec.

# Código para probar las diferentes combinaciones de color del NeoPixel del IdeaBoard.

from ideaboard import IdeaBoard  # Importa la clase IdeaBoard
import time                      # Importa el módulo time para usar pausas

ib = IdeaBoard()                 # Crea una instancia del IdeaBoard
ib.brightness = 0.2              # Ajusta el brillo del NeoPixel (0.0 a 1.0)

# Función que apaga el LED
def apagar_led():
    ib.pixel = (0, 0, 0)         # Asigna el color negro (apagado)

# Instrucciones para el usuario
print("Escribe un color: rojo, verde, azul, amarillo, celeste, lila o blanco.")
print("También puedes escribir STOP para apagar el LED y detener el programa.")

# Bucle principal que espera la entrada del usuario
while True:
    comando = input("Digite el color: ").strip().lower()  # Lee el texto ingresado, elimina espacios y lo convierte a minúscula

    # Condiciones para cada color reconocido
    if comando == "rojo":
        ib.pixel = (255, 0, 0)           # Rojo
    elif comando == "verde":
        ib.pixel = (0, 255, 0)           # Verde
    elif comando == "azul":
        ib.pixel = (0, 0, 255)           # Azul
    elif comando == "amarillo":
        ib.pixel = (255, 255, 0)         # Amarillo
    elif comando == "celeste":
        ib.pixel = (0, 255, 255)         # Celeste 
    elif comando == "lila":
        ib.pixel = (255, 0, 255)         # Lila
    elif comando == "blanco":
        ib.pixel = (255, 255, 255)       # Blanco
    elif comando == "stop":
        apagar_led()                     # Apaga el LED
        print("Programa detenido.")     
        break                            # Sale del bucle
    else:
        # Mensaje si el comando no es válido
        print("Comando no reconocido. Intenta con: rojo, verde, azul, amarillo, celeste, lila, blanco o STOP.")

    time.sleep(0.1)  # Pequeña pausa para evitar sobrecargar el bucle