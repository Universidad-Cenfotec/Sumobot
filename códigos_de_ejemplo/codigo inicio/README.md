# Código de Combate

Este código (`code.py`) es un buen punto de partida para el Sumobot. Permite entender la mayoría de funcionalidades, y cambiando parámetros o combinaciones de funciones, permite tener diferentes estrategias de combate.


# 1. Encabezado e importaciones

```python
import board
import keypad
from ideaboard import IdeaBoard
from time import sleep
from hcsr04 import HCSR04
import random
```

## Qué hace esta sección

Aquí se cargan las librerías que el programa necesita para funcionar.

## Para qué sirve cada una

### `import board`

Permite usar los pines físicos del microcontrolador con nombres como:

* `board.IO0`
* `board.IO25`
* `board.IO26`
* `board.IO36`

Es la forma de decirle al código en qué pin está conectado cada sensor o botón.

---

### `import keypad`

Se usa para leer botones de manera más cómoda.
En este caso sirve para detectar el botón **BOOT** del IdeaBoard.

---

### `from ideaboard import IdeaBoard`

Carga la clase `IdeaBoard`, que simplifica mucho el control del robot.

Con esta librería puedes usar cosas como:

* `ib.motor_1.throttle`
* `ib.motor_2.throttle`
* `ib.pixel`
* `ib.AnalogIn(...)`

O sea, te facilita manejar motores, LED y entradas analógicas.

---

### `from time import sleep`

Permite pausar el programa por cierto tiempo.

Ejemplo:

```python
sleep(0.3)
```

Eso detiene el código por 0.3 segundos.

---

### `from hcsr04 import HCSR04`

Sirve para manejar el sensor ultrasónico HC-SR04.

Con eso puedes medir distancia al frente.

---

### `import random`

Se usa para escoger direcciones al azar, por ejemplo al girar izquierda o derecha en una maniobra evasiva.

---

# 2. Creación de objetos principales

```python
sonar = HCSR04(board.IO25, board.IO26)
ib = IdeaBoard()
keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)
```

## `sonar = HCSR04(board.IO25, board.IO26)`

Aquí creas el objeto del sensor ultrasónico.

* `IO25` y `IO26` son los pines conectados al sensor.
* Luego puedes usar:

  ```python
  sonar.dist_cm()
  ```

  para obtener la distancia en centímetros.

---

## `ib = IdeaBoard()`

Aquí creas el objeto principal del robot.

Ese objeto `ib` controla:

* motores
* LED RGB
* entradas analógicas
* otras utilidades de la placa

---

## `keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)`

Esta línea configura el botón BOOT.

### Qué significa cada parte

* `board.IO0`: el botón está conectado a ese pin.
* `(board.IO0,)`: se pasa como tupla, aunque solo haya un botón.
* `value_when_pressed=False`: cuando el botón se presiona, el valor lógico será `False`.
* `pull=True`: activa una resistencia pull-up interna.

## Idea importante

Este botón se usará para que el robot **espere antes de comenzar**.

---

# 3. Configuración de sensores infrarrojos

```python
sen1 = ib.AnalogIn(board.IO36)
sen2 = ib.AnalogIn(board.IO39)
sen3 = ib.AnalogIn(board.IO34)
sen4 = ib.AnalogIn(board.IO35)

infrarrojos = [sen1, sen2, sen3, sen4]
```

## Qué hace esta sección

Configura los 4 sensores infrarrojos que detectan el borde blanco del dojo.

## Distribución

* `sen1`: adelante izquierdo
* `sen2`: adelante derecho
* `sen3`: atrás izquierdo
* `sen4`: atrás derecho

## Por qué se guardan en una lista

La lista `infrarrojos` permite recorrer los sensores fácilmente con un `for` en lugar de tratarlos uno por uno.

Eso facilita funciones como:

```python
leer_sensores(infrarrojos)
```

---

# 4. Conversión de bits a entero

```python
def arreglo_a_entero(bits):
    valor = 0
    for bit in bits:
        valor = (valor << 1) | bit
    return valor
```

## Qué hace

Convierte una lista de bits en un número entero.

Por ejemplo, si `bits = [1, 0, 1, 1]`, el resultado será:

* empieza en 0
* desplaza a la izquierda y agrega cada bit
* termina en `11` en decimal

## Para qué sirve en este robot

Los sensores infrarrojos devuelven una lista como:

```python
[0, 1, 0, 0]
```

Eso representa qué sensores detectan línea o no.
Con esta función se convierte esa combinación en un único número, para tomar decisiones más fácil.

---

# 5. Lectura de sensores infrarrojos

```python
def leer_sensores(infrarrojos, valor_critico=10000):
    return [int(sen.value < valor_critico) for sen in infrarrojos]
```

## Qué hace

