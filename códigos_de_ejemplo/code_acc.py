from time import sleep
import board
from adafruit_lsm6ds import Rate, AccelRange, GyroRange
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC
import storage  # Para guardar datos en memoria


# Inicialización del bus I2C y configuración del acelerómetro/giroscopio LSM6DS3TRC
i2c = board.I2C()  # Usa board.SCL y board.SDA
sensor = LSM6DS3TRC(i2c, 0x6b)  # Dirección I2C del LSM6DS3TRC

# Configuración del sensor:
sensor.accelerometer_range = AccelRange.RANGE_8G          # Rango del acelerómetro a ±8G
sensor.gyro_range = GyroRange.RANGE_2000_DPS                # Rango del giroscopio a ±2000°/s
sensor.accelerometer_data_rate = Rate.RATE_1_66K_HZ          # Frecuencia de muestreo del acelerómetro
sensor.gyro_data_rate = Rate.RATE_1_66K_HZ                   # Frecuencia de muestreo del giroscopio

#############
def acceleration_xyz(samples, sensor):
    """
    Calcula el promedio de aceleración en los ejes X, Y y Z a partir de 'samples' muestras.
    
    Parámetros:
      - samples: Número de muestras a promediar.
      - sensor: Instancia del sensor LSM6DS3TRC.
      
    Retorna:
      - Una tupla (x, y, z) con los promedios de aceleración, redondeados a una cifra decimal.
    """
    sumx, sumy, sumz, sumGx, sumGy, sumGz = 0, 0, 0, 0, 0, 0
    for _ in range(samples):
        x, y, z = sensor.acceleration
        gX, gY, gZ = sensor.gyro

        sumx += x
        sumy += y
        sumz += z

        sumGx += gX
        sumGy += gY 
        sumGz += gZ
    return round(sumx / samples, 1), round(sumy / samples, 1), round(sumz / samples, 1), round(sumGx / samples, 1), round(sumGy / samples, 1), round(sumGz / samples, 1)

def guardar_datos(datos):
    """
    Guarda los datos en un archivo CSV.
    
    Cada llamada añade una nueva línea al archivo 'datos.csv' con los datos separados por comas.
    """
    with open("datos.csv", "a") as f:
        f.write(",".join(str(d) for d in datos) + "\n")

sleep(10)  # Espera 10 segundos antes de iniciar el ciclo principal

while True:
    # Obtiene el promedio de 5 muestras de aceleración en X, Y y Z
    ax = acceleration_xyz(5, sensor)
    print(f"Acelerometro: {ax[0]:.1f}, {ax[1]:.1f}, {ax[2]:.1f} Giroscopio{ax[3]:.1f}, {ax[4]:.1f}, {ax[5]:.1f}")
    
    # Guarda los datos en 'datos.csv'
    guardar_datos(ax)
    
    # Aquí podrías agregar otras funciones, por ejemplo, para leer el sensor ultrasónico o infrarrojo.
    sleep(0.1)  # Ajusta el retardo según lo requieras
