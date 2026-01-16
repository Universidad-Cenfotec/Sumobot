# 👀 PruebaIR (ESP32) — Lectura de sensores infrarrojos con indicador NeoPixel

**Universidad CENFOTEC**  

Este programa sirve para **probar y entender sensores infrarrojos (IR)** conectados al ESP32.  
Lee **4 sensores analógicos**, muestra sus valores en el **Monitor Serial** y utiliza un **LED NeoPixel** como indicador visual:

- 🔴 **Rojo** → el sensor detecta **NEGRO**
- 🔵 **Azul claro** → el sensor detecta **BLANCO**

Además, el programa puede **detenerse escribiendo `STOP`** desde el Monitor Serial.

Es ideal como práctica previa para robots **seguidor de línea** o **sumo**.

---

## 🧠 ¿Qué hace este código?

El programa realiza un ciclo continuo donde:

1. Lee los 4 sensores IR uno por uno
2. Imprime el valor de cada sensor en el Monitor Serial
3. Decide si el sensor ve **blanco o negro** usando un valor umbral
4. Cambia el color del LED NeoPixel según el resultado
5. Permite detener todo el programa con el comando `STOP`

---

## 📚 Librerías utilizadas

Este proyecto usa una librería externa:

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

## 🎯 Concepto clave: blanco vs negro

El programa usa un **valor crítico**:

```cpp
const int valor_critico = 1000;
```

- Si la lectura es **mayor** → NEGRO
- Si la lectura es **menor** → BLANCO

💡 Este valor **depende mucho** del:
- Tipo de sensor
- Altura del sensor sobre el suelo
- Iluminación del ambiente
- Color del piso

👉 Es normal tener que ajustarlo.

---

## 🕹️ Funcionamiento del LED

El LED NeoPixel se usa como **semáforo visual**:

| Color | Significado |
|-----|-------------|
| 🔴 Rojo | Sensor detecta NEGRO |
| 🔵 Azul claro | Sensor detecta BLANCO |
| ⚫ Apagado | Programa detenido |

Esto permite entender el comportamiento **sin mirar la computadora**.

---

## ⌨️ Control por Monitor Serial

Durante la ejecución puedes escribir:

```text
STOP
```

Al presionar **Enter**:
- El LED se apaga
- El programa se detiene
- El ESP32 queda esperando reinicio

⚠️ Para volver a ejecutar el programa debes **reiniciar la placa**.

---

## 🧪 Cómo usar el programa (Arduino IDE)

1. Instala **Arduino IDE**
2. Instala la librería **Adafruit NeoPixel**
3. Conecta el ESP32 por USB
4. Abre `PruebaIR.ino`
5. Selecciona:
   - **Tools → Board → ESP32**
   - **Tools → Port → tu puerto**
6. Presiona **Upload**

### Para ver los datos:
- Abre **Serial Monitor**
- Baud rate: **115200**

---

## ❗ Errores comunes

### Siempre detecta blanco o negro
- Ajusta `valor_critico`
- Revisa la altura del sensor
- Prueba sobre diferentes superficies

### El LED no enciende
- Revisa que la librería esté instalada

### STOP no funciona
- Usa **115200 baud**
- Escribe STOP y presiona **Enter**

---

## 🌟 Ideas de mejora

- Usar **un LED por sensor**
- Mostrar combinaciones de sensores
- Enviar datos en formato tabla por Serial
- Integrar motores para seguimiento de línea
- Reemplazar delays por temporizadores