Lee cada sensor infrarrojo y lo convierte a:

* `1` si detecta negro
* `0` si detecta blanco

según el umbral `valor_critico`.

## Cómo funciona

Cada sensor analógico da un valor numérico.
El código compara ese valor contra `valor_critico`.

```python
sen.value < valor_critico
```

Si se cumple, devuelve `True`, y `int(True)` es `1`.
Si no, devuelve `False`, y `int(False)` es `0`.

## Resultado típico

Puede devolver algo como:

```python
[0, 0, 1, 0]
```

---

# 6. Función `on_white`

```python
def on_white(infrarrojos, valor_critico=10000):
    sensores = leer_sensores(infrarrojos, valor_critico)
    return arreglo_a_entero(sensores) > 0
```

## Qué pretende hacer

Lee los sensores y devuelve `True` si alguno detecta una condición especial.

## Ojo con el nombre

El nombre `on_white` puede confundir un poco, porque internamente depende de cómo interpretaste los valores de los sensores.

Como en tu función:

```python
int(sen.value < valor_critico)
```

el `1` representa una condición específica, entonces `on_white()` realmente depende de cómo calibraste ese umbral.
En este código no se usa después, pero parece pensada para preguntar si algún sensor detecta borde.

---

# 7. Función `line_status`

```python
def line_status(infrarrojos, valor_critico=10000):
    sensores = leer_sensores(infrarrojos, valor_critico)
    return arreglo_a_entero(sensores)
```

## Qué hace

Devuelve un número entero que representa el estado de los 4 sensores.

## Ejemplo

Si los sensores leen:

```python
[0, 0, 0, 0]
```

entonces retorna `0`.

Si leen:

```python
[0, 0, 1, 0]
```

retorna otro valor entero distinto.

## Para qué sirve

Te permite tomar decisiones según cuál sensor detectó línea.

Por ejemplo:

* `0`: ningún sensor detecta borde
* `1,2,3`: ciertos sensores traseros detectan línea
* otros valores: podría haber sensores delanteros detectando línea

Esa lógica la usas en `forwardCheck()`.

---

# 8. Funciones de movimiento

Estas funciones controlan los motores.

---

## `forward(t, speed)`

```python
def forward(t, speed):
    ib.pixel = (0, 255, 0)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = speed
    sleep(t)
```

### Qué hace

Mueve el robot hacia adelante durante `t` segundos con velocidad `speed`.

### Detalles

* enciende el LED en verde
* ambos motores van hacia adelante
* espera `t` segundos

---

## `backward(t, speed)`

```python
def backward(t, speed):
    ib.pixel = (150, 255, 0)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = -speed
    sleep(t)
```

### Qué hace

Mueve el robot hacia atrás.

### Detalle importante

`throttle` negativo significa reversa.

---

## `left(t, speed)`

```python
def left(t, speed):
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = -speed
    ib.motor_2.throttle = speed
    sleep(t)
```

### Qué hace

Hace girar el robot a la izquierda.

### Cómo lo logra

* un motor gira hacia atrás
* el otro hacia adelante

Eso produce una rotación sobre su eje.

---

## `right(t, speed)`

```python
def right(t, speed):
    ib.pixel = (50, 55, 100)
    ib.motor_1.throttle = speed
    ib.motor_2.throttle = -speed
    sleep(t)
```

Hace lo contrario: gira a la derecha.

---

## `stop()`

```python
def stop():
    ib.pixel = (0, 0, 0)
    ib.motor_1.throttle = 0
    ib.motor_2.throttle = 0
```

### Qué hace

Detiene completamente el robot.

### Importancia

Es clave para:

* frenar antes de medir con ultrasonido
* detenerse antes de cambiar de maniobra
* evitar movimientos no deseados

---

# 9. Función `randomTurn`

```python
def randomTurn(t, speed):
    dir = random.choice([-1, 1])
    ib.pixel = (255, 0, 0)
    ib.motor_1.throttle = dir * -speed
    ib.motor_2.throttle = dir * speed
    sleep(t)
```

## Qué hace

Escoge aleatoriamente entre girar izquierda o derecha.

## Cómo funciona

`random.choice([-1, 1])` elige:

* `-1`
* o `1`

Eso cambia el signo en la velocidad de los motores y provoca giro a un lado u otro.

## Para qué sirve

Después de detectar peligro de salir del dojo, el robot puede retroceder y luego girar en una dirección aleatoria para reubicarse.

Eso evita que siempre haga la misma maniobra.

---

# 10. Función `lookForward`

```python
def lookForward():
    stop()
    dist = sonar.dist_cm()
    sleep(0.2)
    return dist
```

## Qué hace

Mide la distancia al frente con el ultrasónico.

## Paso por paso

1. Detiene el robot.
2. Lee la distancia con:

   ```python
   sonar.dist_cm()
   ```
