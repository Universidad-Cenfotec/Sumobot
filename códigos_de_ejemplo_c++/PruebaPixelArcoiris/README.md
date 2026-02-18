# 🌈 PruebaPixelArcoiris (ESP32 / Arduino) — LED NeoPixel con efecto arcoíris

**Autora:** Fiorella Pérez López  
**Universidad CENFOTEC**

Este programa controla un **LED NeoPixel (RGB direccionable)** para mostrar un **efecto de arcoíris continuo**.  
Además, permite **detener el programa escribiendo un comando desde el Monitor Serial**, lo cual lo hace ideal para aprender:

- LEDs RGB
- Uso de librerías externas
- Comunicación por **Serial**
- Control básico de efectos visuales

Es un excelente primer ejemplo para introducir **iluminación programable** de forma visual y divertida 🌈

---

## 🧠 ¿Qué hace este código?

El programa:

1. Inicializa un LED NeoPixel incorporada en la IdeaBoard
2. Genera colores del arcoíris usando una función matemática
3. Cambia el color del LED suavemente
4. Escucha comandos escritos por el usuario en el **Monitor Serial**
5. Si el usuario escribe `STOP`, el programa se detiene por completo

---


## 📚 Librerías utilizadas

Este proyecto **usa una librería externa**:

### Adafruit NeoPixel
```cpp
#include <Adafruit_NeoPixel.h>
```

📦 Para instalarla:
1. Abre **Arduino IDE**
2. Ve a **Sketch → Include Library → Manage Libraries**
3. Busca **Adafruit NeoPixel**
4. Instálala

---

## 🕹️ Funciones importantes (explicadas fácil)

### `Wheel(byte WheelPos)`

Esta función convierte un número entre **0 y 255** en un color RGB.

- Primero pasa de **rojo → verde**
- Luego de **verde → azul**
- Finalmente de **azul → rojo**

Esto permite crear un **arcoíris suave**, sin saltos bruscos de color.

---

### Comunicación Serial

En el `loop()` el programa revisa:

```cpp
if (Serial.available()) {
  comando = Serial.readStringUntil('\n');
}
```

Esto permite que el usuario escriba texto en el **Monitor Serial**.

Si el texto es:

```text
STOP
```

El programa entra en:

```cpp
while (true);
```

Eso significa:
➡️ El microcontrolador **queda detenido para siempre** (hasta reiniciar).

---

## 🌈 Efecto arcoíris

El efecto se genera con este ciclo:

```cpp
for (int i = 0; i < 256; i++) {
  uint32_t color = Wheel(i);
  strip.setPixelColor(0, color);
  strip.show();
  delay(20);
}
```

- Recorre todos los colores posibles
- Cambia el LED poco a poco
- Produce una transición suave y continua

---

## 🎚️ Ajustes fáciles para experimentar

### Velocidad del arcoíris
```cpp
delay(20);
```

- Menor valor → más rápido
- Mayor valor → más lento

Ejemplo:
- `delay(5)` → muy rápido
- `delay(50)` → muy suave

---

## 🧪 Cómo usar el programa (paso a paso)

1. Instala **Arduino IDE**
2. Instala la librería **Adafruit NeoPixel**
3. Conecta el ESP32 por USB
4. Abre el archivo `PruebaPixelArcoiris.ino`
5. Selecciona:
   - **Tools → Board → ESP32 Dev Module**
   - **Tools → Port → (tu puerto)**
6. Presiona **Upload**

### Para detener el programa:
1. Abre **Serial Monitor**
2. Baud rate: **9600**
3. Escribe:
   ```text
   STOP
   ```
4. Presiona **Enter**

---

## ❗ Errores comunes

### El LED no enciende
- Revisa el pin de datos (GPIO2)
- Verifica alimentación del LED
- Revisa que la librería esté instalada

### El comando STOP no funciona
- Asegúrate de usar **115200 baud**
- Escribe `STOP` en mayúsculas
- Presiona **Enter**

---

## 🌟 Ideas de mejora

- Cambiar colores por comandos (`ROJO`, `AZUL`, etc.)
- Agregar botón físico para detener
- Usar varios LEDs con patrones distintos
- Combinar con sensores (luz, distancia, sonido)
