# 💡 NeoPixel (ESP32) — Control de colores por comandos desde el Monitor Serial

**Autora:** Fiorella Pérez López  
**Universidad CENFOTEC**

Este programa permite **controlar un LED NeoPixel (RGB direccionable)** escribiendo **comandos de texto** desde el **Monitor Serial**.

Es ideal para aprender:
- Uso básico de **LEDs RGB**
- Comunicación **Serial**
- Uso de **librerías externas**
- Cómo interpretar comandos escritos por el usuario

El LED cambia de color según la palabra que se escriba, lo que lo hace muy intuitivo y visual 🎨✨

---

## 🧠 ¿Qué hace este código?

El programa espera que el usuario escriba un **color** en el Monitor Serial.

Cuando recibe un comando:
- Cambia el color del LED NeoPixel
- Muestra mensajes de ayuda si el comando no existe
- Permite apagar el LED y **detener el programa** escribiendo `STOP`

---

## 📚 Librerías utilizadas

Este proyecto usa una librería externa:

### Adafruit NeoPixel
```cpp
#include <Adafruit_NeoPixel.h>
```

### Cómo instalarla
1. Abre **Arduino IDE**
2. Ve a **Sketch → Include Library → Manage Libraries**
3. Busca **Adafruit NeoPixel**
4. Instálala

---

## 🎯 Comandos disponibles

Desde el **Monitor Serial**, escribe uno de estos comandos y presiona **Enter**:

| Comando | Color |
|-------|-------|
| `rojo` | 🔴 Rojo |
| `verde` | 🟢 Verde |
| `azul` | 🔵 Azul |
| `amarillo` | 🟡 Amarillo |
| `celeste` | 🟦 Celeste |
| `lila` | 🟣 Lila |
| `blanco` | ⚪ Blanco |
| `stop` | ⛔ Apaga el LED y detiene el programa |

👉 El programa **no distingue mayúsculas**, así que `RoJo` o `ROJO` también funcionan.

---

## 🕹️ Funciones importantes

### `setColor(r, g, b)`

Enciende el LED con un color RGB:

- `r` → rojo (0–255)
- `g` → verde (0–255)
- `b` → azul (0–255)

Ejemplo:
```cpp
setColor(255, 0, 0); // rojo
```

---

### `apagarLed()`

Apaga completamente el LED NeoPixel.

---

## ⌨️ Uso con Arduino IDE

1. Instala **Arduino IDE**
2. Instala la librería **Adafruit NeoPixel**
3. Conecta el ESP32 por USB
4. Abre `NeoPixel.ino`
5. Selecciona:
   - **Tools → Board → ESP32**
   - **Tools → Port → tu puerto**
6. Presiona **Upload**

### Para controlar el LED:
1. Abre **Serial Monitor**
2. Baud rate: **115200**
3. Escribe un comando (ejemplo: `rojo`)
4. Presiona **Enter**

---

## ❗ Errores comunes

### El LED no enciende
- Asegúrate de que la librería esté instalada

### El comando no responde
- Revisa que el baud rate sea **115200**
- Presiona **Enter** después de escribir
- Usa palabras exactas (rojo, verde, etc.)

---

## 🌟 Ideas de mejora

- Agregar más colores
- Usar números en vez de texto (`1 = rojo`, `2 = verde`, etc.)
- Controlar varios LEDs
- Cambiar brillo del LED
- Combinar con sensores o botones
