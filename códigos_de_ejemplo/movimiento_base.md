# Código Base para el Sumobot

Tomás de Camino BEck, Ph.D  
Universidad CENFOTEC

Se explica detalladamente ["code_scan.py"](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/code_scan.py) que sirve de base para comenzar a planear más estrategias del sumobot.  A partir de este código pueden ènsar en estrategias de ataque, de defensa, en diferentes posiciones de inicio, etc.

##  **Explicación general de las funciones (antes del `while True:`)**

Estas funciones preparan al robot para **moverse**, **detectar el borde del dojo con sensores infrarrojos** y **detectar al enemigo con un sensor ultrasónico**:

* **`arreglo_a_entero(bits)`**: convierte una lista de ceros y unos (de sensores IR) a un número binario en base 10. Así se representa fácilmente qué sensores detectan negro o blanco.

* **`leer_sensores()`**: lee los 4 sensores infrarrojos. Devuelve 1 si detecta blanco (borde), 0 si detecta negro (dentro del dojo).

* **`on_white()`**: retorna `True` si al menos un sensor detecta blanco (está tocando el borde).

* **`line_status()`**: devuelve el número entero que representa el estado de los sensores IR. Permite saber la posición del robot respecto al borde.

* **Funciones de movimiento (`forward()`, `backward()`, `left()`, `right()`)**: hacen que el robot se mueva en distintas direcciones por cierto tiempo y velocidad.

* **`stop()`**: detiene el robot.

* **`randomTurn()`**: gira en una dirección aleatoria (izquierda o derecha).

* **`wiggle()`**: "sacude" el robot moviéndolo rápido a los lados, útil para provocar al enemigo o moverse si está atascado.

* **`lookForward()`**: usa el sensor ultrasónico para medir qué tan lejos está el objeto al frente.

* **`scan()`**: hace que el robot gire poco a poco hasta encontrar un objeto frente a él (el enemigo). Si no lo encuentra después de 10 giros pequeños, devuelve `False`.

* **`forwardCheck()`**: avanza con cuidado **verificando constantemente los sensores infrarrojos**. Si detecta borde blanco, **reacciona retrocediendo y girando aleatoriamente**.

---

## **Explicación detallada del código principal**

Este es el **bucle principal**, donde el robot entra en acción constantemente:

```python
while True:
```

El robot repite las siguientes acciones **infinitamente** (hasta que se apague):

1. **Mide la distancia al frente** con el sensor ultrasónico:

   ```python
   distancia = sonar.dist_cm()
   ```

   * Si hay un objeto (otro robot) **a menos de 30 cm**, y no es una lectura inválida (`-1`):

     ```python
     if (distancia > -1 and distancia < 30):
     ```

     * Llama a `forwardCheck(0.2, 1, th)`, que avanza 0.2 segundos a velocidad máxima, **pero siempre verificando con sensores IR que no se salga del dojo**.
     * Luego se detiene y espera 0.3 segundos.

     ```python
     forwardCheck(0.2,1,th)
     stop()
     sleep(0.3)
     ```

2. **Si no detecta al enemigo**:

   ```python
   else:
       stop()
       sleep(0.3)
       right(0.1,0.2)
   ```

   * El robot se detiene, espera un poco y luego **gira a la derecha lentamente** para buscar al oponente.
   * Esto simula que está “escaneando” el entorno en busca de otro robot.

3. Al final de cada ciclo se asegura de que el robot esté en pausa un instante:

   ```python
   stop()
   ```
