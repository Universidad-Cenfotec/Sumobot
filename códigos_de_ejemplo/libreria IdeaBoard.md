![SumoBot](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/ideaboard-sumobot.JPG) 

# Uso de la librería IdeaBoard

El Sumobot utiliza la placa IdeaBoard, que es una placa que utiliza el ESP32, pero agrega drivers de motores, y pines para poder conectar gran cantidad de sensores digitales y analógicos.

Esta guía explica cómo utilizar la librería **IdeaBoard**, que incluye funciones para:

- Controlar los motores incorporados
- Cambiar el color del LED RGB
- Controlar servomotores
- Leer entradas digitales y analógicas
- Generar salidas digitales y analógicas
- Utilizar una función especial llamada `map_range` para ajustar valores entre distintos rangos

> **Nota**: Este documento es una traducción con modificación del documento de apoyo del IdeaBoard. Mayores detalles, los pueden [encontrar acá](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki)

---

## Introducción

Para comenzar a usar las funciones de la IdeaBoard, primero debemos crear un objeto que nos permitirá acceder a todas sus funcionalidades.

```python
from ideaboard import IdeaBoard

ib = IdeaBoard()
````

---

## Control de motores

La IdeaBoard tiene dos motores llamados `motor_1` y `motor_2`. Estos se controlan con la propiedad **throttle**.

* `1.0` significa velocidad máxima hacia adelante
* `-1.0` significa velocidad máxima hacia atrás
* `0` detiene el motor con freno
* `None` deja el motor libre (sin freno)

Ejemplo:

```python
from ideaboard import IdeaBoard

ib = IdeaBoard()

ib.motor_1.throttle = 1.0  # Avanzar
ib.motor_2.throttle = -1.0 # Retroceder
```

---

## LED RGB (Neopixel)

La IdeaBoard tiene un LED de colores. Puedes encenderlo con diferentes colores usando `ib.pixel`.

Los colores se definen como una combinación de Rojo (R), Verde (G) y Azul (B), con valores entre 0 y 255.

Ejemplo:

```python
from ideaboard import IdeaBoard

ib = IdeaBoard()

ib.brightness = 0.2  # Ajusta la intensidad del brillo (0.0 a 1.0)

# Definir colores
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

ib.pixel = AZUL  # Enciende el LED en azul
```

### Efecto arcoiris

El efecto arcoiris permite mostrar colores de manera cíclica usando valores entre 0 y 255.

```python
from ideaboard import IdeaBoard
from time import sleep

ib = IdeaBoard()

while True:
    for i in range(256):
        ib.arcoiris = i
        sleep(0.01)
```

---

## Servomotores

Los servos permiten mover objetos a posiciones precisas. Se controlan usando el ángulo entre **0** y **180** grados.

Ejemplo:

```python
import board
from ideaboard import IdeaBoard
from time import sleep

ib = IdeaBoard()

servo1 = ib.Servo(board.IO4)

while True:
    servo1.angle = 10   # Mover a 10 grados
    sleep(2)
    servo1.angle = 170  # Mover a 170 grados
    sleep(2)
```

---

## Entradas digitales (Digital In)

Esto te permite **leer botones o sensores digitales** (encendido/apagado).

* `pull=ib.UP` o `pull=ib.DOWN` configuran resistencias internas para estabilizar la señal (opcional).
* `.value` devuelve el estado actual (True o False).

Ejemplo:

```python
import board
import time
from ideaboard import IdeaBoard

ib = IdeaBoard()

entrada = ib.DigitalIn(board.IO27)

while True:
    print(entrada.value)
    time.sleep(0.5)
```

---

## Salidas digitales (Digital Out)

Esto se usa para **encender o apagar dispositivos** como LEDs o relés.

* `.value = True` activa la salida
* `.value = False` apaga la salida

Ejemplo:

```python
import board
import time
from ideaboard import IdeaBoard

ib = IdeaBoard()

salida = ib.DigitalOut(board.IO27)

while True:
    salida.value = True   # Encender
    time.sleep(0.5)
    salida.value = False  # Apagar
    time.sleep(0.5)
```

---

## Entradas analógicas (Analog In)

Permite **leer sensores analógicos** como potenciómetros.

* `.value` devuelve un número de 0 a 65535 que representa la lectura del sensor.

Ejemplo:

```python
import board
import time
from ideaboard import IdeaBoard

ib = IdeaBoard()

entrada = ib.AnalogIn(board.IO33)

while True:
    print(entrada.value)
    time.sleep(0.5)
```

---

## Salidas analógicas (Analog Out)

Puedes **generar señales analógicas** (0 a 3.3V) para controlar dispositivos como luces LED suavemente.

> Solo los pines `board.IO25` y `board.IO26` permiten salida analógica.

Ejemplo:

```python
import time
import board
from ideaboard import IdeaBoard

ib = IdeaBoard()

dac = ib.AnalogOut(board.IO26)

dac.value = 32768  # Produce aproximadamente 1.60V en el pin IO26
```

---

## Función Map Range

Esta función ajusta valores de un rango a otro. Útil para convertir valores de sensores a rangos comprensibles, como mover un servo según un potenciómetro.

Ejemplo:

```python
import board
from ideaboard import IdeaBoard
from analogio import AnalogIn

ib = IdeaBoard()

