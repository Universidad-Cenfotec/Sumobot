# Tomás de Camino Beck
# Universidad Cenfotec

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

#funcion que convierte a entero base 10
# Utiliza desplazamiento de bits
def arreglo_a_entero(bits):
    valor = 0
    for bit in bits:
        valor = (valor << 1) | bit
    return valor

# revisa los cuatro sensores IR, y genera un
# arreglo de 0 y 1s (0-blanco, 1-negro)
def leer_sensores(infrarrojos,valor_critico=10000):
    return [int(sen.value > valor_critico) for sen in infrarrojos]

# Bucle infinito que lee e imprime los valores de los sensores continuamente
while True: 
    estado_sensores =leer_sensores(infrarrojos,10000)
    print(estado_sensores)
    print(arreglo_a_entero(estado_sensores))
    sleep(0.1)