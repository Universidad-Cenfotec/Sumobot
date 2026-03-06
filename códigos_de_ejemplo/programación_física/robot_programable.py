# =========================================================
# SUMOBOT PROGRAMABLE CON CONTROL DE MOVIMIENTO PRECISO
# Universidad CENFOTEC
# Usa sensores IR para programar instrucciones
# Usa giroscopio para mover el robot recto y girar con precisión
# =========================================================

import time
import board
import keypad
import math

from ideaboard import IdeaBoard
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC


# =========================================================
# INICIALIZACIÓN DEL ROBOT
# =========================================================

# Crear objeto de la placa IdeaBoard
ib = IdeaBoard()

# Inicializar bus I2C
i2c = board.I2C()

# Inicializar sensor giroscopio/acelerómetro
sensor = LSM6DS3TRC(i2c, 0x6b)

# Conversión de radianes a grados
RAD_A_GRADOS = 180 / math.pi


# =========================================================
# SENSORES IR PARA PROGRAMACIÓN
# =========================================================

sen1 = ib.AnalogIn(board.IO27)  # delantero izquierdo
sen2 = ib.AnalogIn(board.IO33)  # delantero derecho
sen3 = ib.AnalogIn(board.IO32)  # trasero izquierdo
sen4 = ib.AnalogIn(board.IO35)  # trasero derecho

UMBRAL_BLANCO = 3500
UMBRAL_NEGRO = 5000


# =========================================================
# BOTÓN BOOT
# =========================================================

keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)

def boton_boot():
    event = keys.events.get()
    return event and event.pressed


# =========================================================
# CALIBRAR GIROSCOPIO
# =========================================================
# El giroscopio siempre tiene un pequeño error llamado "drift"
# Aquí lo medimos para poder corregirlo.

def calibrar_drift(sensor, segundos=3):

    print("Calibrando giroscopio... NO MOVER EL ROBOT")

    suma = 0
    muestras = 0

    t0 = time.monotonic()

    while time.monotonic() - t0 < segundos:

        data = sensor.gyro[2]

        # ignorar lecturas con ruido
        if abs(data) < 0.008:

            suma += data
            muestras += 1

        time.sleep(0.005)

    drift = suma / muestras

    print("Drift calculado:", drift)

    return drift


# =========================================================
# GIRO PRECISO POR GRADOS
# =========================================================

def girar_grados(grados, velocidad=0.35):

    global drift

    sentido = 1 if grados > 0 else -1

    grados = abs(grados) - 2
    acumulado = 0

    t_anterior = time.monotonic()

    ib.motor_1.throttle = velocidad * sentido
    ib.motor_2.throttle = -velocidad * sentido

    while acumulado < grados:

        t_actual = time.monotonic()
        dt = t_actual - t_anterior
        t_anterior = t_actual

        vel = sensor.gyro[2] - drift

        delta = vel * dt * RAD_A_GRADOS

        acumulado += abs(delta)

        # desacelerar cerca del objetivo
        if grados - acumulado < 45:

            ib.motor_1.throttle = 0.18 * sentido
            ib.motor_2.throttle = -0.18 * sentido

        time.sleep(0.005)

    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0


# =========================================================
# AVANZAR RECTO CON CONTROL PDI
# =========================================================

def avanzar_recto(velocidad, duracion):

    global drift

    t0 = time.monotonic()

    base = abs(velocidad)
    direccion = 1 if velocidad > 0 else -1

    Kp = 0.15
    Ki = 0.8
    Kd = 0.05

    error_anterior = 0
    error_integral = 0

    while time.monotonic() - t0 < duracion:

        error = sensor.gyro[2] - drift

        error_integral += error

        error_deriv = error - error_anterior

        correccion = Kp*error + Ki*error_integral + Kd*error_deriv

        correccion = max(-0.3, min(0.3, correccion))

        v1 = base * direccion + correccion
        v2 = base * direccion - correccion

        v1 = max(-1, min(1, v1))
        v2 = max(-1, min(1, v2))

        ib.motor_1.throttle = v1
        ib.motor_2.throttle = v2

        error_anterior = error

        time.sleep(0.01)

    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0


# =========================================================
# FUNCIONES DE MOVIMIENTO
# =========================================================

def detener():
    print(">>> ACCIÓN: DETENER")
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0


def avanzar():
    print(">>> ACCIÓN: AVANZAR RECTO")
    avanzar_recto(0.5,5)


def retroceder():
    print(">>> ACCIÓN: RETROCEDER RECTO")
    avanzar_recto(-0.5,5)


def girar_derecha():
    print(">>> ACCIÓN: GIRAR DERECHA 90°")
    girar_grados(90)


def girar_izquierda():
    print(">>> ACCIÓN: GIRAR IZQUIERDA 90°")
    girar_grados(-90)


