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
