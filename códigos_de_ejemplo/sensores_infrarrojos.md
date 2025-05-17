### Explicación del Código: Lectura de 4 Sensores en un Sumobot

Código Ejemplo de lectura de 4 sensores IR:
```python
# Tomás de Camino Beck
# Universidad Cenfotec

# Importa los módulos necesarios
import board               # Permite acceder a los pines de entrada/salida del microcontrolador
from time import sleep     # Permite usar la función sleep para pausar el programa
from ideaboard import IdeaBoard   # Importa la clase IdeaBoard para controlar los sensores y actuadores

# Crea una instancia de la IdeaBoard para controlar el hardware conectado
ib = IdeaBoard()

# Configura los pines analógicos donde están conectados los sensores infrarrojos
sen1 = ib.AnalogIn(board.IO36)  # SENSOR 1 (adelante izquierdo) pin IO36
sen2 = ib.AnalogIn(board.IO39)  # SENSOR 2 (adelante derecho) pin IO39
sen3 = ib.AnalogIn(board.IO34)  # SENSOR 3 (atrás izquierdo) pin IO34
sen4 = ib.AnalogIn(board.IO35)  # SENSOR 4 (atrá derecho) pin IO35

# Crea una lista con los sensores infrarrojos para poder recorrerlos fácilmente
infrarrojos = [sen1, sen2, sen3, sen4]

#funcion que convierte a entero base 10
# Utiliza desplazamiento de bits
def arreglo_a_entero(bits):
    valor = 0
    for bit in bits:
        valor = (valor << 1) | bit
    return valor

# revisa los cuatro sensores IR, y genera un
# arreglo de 0 y 1s (0-blanco, 1-negro)
def leer_sensores(infrarrojos,valor_critico=3000):
    return [int(sen.value < valor_critico) for sen in infrarrojos]

# Bucle infinito que lee e imprime los valores de los sensores continuamente
while True: 
    estado_sensores =leer_sensores(infrarrojos,3500)
    print(estado_sensores)
    print(arreglo_a_entero(estado_sensores))
    sleep(0.1)
```

[Este código](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/code_lecturaIR_4Bit.py) permite leer **cuatro sensores infrarrojos (IR)** colocados en las esquinas del sumobot. Estos sensores ayudan a detectar el borde del **dojo**, que normalmente es una superficie **negra con bordes blancos**. La idea es que el robot pueda **reconocer cuándo se está saliendo del área de combate** y reaccionar.

---

###  ¿Qué hace cada parte?

#### 1. **Inicialización del hardware**

```python
from ideaboard import IdeaBoard
ib = IdeaBoard()
```

Aquí se activa la placa "IdeaBoard", que nos permite controlar sensores, motores, etc.

#### 2. **Lectura de sensores**

```python
sen1 = ib.AnalogIn(board.IO36)  # Sensor frontal izquierdo
sen2 = ib.AnalogIn(board.IO39)  # Sensor frontal derecho
sen3 = ib.AnalogIn(board.IO34)  # Sensor trasero izquierdo
sen4 = ib.AnalogIn(board.IO35)  # Sensor trasero derecho
```

Cada sensor IR está conectado a un pin del microcontrolador. Estos sensores detectan **reflexión de luz**:

* **Negro (dojo)** → poca reflexión → valor **bajo**
* **Blanco (borde)** → mucha reflexión → valor **alto**

Los sensores se agrupan en una lista:

```python
infrarrojos = [sen1, sen2, sen3, sen4]
```

---

### ¿Cómo se detecta si el sensor ve negro o blanco?

```python
def leer_sensores(infrarrojos, valor_critico=3000):
    return [int(sen.value < valor_critico) for sen in infrarrojos]
```

* Si el valor del sensor es **menor que 3000**, se interpreta como **negro** (dentro del dojo), y se pone un **1**.
* Si es mayor, se interpreta como **blanco** (borde), y se pone un **0**.

Ejemplo:
Supongamos que los sensores leen:
`[negro, blanco, blanco, negro]`
→ Esto se convierte en:
`[1, 0, 0, 1]`

---

### Convertir los bits a un número entero

```python
def arreglo_a_entero(bits):
    valor = 0
    for bit in bits:
        valor = (valor << 1) | bit
    return valor
```

Este truco convierte la lista de bits `[1, 0, 0, 1]` en un número entero.
¿Cómo lo hace?

* Comienza con `valor = 0`
* Por cada bit en la lista:

  * Desplaza `valor` una posición a la izquierda (como multiplicar por 2)
  * Luego suma el bit

Ejemplo paso a paso:

```
[1, 0, 0, 1]
1) valor = 0 << 1 = 0 | 1 = 1
2) valor = 1 << 1 = 2 | 0 = 2
3) valor = 2 << 1 = 4 | 0 = 4
4) valor = 4 << 1 = 8 | 1 = 9
```

Resultado final: **9**

Entonces, el patrón `[1, 0, 0, 1]` representa el número **9**.

---

### Bucle principal

```python
while True: 
    estado_sensores = leer_sensores(infrarrojos, 3500)
    print(estado_sensores)               # Ejemplo: [1, 0, 0, 1]
    print(arreglo_a_entero(estado_sensores))  # Ejemplo: 9
    sleep(0.1)
```

Este bucle:

1. **Lee los sensores**
2. **Muestra el estado en forma de bits** (0 y 1)
3. **Convierte ese estado en un número entero**
4. **Repite cada 0.1 segundos**

---

### ¿Para qué sirve esto en el Sumobot?

* Cada **combinación de sensores** nos dice dónde está el robot con respecto al borde.
* Al convertir ese patrón en un número, el robot puede decidir **qué hacer** más fácilmente (avanzar, girar, retroceder, etc.).

