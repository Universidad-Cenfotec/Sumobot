# Emanuel Mena Araya
# Universidad CENFOTEC

# Este es un código simple para probar todas los sensores del SumoBot de la Universidad CENFOTEC
# El código realiza una serie de pruebas en los diferentes módulos del robot, asegurando que cada
# componente está respondiendo como debería.

import sys
import board
from time import sleep
import time
import math

# Definir 'pi' globalmente para usar en conversiones
pi = math.pi

# Lista para almacenar mensajes de error en caso de que no se puedan importar módulos
errores = []
accel_connected = False  # Bandera para saber si el acelerómetro está conectado

# Intentamos importar la librería IdeaBoard para manejar los componentes de la placa
try:
    from ideaboard import IdeaBoard
except ImportError as e:
    error_msg = str(e)
    if "no module named" in error_msg or "ningún módulo se llama" in error_msg:
        print("El módulo ideaboard no se encuentra, asegurate de haberlo importado a tu CircuitPython device")
    elif "cannot import name" in error_msg or "no se puede importar name 'IdeaBoard'" in error_msg:
        print("No se encontró la clase IdeaBoard en el módulo, asegurate de no haberla eliminado o modificado")
    elif "being imported from unexpected location" in error_msg:
        print("Estás intentando correr el código mientras estás en la carpeta de lib, vuelve a ejecutar este código desde la carpeta raíz del CircuitPython device")
    else:
        print("Ocurrió un ImportError inesperado")
    errores.append(error_msg)
    print(f"Mensaje de Error: {error_msg}\n")
else:
    print("Librería IdeaBoard importada correctamente")
    
# Intentamos importar la librería para el sensor ultrasónico HCSR04
try:
    from hcsr04 import HCSR04  # Librería para el sensor de Ultrasonido
except Exception as e:
    error_msg = str(e)
    if "no module named" in error_msg or "ningún módulo se llama" in error_msg:
        print("El módulo hcsr04 no se encuentra, asegurate de haberlo importado a tu CircuitPython device")
    elif "cannot import name" in error_msg or "no se puede importar name 'HCSR04'" in error_msg:
        print(f"El nombre especificado no se encuentra en el módulo: {error_msg}")
    elif ".mpy" in error_msg:
        print(".mpy de hcsr04 incompatible.")
        version = sys.implementation.version
        print(f"Versión CircuitPython: {version[0]}.{version[1]}.{version[2]}")
        print(f"Asegurate de usar una versión {version[0]}.x del archivo .mpy")
    else:
        print("Ocurrió un ImportError inesperado")
    errores.append(error_msg)
    print(f"Mensaje de Error: {error_msg}\n")
else:
    print("Librería HCSR04 importada correctamente")
    
# Intentamos importar la librería para el acelerómetro LSM6DS3TRC y sus configuraciones
try:
    from adafruit_lsm6ds import Rate, AccelRange, GyroRange
    from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC
except ImportError as e:
    error_msg = str(e)
    if "no module named" in error_msg or "ningún módulo se llama" in error_msg:
        print(f"El módulo no se encuentra: {error_msg}")
    elif "cannot import name" in error_msg or "no se puede importar name" in error_msg:
        print(f"El nombre especificado no se encuentra en el módulo: {error_msg}")
    else:
        print("Ocurrió un ImportError inesperado")
        print(f"Mensaje de Error: {error_msg}")
        errores.append(error_msg)
else:
    print("Librería LSM6DS3TRC importada correctamente")
    
    # Inicializamos el bus I2C y el acelerómetro
    try:
        i2c = board.I2C()
        sensor = LSM6DS3TRC(i2c, 0x6b)
    except Exception as e:
        error_msg = str(e)
        errores.append(error_msg)
        if "SDA or SCL" in error_msg:
            print("No tienes el acelerómetro conectado")
        elif "0x6b" in error_msg:
            print("Tienes un dispositivo conectado al puerto I2C pero no es el acelerómetro LSM6DS3TRC")
    else:
        accel_connected = True
    finally:
        if accel_connected:
            print("El acelerómetro LSM6DS3TRC está conectado, el diagnóstico usará de este para una prueba extra")
        else:
            print("El acelerómetro LSM6DS3TRC no está conectado, no se usará en el diagnóstico")

