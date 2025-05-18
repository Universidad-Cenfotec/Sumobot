# Código Base (busca y ataca)

Este código es un script de CircuiPython diseñado para controlar el sumobot de la Universidad CENFOTEC utilizando la placa IdeaBoard, junto con varios sensores y actuadores. Está orientado a estudiantes de secundaria y tiene como objetivo introducirlos en la programación de robots y el manejo de componentes electrónicos.

1. **Librerías e Importaciones**: Se importan varias librerías para interactuar con la placa IdeaBoard, el sensor de ultrasonidos HCSR04, control de tiempo, y generación de números aleatorios.

2. **Inicialización de Sensores y Actuadores**: Se crea una instancia para el sensor de ultrasonido (sonar) y se inicializan el sensor infrarrojo y los motores mediante la IdeaBoard.

3. **Funciones de Movimiento y Control**:
   - `wiggle(t, n, speed)`: Hace que el robot se mueva de izquierda a derecha por un tiempo `t`, a una velocidad `speed`, repitiendo el movimiento `n` veces.
   - `forward(t, speed)`, `backward(t, speed)`, `left(t, speed)`, `right(t, speed)`: Controlan el movimiento del robot en direcciones específicas por un tiempo `t` a una velocidad `speed`.
   - `stop()`: Detiene todos los motores del robot.
   - `randomTurn(t, speed)`: Hace girar al robot en una dirección aleatoria (izquierda o derecha) por un tiempo `t` a una velocidad `speed`.

4. **Funciones de Detección**:
   - `on_white(value)`: Utiliza un sensor infrarrojo analogo y devuelve una respuesta booleana, True si la lectura es menor que value, False de lo contrario
   - `lookForward()`: Utiliza el sensor de ultrasonidos para medir la distancia a objetos enfrente del robot y retorna esta distancia en centímetros.
   - `scan()`: Mueve el robot hacia un lado buscando objetos delante. Se detiene después de un número fijo de giros o cuando encuentra un objeto a una distancia adecuada.

5. **Navegación y Evitación de Obstáculos**:
   - `forwardCheck(t, speed)`: Mueve el robot hacia adelante pero revisa constantemente el sensor infrarrojo para evitar salir del área designada (Dojo). Si detecta el borde, se detiene, retrocede, y gira en una dirección aleatoria.

6. **Ciclo Principal**: En un bucle infinito, el robot primero intenta detectar objetos con `scan()`. Si encuentra algo, avanza con precaución usando `forwardCheck()`. Si no encuentra nada, gira aleatoriamente y luego avanza con precaución.