def giro_180():
    print(">>> ACCIÓN: GIRO 180°")
    girar_grados(180)


# =========================================================
# FUNCIONES DE LED
# =========================================================

def led_verde():

    print(">>> ACCIÓN: LED VERDE")

    ib.pixel = (0,255,0)
    time.sleep(3)
    ib.pixel = (0,0,0)


def led_rojo():

    print(">>> ACCIÓN: LED ROJO")

    ib.pixel = (255,0,0)
    time.sleep(3)
    ib.pixel = (0,0,0)


def led_azul():

    print(">>> ACCIÓN: LED AZUL")

    ib.pixel = (0,0,255)
    time.sleep(3)
    ib.pixel = (0,0,0)


# =========================================================
# CELEBRACIÓN
# =========================================================

def celebrar():

    print(">>> ACCIÓN: CELEBRACIÓN")

    for i in range(6):

        ib.pixel = (255,0,0)
        time.sleep(0.2)

        ib.pixel = (0,255,0)
        time.sleep(0.2)

        ib.pixel = (0,0,255)
        time.sleep(0.2)

    ib.pixel = (0,0,0)


# =========================================================
# TABLA DE ACCIONES (CÓDIGOS BINARIOS)
# =========================================================

acciones = {

"1100": ("Avanzar", avanzar),
"0011": ("Retroceder", retroceder),
"1001": ("Girar derecha", girar_derecha),
"0110": ("Girar izquierda", girar_izquierda),
"1110": ("Giro 180°", giro_180),
"0101": ("LED verde", led_verde),
"0010": ("LED rojo", led_rojo),
"0001": ("LED azul", led_azul),
"0111": ("Celebración", celebrar),
"0000": ("Detener", detener)

}


# =========================================================
# EJECUTAR INSTRUCCIÓN
# =========================================================

def ejecutar(codigo):

    if codigo in acciones:

        nombre, funcion = acciones[codigo]

        print("\nCódigo:", codigo)
        print("Acción:", nombre)

        funcion()

    else:

        print("Código no válido:", codigo)


# =========================================================
# LED DE ESPERA
# =========================================================

def espera_parpadeo():

    print("\nEsperando próxima lectura")

    for i in range(6):

        ib.pixel = (255,255,255)
        time.sleep(0.5)

        ib.pixel = (0,0,0)
        time.sleep(0.5)

    ib.pixel = (0,255,0)
    time.sleep(1.5
               )
    ib.pixel = (0,0,0)


# =========================================================
# LEER CÓDIGO DE LOS SENSORES
# =========================================================

def valor_a_bit(valor):

    if valor < UMBRAL_BLANCO:
        return 1

    elif valor > UMBRAL_NEGRO:
        return 0

    else:
        return -1


def leer_codigo():

    b1 = valor_a_bit(sen1.value)
    b2 = valor_a_bit(sen2.value)
    b3 = valor_a_bit(sen3.value)
    b4 = valor_a_bit(sen4.value)

    codigo = f"{b1}{b2}{b3}{b4}"

    print("\nCódigo detectado:", codigo)

    return codigo


# =========================================================
# VARIABLES DE PROGRAMA
# =========================================================

programa = []
modo_programacion = False
MAX_INSTRUCCIONES = 6


# =========================================================
# CALIBRAR GIROSCOPIO AL INICIAR
# =========================================================

ib.pixel = (255,0,0)

drift = calibrar_drift(sensor,4)

ib.pixel = (0,255,0)

print("Robot listo")
print("Esperando código 1111 para comenzar programación")


# =========================================================
# BUCLE PRINCIPAL
# =========================================================

while True:

    espera_parpadeo()

    codigo = leer_codigo()

    if not modo_programacion and codigo == "1111":

        print("\n*** INICIO DE PROGRAMACIÓN ***")

        modo_programacion = True
        programa = []

        continue


    if modo_programacion:

        if codigo == "1111":
            print("1111 ignorado")
            continue

        if codigo in acciones:

            nombre, _ = acciones[codigo]

            programa.append(codigo)

            print("Guardado:", codigo, "->", nombre)
            print("Cantidad:", len(programa), "/", MAX_INSTRUCCIONES)

        else:

            print("Código no válido, no se guarda")


        if len(programa) == MAX_INSTRUCCIONES:

            print("\nPrograma final")

            for c in programa:

                nombre, _ = acciones[c]
                print(c, "->", nombre)

            ib.pixel = (255,255,0)

            print("\nPresiona BOOT para ejecutar")

            while True:
                if boton_boot():
                    break

            print("\n*** EJECUTANDO PROGRAMA ***")

            for instruccion in programa:

                ejecutar(instruccion)

            print("\nPrograma terminado")

            programa = []
            modo_programacion = False

            ib.pixel = (0,0,0)

            print("\nEsperando nuevo 1111")