# Mostramos todos los módulos cargados para fines de depuración (porque, a veces, necesitas ver quién está en la fiesta)
modulos = sys.modules
print("\nMódulos Cargados:")
sleep(0.5)
for clave, valor in modulos.items():
    print(f"{clave}: {valor}")
    sleep(0.07)  # Este sleep es para que se vea fancy; puedes quitarlo si quieres ¯\_(ツ)_/¯
    
# Si hubo errores críticos al importar, detenemos el diagnóstico
if len(errores) > 0:
    print("No se puede iniciar el diagnóstico debido a los siguientes errores:")
    for error in errores:
        print(error)
    # En algunos dispositivos CircuitPython, 'input' puede no funcionar correctamente.
    try:
        input("Presione Enter para salir del programa: ")
    except Exception:
        pass
    sys.exit()
  
# Inicializamos la IdeaBoard, el sensor ultrasónico y los sensores infrarrojos (analógicos)
ib = IdeaBoard()
sonar = HCSR04(board.IO25, board.IO26)
sen1 = ib.AnalogIn(board.IO36)
sen2 = ib.AnalogIn(board.IO39)
sen3 = ib.AnalogIn(board.IO34)
sen4 = ib.AnalogIn(board.IO35)
infrarrojos = [sen1, sen2, sen3, sen4]

# Definimos algunos colores en formato RGB para usar en los LEDs del board
AMARILLO = (244, 206,   0)
AZUL     = (  0, 105, 255)
ROJO     = (255,  23,  16)
VERDE    = (  0, 255,  40)
MORADO   = (208,  43, 208)
MAGENTA  = (255,  27, 238)
NARANJA  = (255, 151,  66)
CYAN     = (  0, 222, 163)

# Si el acelerómetro está conectado, configuramos sus rangos y tasas de datos
if accel_connected:
    sensor.accelerometer_range = AccelRange.RANGE_8G
    sensor.gyro_range = GyroRange.RANGE_2000_DPS
    sensor.accelerometer_data_rate = Rate.RATE_1_66K_HZ
    sensor.gyro_data_rate = Rate.RATE_1_66K_HZ

# =============================================================================
# Funciones auxiliares
# =============================================================================

def stop(tiempo=0.1):
    """
    Detiene ambos motores y apaga el LED.
    
    Parámetros:
      - tiempo: Tiempo en segundos para esperar tras detener (default 0.1s)
    """
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
    ib.pixel = (0, 0, 0)  # Apagar luces al detenerse
    sleep(tiempo)
    
def map_value(in_min, in_max, out_min, out_max, value):
    """
    Mapea un valor de un rango (in_min-in_max) a otro rango (out_min-out_max).
    
    Esto es útil para transformar lecturas de sensores a valores de brillo, por ejemplo.
    """
    return out_min + (float(value - in_min) / float(in_max - in_min)) * (out_max - out_min)

def calcular_drift_promedio(sensor, tiempo_total=3):
    """
    Calcula el sesgo (bias) promedio del giroscopio en reposo.
    
    Parámetros:
      - sensor: Objeto sensor (se asume que tiene 'gyro' y está configurado)
      - tiempo_total: Tiempo de calibración en segundos (se recomienda 3s)
    
    Retorna:
      - Drift promedio en rad/s (con signo)
    
    Nota: Durante la calibración, se va actualizando un LED para dar feedback visual.
    """
    print("calculando drift")
    
    drift_acumulado = 0.0
    tiempo_inicio = time.monotonic()
    numero_mediciones = 0
    
    # Incremento para la animación del LED (porque, ¿quién no ama una animación chula mientras calibra?)
    incremento = 255.0 / (56 * tiempo_total)
    var_pixel = 0
    
    # Se utiliza un delay corto (0.04s) para obtener varias mediciones en poco tiempo
    while (time.monotonic() - tiempo_inicio) < tiempo_total:
        drift_acumulado += sensor.gyro[2]
        numero_mediciones += 1
        var_pixel += incremento
        ib.pixel = (0, int(var_pixel) % 256, 0)  # Aseguramos que el valor del LED esté en rango 0-255
        sleep(0.04)
        
    print(numero_mediciones)
    return drift_acumulado / numero_mediciones if numero_mediciones else 0.0