3. Espera un poco.
4. Retorna la distancia.

## Por qué primero hace `stop()`

Porque si el robot está vibrando o moviéndose, la medición puede ser menos estable.

---

# 11. Función `scan`

```python
def scan():
    stop()
    maxCount = 10
    count = 0
    dist = lookForward()
    while count < maxCount and (dist > 30 or dist == -1):
        left(0.2, 0.2)
        count += 1
        dist = lookForward()
    stop()
    if count == maxCount:
        return False
    else:
        return True
```

## Qué hace

Busca un oponente girando poco a poco hacia la izquierda.

## Lógica

* empieza detenido
* mide al frente
* mientras no vea nada cercano:

  * gira un poco
  * vuelve a medir
* si encuentra algo antes de llegar al máximo de intentos, retorna `True`
* si no encuentra nada, retorna `False`

## Condición de búsqueda

```python
(dist > 30 or dist == -1)
```

Significa:

* si el objeto está a más de 30 cm, todavía no está cerca
* si el sensor devuelve `-1`, no detectó nada útil

## Observación

En tu código principal esta función no se está usando todavía, pero es una buena base para una estrategia de búsqueda.

---

# 12. Función `wiggle`

```python
def wiggle(t, n, speed):
    for i in range(n):
        ...
```

## Qué hace

Hace que el robot se mueva alternando izquierda y derecha varias veces.

## Para qué puede servir

* desatascarse
* buscar al oponente
* generar movimiento agresivo
* ajustar orientación

## Cómo funciona

Dentro del `for`, el robot:

* gira a un lado
* gira al otro
* se detiene
* vuelve a girar

Es una oscilación.

---

# 13. Función `wiggle_forward`

```python
def wiggle_forward(t, n, speed):
    for i in range(n):
        ...
        forward(0.3, 1)
        ...
```

## Qué hace

Es parecida a `wiggle`, pero incluye un avance hacia adelante.

## Para qué sirve

Tu comentario lo sugiere bien: cuando detecta línea atrás, el robot puede aprovechar y lanzarse hacia adelante con fuerza, porque atrás está en riesgo pero al frente todavía puede avanzar para mantenerse en combate.

## Idea estratégica

Si los sensores traseros ven blanco, la mejor respuesta no siempre es retroceder.
A veces conviene **avanzar fuerte** para no salir por atrás.

---

# 14. Función `forwardCheck`

```python
def forwardCheck(t, speed, th):
    d = int(t / 0.01)
    for i in range(d):
        status = line_status(infrarrojos, th)
        print(status)
        if status == 0:
            forward(0.1, speed)
        elif status >= 1 and status <= 3:
            wiggle_forward(0.1, 4, 1)
        else:
            stop()
            sleep(0.3)
            backward(1, 0.3)
            randomTurn(1, 0.3)
```

## Esta es una de las funciones más importantes

Hace que el robot avance, **pero vigilando constantemente los sensores IR** para no salirse del dojo.

---

## Paso 1: dividir el tiempo

```python
d = int(t / 0.01)
```

Divide el tiempo `t` en pequeños pasos.

La idea es no avanzar "a ciegas" durante todo el tiempo, sino revisar los sensores frecuentemente.

---

## Paso 2: revisar sensores en cada iteración

```python
status = line_status(infrarrojos, th)
print(status)
```

Lee el patrón de sensores y lo imprime para depuración.

---

## Caso 1: `status == 0`

```python
if status == 0:
    forward(0.1, speed)
```

Significa que no se detecta línea peligrosa.
Entonces avanza.

---

## Caso 2: `status >= 1 and status <= 3`

```python
elif status >= 1 and status <= 3:
    wiggle_forward(0.1, 4, 1)
```

Según tu lógica, esto representa que se detectó línea atrás.

Entonces el robot hace una maniobra agresiva hacia adelante.

---

## Caso 3: cualquier otro caso

```python
else:
    stop()
    sleep(0.3)
    backward(1, 0.3)
    randomTurn(1, 0.3)
```

Aquí el robot interpreta una situación de riesgo más seria, posiblemente línea al frente o combinación peligrosa.

Entonces:

1. se detiene
2. espera un poco
3. retrocede
4. gira aleatoriamente

Esto busca sacarlo de la zona de peligro.

---

# 15. Función `esperar_boton`

```python
def esperar_boton():
    print("Esperando botón...")
    ib.pixel = (255, 100, 0)

    while True:
        event = keys.events.get()
        if event and event.released:
            print("Botón soltado. Iniciando...")
            ib.pixel = (0, 255, 0)
            sleep(0.2)
            ib.pixel = (0, 0, 0)
            return
```

## Qué hace

Esta función detiene el inicio del robot hasta que el botón BOOT sea:

