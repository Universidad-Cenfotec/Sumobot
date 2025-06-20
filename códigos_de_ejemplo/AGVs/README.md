# Introducción a los AGV y al código de navegación con Sumobot

Tomás de Camino Beck, Ph.D.  
Universidad CENFOTEC  

![agv1](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/AGVs/Sumobot%20AGV1.png)

## ¿Qué es un AGV?

Un **AGV** (*Automated Guided Vehicle*) es un vehículo autónomo que se mueve por un entorno utilizando alguna forma de guía externa, como:

* Líneas en el suelo (pintadas o magnéticas),
* Sensores ópticos o infrarrojos,
* Balizas láser, GPS, o visión artificial.

Estos sistemas son comunes en fábricas, almacenes y laboratorios educativos, donde permiten transporte automatizado y navegación precisa sin intervención humana.

---

## Saberes que cubre este proyecto de Sumobot

Este proyecto de **Sumobot que se mueve sobre una cuadrícula** cubre los siguientes saberes clave:

* **Electrónica básica**: sensores IR, motores DC, LED RGB.
* **Programación en CircuitPython**: definición de funciones, bucles, estructuras de decisión.
* **Control de movimiento**: velocidad, giro, avance, retroceso.
* **Interpretación de sensores**: lectura binaria según umbrales.
* **Uso de giroscopio**: integración de velocidad angular para medir ángulos.
* **Estrategias de navegación**: detección de intersecciones, seguimiento de líneas.
* **Abstracción funcional**: comandos simplificados y ejecución dinámica.

---

## Explicación por partes del código

El código [`code_grid.py`](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/AGVs/code_grid.py) permite al sumobot seguir lineas negras y detenerse en intersecciones, girar, para mantenerse navegando en una cuadrñicula de líneas negras.

![agv](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/AGVs/Sumobot%20AGV4.JPG)

### 1. Funciones de utilidad

```python
def leer_sensores(sensores, umbral=10000):
```

* Lee el valor de cada sensor IR.
* Devuelve una lista binaria indicando si detecta línea negra (valor menor al umbral).

```python
def stop():
```

* Detiene ambos motores y apaga el LED RGB.

```python
def execute(commandlist: list, commands: dict):
```

* Ejecuta una lista de comandos (en forma de texto) mapeados a funciones.
* Permite diseñar secuencias de navegación dinámicas como `["F", "L", "F"]`.

```python
def str_to_list(secuencia: str) -> list:
```

* Convierte un string como `"F,L,R"` en `["F", "L", "R"]`.

---

#### ⚙️ 2. Movimientos básicos

```python
def forward(t, speed)
def backward(t, speed)
def left(t, speed)
def right(t, speed)
```

* Controlan el movimiento de los motores para avanzar, retroceder o girar.
* Usan LED RGB para indicar el estado (verde, amarillo, etc).

---

### 3. Control con giroscopio

```python
def calibrar_drift(sensor, segundos=2)
```

* Mide el sesgo (drift) del eje Z del giroscopio para compensarlo al girar.

```python
def girar_grados(sensor, grados, drift, velocidad=0.25)
```

* Gira el robot una cantidad específica de grados.
* Integra la velocidad angular del giroscopio para medir cuánto ha rotado.

---

### 4. Seguimiento de línea con parada

```python
def forward_line_stop(th=2950, speed=0.5, corr=0.1)
```

* Sigue la línea usando sensores delanteros.
* Se detiene cuando ambos sensores traseros detectan fondo blanco (intersección).
* Usa lógica de corrección para girar ligeramente si el robot se desvía.

---

### 5. Funciones de envoltura ("wrappers")

```python
def f(): forward_line_stop(...)
def l(): girar_grados(..., -90, ...)
def r(): girar_grados(..., 90, ...)
```

* Simplifican la ejecución de comandos al ser llamadas desde `execute()`.

---

## Programa principal

1. **Calibración**

```python
drift = calibrar_drift(sensor, 5)
```

* Mide y guarda el "drift" del giroscopio.

2. **Parámetros de navegación**

```python
th = 2950       # Umbral para sensores IR
speed = 0.3     # Velocidad base
corr = 0.1      # Corrección para giros leves
```

3. **Diccionario de comandos**

```python
comandos = {
    "F": f,
    "L": l,
    "R": r
}
```

4. **Bucle principal**

```python
while True:
    com = str_to_list("F,L")
    execute(com, comandos)
```

* Ejecuta la secuencia: avanzar hasta la siguiente intersección (`F`), girar a la izquierda (`L`).
* Este ciclo se repite indefinidamente, moviéndose de intersección en intersección.

---

Este proyecto enseña cómo un **robot puede tomar decisiones de movimiento** usando sensores e información de orientación. La abstracción por comandos, el uso del giroscopio y el seguimiento de líneas permiten implementar **algoritmos básicos de navegación autónoma en entornos estructurados**, lo que es una excelente introducción práctica al mundo de los AGVs.
