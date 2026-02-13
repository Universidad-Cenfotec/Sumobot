# 🦇 PruebaUltrasonico Sumobot que evita obstáculos a 10 cm

**Universidad CENFOTEC**  
**Autora:** Mariana Cubero  

Este programa controla un robot con **dos motores** y un sensor **ultrasónico**, para que avance solo y, cuando detecte un obstáculo muy cerca (**menos de 10 cm**), haga esto:

1. 🛑 Detecta el obstáculo  
2. ↩️ Retrocede por 1 segundo  
3. ➡️ Gira a la derecha por 1 segundo  
4. 🚀 Vuelve a avanzar  

Es un comportamiento sencillo, ideal como primera práctica para entender **motores + ultrasonido**.

---

## 🧠 ¿Qué hace este código?

En el `loop()`:

- Mide la distancia con `medirDistanciaCM()`
- Imprime esa distancia en el **Serial Monitor**
- Si la distancia es válida y menor a `10 cm`:
  - retrocede (`atras()`)
  - gira (`girarDerecha()`)
  - luego continúa avanzando
- Si no hay nada cerca:
  - avanza (`adelante()`)

---

## 📚 Librerías usadas

No usa librerías externas.

- pinMode
- digitalWrite
- delay / delayMicroseconds
- pulseIn
- Serial

---

## 🕹️ Funciones principales

### Movimiento
- `adelante()` → avanza
- `atras()` → retrocede
- `parar()` → detiene motores
- `girarDerecha()` → giro sobre su eje

### Ultrasonido
`medirDistanciaCM()`:
- Envía pulso TRIG
- Mide eco con pulseIn
- Convierte a centímetros
- Devuelve `-1` si no hay eco

---

## 🎚️ Ajustes recomendados

### Distancia de detección
```cpp
const float DISTANCIA_UMBRAL = 10.0;
```

Prueba valores como:
- 15 cm (más precaución)
- 5 cm (más agresivo)

### Tiempos
```cpp
delay(1000); // retroceso
delay(1000); // giro
```

---

## 🧪 Uso con Arduino IDE

1. Instala Arduino IDE  
2. Instala soporte ESP32  
3. Conecta el ESP32 por USB  
4. Selecciona placa y puerto  
5. Abre `PruebaUltrasonico.ino`  
6. Presiona **Upload**  

Para ver datos:
- Abre **Serial Monitor**
- Baud rate: **115200**

---

## ❗ Errores comunes

- Siempre marca `-1` → revisar TRIG/ECHO y voltajes, el jumper de la IdeaBoard debe de estar en Vin-Select y tener las baterías conectadas y encendidas.
- Motores en direcciones incorrectas  → Dale vuelta a los cables de los motores.

---

## 🌟 Ideas de mejora

- Giro aleatorio
- Uso de PWM para velocidad
- Promediar lecturas
- Usar `parar()` entre movimientos


