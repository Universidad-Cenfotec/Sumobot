# Tomás de Camino Beck
# Universidad Cenfotec

# Programa para leer sensores infrarrojos conectados a una IdeaBoard.
# El programa lee continuamente los valores de 4 sensores infrarrojos analógicos
# y muestra en pantalla el número de cada sensor junto con su valor actual

# Importa los módulos necesarios
import board               # Permite acceder a los pines de entrada/salida del microcontrolador
from time import sleep     # Permite usar la función sleep para pausar el programa
from ideaboard import IdeaBoard   # Importa la clase IdeaBoard para controlar los sensores y actuadores

# Crea una instancia de la IdeaBoard para controlar el hardware conectado
ib = IdeaBoard()

# Configura los pines analógicos donde están conectados los sensores infrarrojos
sen1 = ib.AnalogIn(board.IO36)  # SENSOR 1 (adelante izquierdo) pin IO36
sen2 = ib.AnalogIn(board.IO39)  # SENSOR 2 (adelante derecho) pin IO39
sen3 = ib.AnalogIn(board.IO34)  # SENSOR 3 (atrás izquierdo) pin IO34
sen4 = ib.AnalogIn(board.IO35)  # SENSOR 4 (atrá derecho) pin IO35

# Crea una lista con los sensores infrarrojos para poder recorrerlos fácilmente
infrarrojos = [sen1, sen2, sen3, sen4]

# Bucle infinito que lee e imprime los valores de los sensores continuamente
while True: 
    # Recorre cada sensor de la lista junto con su número (empezando desde 1)
    for i, sen in enumerate(infrarrojos, start=1):
        # Imprime el número de sensor y su valor analógico leído
        print(f"SENSOR {i}: {sen.value}")
    
    # Imprime una línea para separar visualmente cada ciclo de lectura
    print("_________")
    
    # Pausa el programa durante 1 segundo antes de leer nuevamente
    sleep(0.5)
