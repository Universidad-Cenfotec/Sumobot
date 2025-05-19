# Almacenando Datos en el Sumobot

Tomás de Camino Beck, Ph.D  
Universidad CENFOTEC

**Introducción**

Este documento describe el funcionamiento del programa [`code_storage.py`](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/code_storage.py), un ejemplo práctico diseñado para enseñar a estudiantes de colegio cómo **registrar y almacenar datos de sensores en un robot** utilizando un microcontrolador con ESP32.

El objetivo principal de este código es que los estudiantes aprendan a **medir información del entorno** (como la distancia a un objeto usando un sensor ultrasónico) y a **guardar esos datos en un archivo** dentro del robot. Esta técnica es fundamental para:

* **Analizar patrones de movimiento.**
* **Estudiar el entorno del robot.**
* **Diseñar estrategias y planificar comportamientos autónomos.**

El sensor ultrasónico mide la distancia a un objeto, y el programa guarda estas mediciones repetidamente en un archivo llamado `datos.csv`. Esta recopilación de datos puede luego ser descargada y analizada con herramientas como Excel o Python, permitiendo a los estudiantes observar cómo se comporta el robot y cómo reacciona a su entorno.

El código está pensado como punto de partida para desarrollar ideas más avanzadas, como navegación inteligente, reconocimiento de obstáculos o toma de decisiones basada en datos reales. Los estudiantes pueden modificarlo para registrar otras variables, como velocidad, giros o estados internos del robot.

---

## ¿Qué hace este código?

Este código permite que un **robot con un ESP32 y un sensor ultrasónico** mida distancias y guarde esos datos en un archivo llamado `datos.csv`. De esta forma, el robot puede “recordar” lo que midió para que después un humano analice esa información.

Es como si el robot llevara un cuaderno de apuntes y escribiera en él la distancia que ve hacia adelante, una y otra vez.

---

## Explicación paso a paso

### 1. **Importación de librerías**

```python
import board
import time
import os
from ideaboard import IdeaBoard
```

Estas líneas cargan funciones necesarias para usar el hardware:

* `board`: para acceder a los pines del ESP32.
* `time`: para usar pausas (como `sleep()`).
* `os`: para manipular archivos.
* `IdeaBoard`: es la clase que permite controlar sensores y motores conectados a la placa.

---

### 2. **Inicializar la placa y abrir el archivo**

```python
ib = IdeaBoard()
file = open("/datos.csv", "w")
file.write("tiempo,distancia\n")
```

* Se crea una conexión con la **IdeaBoard**.
* Se abre (o crea) un archivo `datos.csv` para escribir los datos.
* Se escribe la primera línea del archivo, que es el **encabezado**: `"tiempo,distancia"` (esto es útil si después se analiza con Excel o Google Sheets).

---

### 3. **Bucle principal**

```python
for i in range(100):
    distancia = ib.ultrasonic()
    tiempo_actual = time.monotonic()
    file.write(f"{tiempo_actual},{distancia}\n")
    print(f"Distancia: {distancia} cm")
    time.sleep(0.1)
```

Esto se repite 100 veces:

* `ib.ultrasonic()` mide la distancia con el sensor ultrasónico (en centímetros).
* `time.monotonic()` obtiene el tiempo en segundos desde que el código empezó a correr.
* `file.write(...)` guarda el tiempo y la distancia en el archivo, separados por una coma.
* `print(...)` muestra la distancia en la consola (opcional para monitorear).
* `time.sleep(0.1)` espera 0.1 segundos (100 milisegundos) antes de volver a medir.

**Así el robot mide 100 veces durante 10 segundos aproximadamente.**

---

### 4. **Cerrar el archivo**

```python
file.close()
```

Esto es muy importante. Cierra el archivo para que todos los datos se guarden correctamente.

---

## ¿Y luego qué se hace con `datos.csv`?

Este archivo se puede descargar desde el robot a una computadora y abrir con herramientas como:

* **Excel** o **Google Sheets** → Para hacer gráficos de distancia vs tiempo.
* **Python** con pandas y matplotlib → Para hacer análisis más avanzados.

---

## ¿Para qué sirve esto en robótica?

* Observar cómo varía la distancia cuando el robot se mueve.
* Detectar patrones (por ejemplo: “cada 3 segundos hay un obstáculo”).
* Ver cómo responde el sensor a diferentes objetos o ambientes.
* Planificar rutas más eficientes o programar reacciones automáticas.

---

## Resumen visual

| Parte del código   | ¿Qué hace?                                 |
| ------------------ | ------------------------------------------ |
| `ib.ultrasonic()`  | Mide la distancia al frente                |
| `time.monotonic()` | Registra cuánto tiempo ha pasado           |
| `file.write(...)`  | Guarda tiempo y distancia en un archivo    |
| `file.close()`     | Finaliza y asegura el guardado del archivo |
