# Control de Movimientos Usando PDI y Giroscopio

Este documento explica el uso del código "code_PDI.py". Este es un código de prueba, que e puede utilizar para aprender sombre teoría de control aplicado a robots. Es un código en desarrollo y debe ser ajustado. Es una simplificación de movimiento de robots para navegación. Es necesario ajjustar una serie de parámetros para poder tener un movimiento controlado effectivo, y se debe dejar este reto a estudaintes. este código sirve como punto de partida.

---

## ¿Qué hace este programa?

Este programa controla un robot con dos ruedas usando una placa **ESP32** y un sensor llamado **giroscopio** (en este caso, el sensor LSM6DS3TRC). Tiene dos funciones principales:

* **Girar un ángulo exacto**.
* **Moverse en línea recta sin desviarse**.

---

## ¿Qué es un giroscopio?

El **giroscopio** mide qué tan rápido está girando el robot. Se mide en radianes por segundo (rad/s), como si dijera “estás girando a la derecha o izquierda a tal velocidad”. Usando esta información, el robot puede calcular cuánto ha girado, ¡sin necesidad de sensores externos!

---

## ¿Qué es el “drift”?

El **drift** es como un pequeño error constante que tiene el sensor. Si el robot está quieto, el sensor debería decir “0”, pero a veces da un número pequeño distinto de cero. Por eso, se mide el **drift al inicio** y luego se resta cada vez que usamos el giroscopio.

```python
drift = calibrar_drift(sensor, 5)
```

Esto mide el error promedio durante 5 segundos.

---

## ¿Cómo gira el robot exactamente?

La función `girar_grados(sensor, grados, drift)` hace que el robot gire una cantidad específica de grados. Lo hace así:

1. Enciende los motores en direcciones opuestas para que el robot gire.
2. Usa el giroscopio para ir sumando cuánto ha girado.
3. Cuando se acerca al final, **desacelera** para no pasarse.
4. Se detiene exactamente cuando ha girado lo necesario.

Esto se parece a cómo giramos nosotros para mirar algo exacto: primero rápido, luego despacio al acercarse al ángulo deseado.

---

## ¿Cómo avanza recto?

La función `straight_move(velocidad, duracion, drift)` hace que el robot avance en línea recta por cierto tiempo. Pero si un motor va un poquito más rápido que el otro, el robot se desviaría. Aquí entra en juego el **control PDI**.

---

## ¿Qué es el control PDI? (Explicación sencilla)

Un control **PDI** (Proporcional, Derivativo e Integral) es como un pequeño "cerebro matemático" que:

* **P (Proporcional):** Corrige según cuánto se está desviando ahora.
* **D (Derivativo):** Corrige si la desviación está aumentando muy rápido.
* **I (Integral):** Corrige errores acumulados con el tiempo.

Así, el robot **corrige en tiempo real** su rumbo. Si empieza a girar un poco hacia un lado, ajusta la velocidad de cada motor para seguir recto.

Ejemplo de vida real: imagina que caminas en línea recta con los ojos cerrados. Al mínimo desvío, mueves un poco tus pies para corregir. Eso es un control PDI.

---

## ¿Qué hace el programa al final?

En la parte principal (`while True:`):

1. Calibra el sensor de giroscopio.
2. Avanza recto 5 segundos.
3. Espera 1 segundo y repite.

Esto permite probar que el robot va recto gracias al giroscopio y al control PDI.

---

## Resumen visual:

| Parte del código   | ¿Qué hace?                                  |
| ------------------ | ------------------------------------------- |
| `calibrar_drift()` | Mide el error del giroscopio estando quieto |
| `girar_grados()`   | Gira una cantidad precisa de grados         |
| `straight_move()`  | Avanza en línea recta corrigiendo el rumbo  |
| `sensor.gyro[2]`   | Mide el giro en el plano del robot          |
| `PDI`              | Controla corrección con matemáticas simples |
