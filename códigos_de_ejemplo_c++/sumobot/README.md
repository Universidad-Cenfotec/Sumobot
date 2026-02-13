# 🥋 SumoBot - Robot que “busca y esquiva” con ultrasonido + sensores IR

**Creadores:**  
- Tomás de Camino Beck  
- Jeffry Valverde  
**Escuela de Sistemas Inteligentes - Universidad CENFOTEC**

Este proyecto controlar el robot **SumoBot de la Universidad CENFOTEC** usando el **ESP32 de la IdeaBoard**, dos motores (izquierdo/derecho), un sensor **ultrasónico** para “ver” al frente y **4 sensores IR** para detectar el borde/obstáculos cercanos.

La idea general es:
1. **Escanear** (girando a la izquierda) hasta “ver” algo a menos de ~30 cm con el ultrasonido.
2. **Avanzar en pasitos**, pero revisando IR constantemente.
3. Si algún IR detecta peligro/obstáculo → **se detiene**, **retrocede** y **gira aleatoriamente** para escapar.

---

## 🧠 ¿Qué hace este código exactamente?

En el `loop()`:

- Si `scan()` encuentra un objeto cerca (o “algo”) en pocos intentos:
  - intenta avanzar con `forwardCheck(0.5, 200)`
- Si `scan()` no encontró nada:
  - gira aleatoriamente con `randomTurn(1, 200)`
  - y vuelve a intentar avanzar con `forwardCheck(0.5, 200)`

La función importante aquí es **`forwardCheck()`**, porque avanza *por pedacitos* y revisa los sensores IR en cada paso. Eso evita que el robot se vaya directo al borde.

---

## 📚 Librerías usadas

Este código usa **solo lo básico de Arduino**, no requiere librerías externas:

- `Arduino.h` (incluida automáticamente en Arduino IDE)
- Funciones estándar como:
  - `pinMode()`, `digitalWrite()`, `analogRead()`, `delay()`, `delayMicroseconds()`
  - `Serial.begin()`
  - `pulseIn()`
  - `random()`

---

## 🧱 Funciones del código

### `setMotors(speedA1, speedA2, speedB1, speedB2)`
Controla la velocidad/dirección de los dos motores.  
En este diseño, cada motor tiene **dos pines**:
- Uno para girar en un sentido
- Otro para el sentido contrario

Ejemplo:
- **Avanzar:** `setMotors(speed, 0, speed, 0)`
- **Retroceder:** `setMotors(0, speed, 0, speed)`

---

### Movimientos básicos
- `forward(t, speed)` → avanza por `t` segundos y se detiene
- `backward(t, speed)` → retrocede por `t` segundos y se detiene
- `left(t, speed)` → gira a la izquierda por `t` segundos y se detiene
- `right(t, speed)` → gira a la derecha por `t` segundos y se detiene
- `stop()` → apaga motores

---

### `lookForward()`
Usa el ultrasónico para medir la distancia al frente en centímetros.

---

### `scan()`
Hace un “radar simple”:
- mide distancia
- si está lejos (más de 30 cm), gira un poquito a la izquierda y vuelve a medir
- repite hasta 10 intentos

Devuelve:
- `true` si encontró algo antes de 10 intentos
- `false` si no encontró nada (se rindió)

---

### `forwardCheck(t, speed)`
La función “inteligente”:
- divide `t` en pasos de 0.1s
- antes de cada paso, lee los 4 sensores IR
- si cualquiera pasa el **THRESHOLD**, aplica una rutina de escape:
  1. stop
  2. retrocede
  3. gira aleatorio
  4. sale de la función

---

## 🎚️ Ajustes importantes

### `THRESHOLD` (sensores IR)
```cpp
#define THRESHOLD 500
```
Ese número depende de tus sensores y del piso/arena de sumo.

Si el robot no detecta bien, prueba:
- 300, 400, 600, 700…

Tip práctico:
- abre el Serial Monitor y (si quieres) imprime analogRead() para ver valores reales (ver sección “Mejoras” abajo).