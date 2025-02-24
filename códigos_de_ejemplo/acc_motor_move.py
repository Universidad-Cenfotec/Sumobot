# Emanuel Mena Araya
# Universidad CENFOTEC
from ideaboard import IdeaBoard
import math
import board
import time
from adafruit_lsm6ds import Rate, AccelRange, GyroRange
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

# Definir pi para conversiones de grados a radianes y viceversa
pi = math.pi

# Inicializamos la IdeaBoard, que controla motores y LEDs
ib = IdeaBoard()

# Configuramos el bus I2C y el acelerómetro/giroscopio LSM6DS3TRC
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, 0x6b)

# Configuración del acelerómetro y giroscopio:
sensor.accelerometer_range = AccelRange.RANGE_8G        # Rango del acelerómetro a ±8G
sensor.gyro_range = GyroRange.RANGE_2000_DPS              # Rango del giroscopio a ±2000°/s
sensor.accelerometer_data_rate = Rate.RATE_1_66K_HZ        # Frecuencia de muestreo del acelerómetro
sensor.gyro_data_rate = Rate.RATE_1_66K_HZ                 # Frecuencia de muestreo del giroscopio

# Modo de depuración: cambia a False para quitar los prints de depuración
DEBUG = True

def calcular_drift_promedio(sensor, tiempo_total=3):
    """
    Calcula el sesgo (bias) promedio del giroscopio en reposo.
    
    Durante un periodo de 'tiempo_total' segundos, se promedian las lecturas del eje Z
    del giroscopio para estimar el drift. Esto es útil para corregir pequeñas imprecisiones
    en la medición de la velocidad angular.
    
    Parámetros:
      - sensor: Objeto sensor configurado con giroscopio.
      - tiempo_total: Tiempo en segundos para tomar mediciones (default 3 s).
    
    Retorna:
      - Drift promedio en rad/s (con signo).
    """
    drift_acumulado = 0.0
    tiempo_inicio = time.monotonic()
    numero_mediciones = 0

    # Se utiliza un delay corto para tomar muestras rápidas y precisas
    while (time.monotonic() - tiempo_inicio) < tiempo_total:
        drift_acumulado += sensor.gyro[2]
        numero_mediciones += 1
        time.sleep(0.001)
        
    return drift_acumulado / numero_mediciones if numero_mediciones else 0.0

def corregir_drift(vel_angular, drift_por_segundo):
    """
    Corrige la velocidad angular restando el drift calculado.
    
    Parámetros:
      - vel_angular: Velocidad angular medida (rad/s).
      - drift_por_segundo: Valor de drift promedio (rad/s).
    
    Retorna:
      - Velocidad angular corregida (rad/s).
    """
    return vel_angular - drift_por_segundo

def grados_a_radianes(grados):
    """
    Convierte un ángulo de grados a radianes.
    
    Parámetros:
      - grados: Ángulo en grados.
    
    Retorna:
      - Ángulo en radianes.
    """
    return grados * (pi / 180)

def radianes_a_grados(radianes):
    """
    Convierte un ángulo de radianes a grados.
    
    Parámetros:
      - radianes: Ángulo en radianes.
    
    Retorna:
      - Ángulo en grados.
    """
    return radianes * (180 / pi)

def girar(objetivo_grados, driftPromedio, velocidad_max=0.2, velocidad_min=0.05):
    """
    Realiza un giro controlado integrando la velocidad angular hasta alcanzar el ángulo deseado.
    
    Se utiliza un control proporcional para ajustar la velocidad de giro conforme se acerca
    al objetivo, lo que permite una mayor precisión.
    
    Parámetros:
      - objetivo_grados: Ángulo deseado en grados (positivo indica giro a la derecha, negativo a la izquierda).
      - driftPromedio: Sesgo del giroscopio obtenido en la calibración.
      - velocidad_max: Velocidad máxima de giro.
      - velocidad_min: Velocidad mínima de giro para asegurar que el robot se mueva.
    """
    # Determinamos la dirección de giro:
    # Para un giro a la derecha, se espera que sensor.gyro[2] sea negativo.
    if objetivo_grados > 0:
        multiUno = 1   # Motor 1
        multiDos = -1  # Motor 2
    else:
        multiUno = -1
        multiDos = 1

    angulo_acumulado = 0.0
    last_time = time.monotonic()
    
    # Integramos la velocidad angular hasta alcanzar el ángulo deseado
    while abs(angulo_acumulado) < abs(objetivo_grados):
        current_time = time.monotonic()
        dt = current_time - last_time
        last_time = current_time

        if dt < 0.001:
            continue  # Saltamos iteraciones con dt muy pequeño para evitar errores

        # Lectura del giroscopio y corrección del drift
        vel_cruda = sensor.gyro[2]
        vel_corregida = corregir_drift(vel_cruda, driftPromedio)
        delta_rad = vel_corregida * dt
        delta_grados = radianes_a_grados(delta_rad)
        angulo_acumulado += abs(delta_grados)

        # Control proporcional para ajustar la velocidad de giro
        error = abs(objetivo_grados) - abs(angulo_acumulado)
        factor = error / abs(objetivo_grados)
        velocidad_actual = max(velocidad_min, velocidad_max * factor)
        
        if DEBUG:
            print(f"dt: {dt:.4f}s | vel_cruda: {vel_cruda:.4f} rad/s | vel_corregida: {vel_corregida:.4f} rad/s | Δ°: {abs(delta_grados):.2f} | Total: {angulo_acumulado:.2f}° | V_act: {velocidad_actual:.3f}")

        # Aplicamos la velocidad a los motores (dirección determinada por multiUno y multiDos)
        ib.motor_1.throttle = velocidad_actual * multiUno
        ib.motor_2.throttle = velocidad_actual * multiDos
        
        time.sleep(0.005)
    
    # Detenemos los motores al finalizar el giro
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0

# -----------------------------------------------------------------------------
# Programa principal: calibración y ejecución de giro
# -----------------------------------------------------------------------------

# Calibración del drift del giroscopio en 3 segundos
drift = calcular_drift_promedio(sensor, tiempo_total=3)
print(f"Drift Promedio (bias): {drift:.4f} rad/s")

# Realizar un giro de 90° a la derecha (nota: usamos -90 para indicar la dirección)
girar(-90, drift, 0.2, 0.15)
print("Giro completado.")