def corregir_drift(vel_angular, drift_por_segundo):
    """
    Corrige la velocidad angular restando el drift (bias) calculado.
    
    Parámetros:
      - vel_angular: Velocidad angular medida (rad/s)
      - drift_por_segundo: Drift promedio (rad/s)
    
    Retorna:
      - Velocidad angular corregida (rad/s)
    """
    return vel_angular - drift_por_segundo

def grados_a_radianes(grados):
    """Convierte grados a radianes."""
    return grados * (pi / 180)

def radianes_a_grados(radianes):
    """Convierte radianes a grados."""
    return radianes * (180 / pi)

def girar(objetivo_grados, driftPromedio, velocidad_max=0.2, velocidad_min=0.15):
    """
    Realiza un giro controlado integrando la velocidad angular hasta alcanzar el ángulo deseado.
    
    Se usa control proporcional para disminuir la velocidad al acercarse al objetivo.
    
    Parámetros:
      - objetivo_grados: Ángulo deseado en grados (positivo para giro a la derecha, negativo para izquierda)
      - driftPromedio: Sesgo del giroscopio obtenido en la calibración
      - velocidad_max: Velocidad máxima de giro
      - velocidad_min: Velocidad mínima de giro (para asegurar que el robot se mueva)
    """
    # Configuramos la dirección de giro para los motores:
    # Para giro a la derecha se espera que sensor.gyro[2] sea negativo.
    if objetivo_grados > 0:
        multiUno = 1   # Motor 1
        multiDos = -1  # Motor 2
    else:
        multiUno = -1
        multiDos = 1

    angulo_acumulado = 0.0
    last_time = time.monotonic()
    
    # Se sigue integrando la velocidad angular hasta que se alcanza el ángulo deseado
    while abs(angulo_acumulado) < abs(objetivo_grados):
        current_time = time.monotonic()
        dt = current_time - last_time
        last_time = current_time

        if dt < 0.001:
            continue  # Evitamos dividir por cero o tener intervalos demasiado cortos

        vel_cruda = sensor.gyro[2]
        vel_corregida = corregir_drift(vel_cruda, driftPromedio)
        delta_rad = vel_corregida * dt
        delta_grados = radianes_a_grados(delta_rad)
        angulo_acumulado += abs(delta_grados)

        # Control proporcional: se reduce la velocidad al acercarse al objetivo
        error = abs(objetivo_grados) - abs(angulo_acumulado)
        factor = error / abs(objetivo_grados)
        velocidad_actual = max(velocidad_min, velocidad_max * factor)
        
        # Debug (puedes descomentar la siguiente línea para ver datos en consola)
        # print(f"dt: {dt:.4f}s | vel_cruda: {vel_cruda:.4f} rad/s | vel_corregida: {vel_corregida:.4f} rad/s | Δ°: {abs(delta_grados):.2f} | Total: {angulo_acumulado:.2f}° | V_act: {velocidad_actual:.3f}")

        ib.motor_1.throttle = velocidad_actual * multiUno
        ib.motor_2.throttle = velocidad_actual * multiDos
        
        sleep(0.005)
    
    # Detenemos los motores al finalizar el giro
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

# =============================================================================
# Secuencia principal del diagnóstico
# =============================================================================

print("\nDiagnóstico listo para realizarse, este se iniciará en 3 segundos")
sleep(3)

# --- Pruebas de motores ---
print("Motor 1: Adelante")
ib.pixel = ROJO 
ib.motor_1.throttle = 1
ib.motor_2.throttle = 0
sleep(1)
stop()

print("Motor 1: Atrás")
ib.pixel = VERDE
ib.motor_1.throttle = -1
ib.motor_2.throttle = 0
sleep(1)
stop()

print("Motor 2: Adelante")
ib.pixel = AZUL
ib.motor_1.throttle = 0
ib.motor_2.throttle = 1
sleep(1)
stop()