pot = AnalogIn(board.IO33)
servo = ib.Servo(board.IO4)

while True:
    val = pot.value
    val = ib.map_range(val, 0, 65535, 0, 180)  # Convierte valor del potenciómetro a grados del servo
    servo.angle = val
```

---

## Notas finales

Esta guía está pensada para ayudarte a iniciar con **IdeaBoard** de manera sencilla.
Puedes combinar estas funciones para crear proyectos más complejos como robots, sistemas de luces inteligentes o control de sensores.

---

# Placa Sumobot + IdeaBoard

## Sensores infrarrojos

La placa de Sumobot cuenta con 4 sensores infrarojos en la parte inferior. Este es un código de ejemplo de como se pueden leer los datos de el sensor.  Se asume que los sensores 1 a 4, están conectados a los pines 36,39,34 y 35

```python
import board
from time import sleep
from ideaboard import IdeaBoard

ib = IdeaBoard()

sen1 = ib.AnalogIn(board.IO36)  # SENSOR 1 (adelante izquierdo) pin IO36
sen2 = ib.AnalogIn(board.IO39)  # SENSOR 2 (adelante derecho) pin IO39
sen3 = ib.AnalogIn(board.IO34)  # SENSOR 3 (atrás izquierdo) pin IO34
sen4 = ib.AnalogIn(board.IO35)  # SENSOR 4 (atrá derecho) pin IO35

infrarrojos = [sen1, sen2, sen3, sen4]

while True: 
    for i, sen in enumerate(infrarrojos, start=1):
        print(f"SENSOR {i}: {sen.value}")
    
    print("_________")
    
    sleep(0.5)
```

Los detalles de conexión de la placa, los puede encontrar en [esta guia](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/Guia%20de%20Conexiones%20Sumobot.pdf)

## Acelerómetro y Giroscopio 

La placa del Sumobot, cuenta con un acelerómetro y giroscopio, que se conecta a través de una una conexión Qwiic que requiere un cable especial que se entrega con el Kit de Sumobot. Detalles de las conexiones las puede ver en  [esta guia](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/Guia%20de%20Conexiones%20Sumobot.pdf)

Este código simplificado muestra lo siguiente que:

- Inicializa el acelerómetro y giroscopio LSM6DS3TRC
- Lee datos del acelerómetro y del giroscopio
- Muestra las lecturas en consola
- Explica paso a paso cómo usar cada parte

```python
# Ejemplo básico para leer acelerómetro y giroscopio con el sensor LSM6DS3TRC

import board
import time
import math
from adafruit_lsm6ds import Rate, AccelRange, GyroRange
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

# Inicializamos el bus I2C del microcontrolador
i2c = board.I2C()

# Inicializamos el sensor LSM6DS3TRC en la dirección I2C por defecto (0x6B)
sensor = LSM6DS3TRC(i2c, 0x6B)

# Configuramos la sensibilidad del acelerómetro y giroscopio
sensor.accelerometer_range = AccelRange.RANGE_8G  # Hasta ±8G para aceleraciones fuertes
sensor.gyro_range = GyroRange.RANGE_2000_DPS      # Hasta ±2000 grados por segundo para giros rápidos
sensor.accelerometer_data_rate = Rate.RATE_104_HZ # 104 lecturas por segundo
sensor.gyro_data_rate = Rate.RATE_104_HZ          # Igual que acelerómetro para sincronizar

# Función para convertir radianes a grados (opcional, útil para giroscopio)
def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)

print("Iniciando lectura de acelerómetro y giroscopio...")

# Bucle principal
while True:
    # Leer aceleración (X, Y, Z) en metros por segundo cuadrado (m/s²)
    accel_x, accel_y, accel_z = sensor.acceleration
    print(f"Acelerómetro -> X: {accel_x:.2f} m/s², Y: {accel_y:.2f} m/s², Z: {accel_z:.2f} m/s²")
    
    # Leer velocidad angular (X, Y, Z) en radianes por segundo (rad/s)
    gyro_x, gyro_y, gyro_z = sensor.gyro
    print(f"Giroscopio -> X: {radianes_a_grados(gyro_x):.2f} °/s, Y: {radianes_a_grados(gyro_y):.2f} °/s, Z: {radianes_a_grados(gyro_z):.2f} °/s")
    
    print("-----------------------------------------")
    
    # Esperar un poco antes de la siguiente lectura
    time.sleep(0.5)
```

### Explicación del código

**1. Importar librerías**
Se usan `board` para acceder al bus I2C, `time` para esperar entre lecturas y `math` para conversiones. La librería `adafruit_lsm6ds` se usa para controlar el sensor.

**2. Inicializar el sensor**
Se crea una instancia del sensor en la dirección I2C estándar `0x6B`.
Si el sensor está conectado correctamente, comenzará a responder.

**3. Configurar rangos y tasas de datos**
Se ajustan los rangos de acelerómetro y giroscopio para que tengan buena sensibilidad y se evita ruido excesivo.

**4. Leer datos**
En cada ciclo se leen las aceleraciones en X, Y, Z y las velocidades angulares.
Las velocidades angulares se convierten de radianes/segundo a grados/segundo para que sean más fáciles de interpretar.

**5. Mostrar los datos**
Se imprimen en la consola cada medio segundo.


