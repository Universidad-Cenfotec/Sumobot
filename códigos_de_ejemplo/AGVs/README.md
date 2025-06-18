# Introducción a los AGV y al código de navegación con Sumobot

Tomás de Camino Beck, Ph.D.  
Universidad CENFOTEC  

![agv1](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/AGVs/Sumobot%20AGV1.png)


## ¿Qué es un AGV?

Un **AGV** (Automated Guided Vehicle o Vehículo de Guiado Automático) es un robot móvil diseñado para moverse de manera autónoma por un espacio físico siguiendo una guía externa. Esta guía puede ser una **línea negra**, un **cable enterrado**, un **patrón magnético** o una **ruta programada**. Los AGV se utilizan comúnmente en fábricas, almacenes o laboratorios para transportar objetos o recorrer rutas definidas sin intervención humana.

En este proyecto, el robot **Sumobot de CENFOTEC** simula un AGV sencillo que se mueve sobre una **cuadrícula de líneas negras** trazadas en el suelo. Para hacerlo, utiliza sensores infrarrojos para detectar las líneas y un giroscopio que le permite girar con precisión en las intersecciones.

---

## ¿Qué hace este código?

El código [`code_grid.py`](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/AGVs/code_grid.py) permite que un **Sumobot navegue por una cuadrícula negra**:

- **Sigue una línea negra** utilizando sensores infrarrojos delanteros.
- **Detecta intersecciones** con sensores traseros.
- **Se detiene en cada intersección**.
- **Gira 90 grados** utilizando un giroscopio, manteniéndose en el centro de la intersección.
- **Repite una secuencia de movimientos** definida en el loop principal.

![agv2](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/AGVs/Sumobot%20AGV4.JPG)

---

## Explicación paso a paso del código

### 1. Inicialización del hardware

```python
ib = IdeaBoard()
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, address=0x6B)
````

Se crea una instancia de la placa `IdeaBoard`, se inicializa el bus I2C y se conecta el sensor giroscópico `LSM6DS3TRC`.

También se definen los sensores infrarrojos (IR):

```python
sen1 = ib.AnalogIn(board.IO36)  # Delantero izquierdo
sen2 = ib.AnalogIn(board.IO39)  # Delantero derecho
sen3 = ib.AnalogIn(board.IO34)  # Trasero izquierdo
sen4 = ib.AnalogIn(board.IO35)  # Trasero derecho
```

---

### 2. Lectura de sensores infrarrojos

```python
def leer_sensores(sensores, umbral=10000):
    return [int(sensor.value < umbral) for sensor in sensores]
```

Convierte las lecturas analógicas de los sensores IR en valores binarios:

* `1` si el sensor detecta una línea negra (valor bajo).
* `0` si detecta fondo blanco (valor alto).

---

### 3. Funciones de movimiento

Funciones básicas para moverse hacia adelante, atrás o girar:

```python
def forward(t, speed):
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    time.sleep(t)
    stop()
```

Funciones similares existen para `backward`, `left` y `right`, simplemente ajustando el sentido de los motores.

---

### 4. Control de giro con giroscopio

#### Calibración del drift:

```python
def calibrar_drift(sensor, segundos=2):
    ...
    drift = suma / muestras
    return drift
```

Calcula un promedio del movimiento natural (drift) del giroscopio en reposo para mejorar la precisión del giro.

#### Giro controlado:

```python
def girar_grados(sensor, grados, drift, velocidad=0.25):
    ...
    while acumulado < grados:
        vel_angular = sensor.gyro[2] - drift
        ...
```

Esta función gira el robot exactamente una cantidad determinada de grados (por ejemplo, 90°), usando el giroscopio para medir la rotación acumulada.

---

### 5. Movimiento recto con corrección PDI

```python
def straight_move(velocidad, duracion, drift, Kp=0.15, Ki=0.8, Kd=0.05):
    ...
```

Mantiene el robot moviéndose en línea recta usando un **controlador PDI** que corrige desviaciones detectadas por el giroscopio. Esta función no se utiliza directamente en el código, pero se deja allí para posibilidar funcionalidades de mayor precisión

---

### 6. Seguidor de línea con parada en intersección

```python
def forward_line_stop(th=2950, speed=0.5, corr=0.1):
    ...
    front = leer_sensores([sen1, sen2], th)
    back = leer_sensores([sen3, sen4], th)

    if tras_izq == 0 and tras_der == 0:
        forward(0.15, speed)
        stop()
        return
```

Esta es la función principal de navegación:

* El robot avanza mientras los sensores delanteros detecten línea negra.
* Si pierde alineación, corrige el rumbo ajustando los motores.
* Si los sensores traseros **no detectan línea** (es decir, detectan blanco), el robot ha llegado a una intersección y se detiene.

---

### 7. Funciones simplificadas para el loop principal

```python
def f():
    forward_line_stop(th, speed, corr)

def l():
    girar_grados(sensor, -90, drift)

def r():
    girar_grados(sensor, 90, drift)
```

Estas funciones se utilizan en el programa principal para definir una secuencia de navegación legible.

---

### 8. Programa principal

```python
drift = calibrar_drift(sensor, 5)
th = 2950
speed = 0.3
corr = 0.1

while True:
    f()
    f()
    l()
```

El programa:

* Calibra el giroscopio.
* Avanza dos intersecciones.
* Gira a la izquierda.
* Repite indefinidamente.

---

## Conclusión: aprendizajes al trabajar con este código

Este proyecto permite a los estudiantes:

* **Comprender cómo funciona un AGV** y cómo puede orientarse por guías físicas.
* **Aplicar sensores infrarrojos** para interpretar el entorno físico.
* **Utilizar un giroscopio** para movimientos precisos en un entorno estructurado.
* **Aplicar controladores como el PDI** para estabilizar el movimiento.
* **Desarrollar pensamiento lógico y estructurado** a través de programación por funciones y condicionales.
* **Explorar conceptos de robótica móvil**, navegación autónoma y sistemas embebidos, de forma práctica y tangible.

Este tipo de actividades refuerza tanto el aprendizaje técnico como el pensamiento computacional en jóvenes interesados en ciencia y tecnología.