print("Motor 2: Atrás")
ib.pixel = AMARILLO
ib.motor_1.throttle = 0
ib.motor_2.throttle = -1
sleep(1)
stop()

print("Motores: Adelante")
ib.pixel = MORADO
ib.motor_1.throttle = 1
ib.motor_2.throttle = 1
sleep(1)
stop()

print("Motores: Atrás")
ib.pixel = MAGENTA
ib.motor_1.throttle = -1
ib.motor_2.throttle = -1
sleep(1)
stop()

print("Motores: Reloj")
ib.pixel = NARANJA
ib.motor_1.throttle = 1
ib.motor_2.throttle = -1
sleep(1)
stop()

print("Motores: Contra Reloj")
ib.pixel = CYAN
ib.motor_1.throttle = -1
ib.motor_2.throttle = 1
sleep(1)
stop()

print("Motores completados")

# --- Diagnóstico de sensores infrarrojos ---
print("Diagnóstico de infrarrojos")
print("Ponga una pieza de papel o un objeto blanco debajo del sensor correspondiente hasta que se lea un valor lo suficientemente bajo")

index = 0
for sen in infrarrojos:
    valor_pixel = 0
    valor = 62556  # Valor inicial alto para comenzar la espera
    index += 1

    # Espera hasta que el sensor detecte suficiente luz (o reflejo)
    while valor > 4000:
        valor = sen.value
        print(f"Sen{index}: {valor}")

        # Mapea el valor del sensor a un brillo inverso para el LED
        valor_pixel = map_value(4000, 62556, 255, 0, valor)
        ib.pixel = (int(valor_pixel), int(valor_pixel), int(valor_pixel))
        sleep(0.5)
        
    # Cuando se detecta un objeto blanco, se enciende el LED con otro color
    ib.pixel = (5, 255, 54)
    sleep(2)
    
sleep(2)

# --- Diagnóstico del sensor ultrasónico ---
print("Diagnóstico de Ultrasonico")
print("Ponga su mano a 15cm del sensor ultrasonico")
ib.pixel = (48, 57, 189)
dist = 0

# Se espera que la distancia se encuentre entre 14 y 16 cm
while (dist <= 14 or dist >= 16):
    dist = sonar.dist_cm()
    print(f"Distancia: {dist}cm")
    if dist > 0 and dist < 15:
        color = map_value(0, 14, 20, 150, dist)
        ib.pixel = (int(color), 0, 0)
    elif dist > 15:
        color = map_value(15, 30, 20, 250, dist)
        ib.pixel = (0, 0, int(color))
    elif dist == -1:
        ib.pixel = NARANJA
    
    sleep(0.5)

# --- Prueba del acelerómetro (si está conectado) ---
if accel_connected: 
    print("Test de Acelerómetro")
    
    drift = calcular_drift_promedio(sensor, 3)
    
    print("Girando 90° a la izquierda")
    ib.pixel = ROJO
    girar(90, drift)
    sleep(1)
    
    print("Girando 90° a la derecha")
    ib.pixel = MORADO
    girar(-90, drift)
    sleep(1)
    
    print("Girando 90° a la derecha")
    ib.pixel = MAGENTA
    girar(-90, drift)
    sleep(1)
    
    print("Girando 90° a la izquierda")
    ib.pixel = VERDE
    girar(90, drift)
    drift = calcular_drift_promedio(sensor, 3)
    
    print("Girando 180° a la izquierda")
    ib.pixel = AZUL
    girar(180, drift)
    sleep(1)
    
    print("Girando 180° a la izquierda")
    ib.pixel = ROJO
    girar(180, drift)
    drift = calcular_drift_promedio(sensor, 3)

    print("Girando 360 a la derecha")
    ib.pixel = MORADO
    girar(-360, drift)
    sleep(1)

print("Diagnóstico Finalizado")

# Bucle infinito para mostrar un efecto arcoíris en el LED final (porque siempre se debe terminar con estilo)
while True:
    for i in range(256):
        ib.arcoiris = i
        sleep(0.01)