1. presionado
2. y luego soltado

## Cómo funciona

### `keys.events.get()`

Busca un evento del botón.

Puede ser:

* presionado
* soltado
* o ninguno

### `if event and event.released:`

Solo actúa cuando detecta que el botón fue soltado.

## Por qué usar `released` y no `pressed`

Porque así el robot no arranca justo cuando lo estás tocando, sino cuando ya lo liberaste.

Eso es útil en competencia: puedes tenerlo listo y soltarlo exactamente cuando quieres iniciar.

## `return`

Cuando detecta la liberación, sale de la función y el programa continúa normalmente.

---

# 16. Variable de umbral

```python
th = 2950
```

## Qué hace

Define el umbral para los sensores infrarrojos.

Ese número separa dos condiciones:

* superficie oscura
* línea blanca

## Importancia

Este valor casi siempre necesita calibración real en tu robot, con tus sensores y tu dojo.

Si está mal calibrado:

* puede creer que está sobre blanco cuando no lo está
* o no detectar la línea a tiempo

---

# 17. Inicio del programa antes del bucle principal

```python
stop()
esperar_boton()
```

## Qué hace

Antes de arrancar:

1. detiene motores por seguridad
2. espera el botón

## Resultado

El robot queda quieto al encenderse y **solo empieza cuando sueltas el botón**.

---

# 18. Bucle principal

```python
while True:
    distancia = sonar.dist_cm()
    if distancia > -1 and distancia < 30:
        right(0.1, 0.2)
        forwardCheck(0.2, 1, th)
        stop()
        sleep(0.3)
    else:
        stop()
        sleep(0.3)
        right(0.1, 0.2)
    stop()
```

## Esta sección es la estrategia principal del robot

Se repite indefinidamente.

---

## Paso 1: medir distancia

```python
distancia = sonar.dist_cm()
```

El ultrasónico revisa si hay un objeto al frente.

---

## Caso 1: detecta algo cerca

```python
if distancia > -1 and distancia < 30:
```

Significa:

* la medición es válida (`> -1`)
* hay algo a menos de 30 cm

Probablemente un oponente.

### Entonces hace:

```python
right(0.1, 0.2)
forwardCheck(0.2, 1, th)
stop()
sleep(0.3)
```

#### `right(0.1, 0.2)`

Hace un pequeño ajuste a la derecha.

#### `forwardCheck(0.2, 1, th)`

Avanza agresivamente, pero cuidando no salirse del dojo.

#### `stop()` y `sleep(0.3)`

Se detiene un momento antes de volver a decidir.

---

## Caso 2: no detecta nada

```python
else:
    stop()
    sleep(0.3)
    right(0.1, 0.2)
```

Si no hay oponente cerca:

* se detiene
* espera
* gira un poco a la derecha

## Interpretación estratégica

Está buscando oponente girando poco a poco.

---

## `stop()` final

```python
stop()
```

Asegura que al terminar cada iteración no queden motores encendidos accidentalmente.

---

# 19. Resumen global de la estrategia

Tu robot hace esto:

1. se enciende
2. queda esperando el botón
3. cuando sueltas el botón, arranca
4. mide con ultrasónico
5. si detecta rival cerca:

   * ajusta dirección
   * avanza controlando línea
6. si no detecta rival:

   * gira para buscarlo
7. si detecta borde con IR:

   * reacciona según la posición del peligro

---

# 20. Fortalezas del código

Este código tiene varias cosas buenas:

* separa el movimiento en funciones claras
* usa el ultrasónico para buscar rival
* usa infrarrojos para no salirse
* agrega inicio con botón
* tiene maniobras de recuperación
* la lógica está modularizada

---

# 21. Cosas que podrías mejorar después

Hay varios puntos mejorables:

## A. `forwardCheck()` no revisa cada 0.01 s realmente

Aunque calculas:

```python
d = int(t / 0.01)
```

adentro llamas `forward(0.1, speed)`, que ya duerme 0.1 segundos.
Entonces la revisión no es tan rápida como parece.

---

## B. El robot gira casi siempre a la derecha

En el ciclo principal, si detecta o no detecta rival, igual hay bastante tendencia a girar a la derecha.

Podría volverse predecible.

---

## C. `scan()` está definida pero no se usa

Podrías integrarla para hacer una búsqueda más inteligente.

---

## D. El nombre `on_white()` puede ser confuso

Sería bueno renombrarla según la lógica real del sensor.

---

## E. Hay muchos `sleep()`

Eso simplifica el código, pero hace que el robot sea menos reactivo.

---

# 22. Idea conceptual del programa

En una frase:

**Este código implementa un Sumobot que espera una señal de inicio con el botón BOOT, busca oponentes con ultrasonido y evita salir del dojo usando 4 sensores infrarrojos.**
