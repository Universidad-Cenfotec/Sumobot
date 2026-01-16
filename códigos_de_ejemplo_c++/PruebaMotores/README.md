# 🔧 PruebaMotores (ESP32) — Control básico de un motor con velocidad y dirección

**Universidad CENFOTEC**  
**Autora:** Mariana Cubero  

Este programa es una **prueba simple de motores**, pensada para aprender cómo:

- Encender y apagar un motor
- Cambiar el **sentido de giro** (adelante / atrás)
- Variar la **velocidad** usando valores entre `-1` y `1`
- Usar **PWM** de forma básica en un ESP32

Es un excelente primer paso antes de hacer robots más complejos 🚗🤖

---

## 🧠 ¿Qué hace este código?

El programa prueba **un solo motor (Motor A)** usando diferentes valores de velocidad:

- `1` → máxima velocidad hacia adelante
- `0` → motor detenido
- `-1` → máxima velocidad hacia atrás
- `0.5` → velocidad media hacia adelante
- `-0.5` → velocidad media hacia atrás

Cada estado dura **2 segundos**, para que el comportamiento sea fácil de observar.

> 📝 Aunque hay pines definidos para el **Motor B**, este código se enfoca únicamente en probar el **Motor A**.

---

## 📚 Librerías usadas

Este programa **no usa librerías externas**.  
Solo funciones básicas del entorno Arduino:

- `pinMode()`
- `digitalWrite()`
- `analogWrite()`
- `delay()`
- `Serial.begin()`

---

## 🕹️ Concepto clave: velocidad entre -1 y 1

La función principal del programa es:

```cpp
bool moveMotor1(float s);
```

El valor `s` representa:

| Valor de `s` | Comportamiento |
|-------------|----------------|
| `1` | Máxima velocidad hacia adelante |
| `0.5` | Velocidad media hacia adelante |
| `0` | Motor detenido |
| `-0.5` | Velocidad media hacia atrás |
| `-1` | Máxima velocidad hacia atrás |

Si `s` está fuera del rango `[-1, 1]`, la función devuelve `false` y **no mueve el motor**.

---

## 🔁 ¿Cómo se controla el motor?

El motor tiene **dos pines**:

- Uno controla el giro hacia adelante
- El otro controla el giro hacia atrás

El código:
- Usa **PWM (`analogWrite`)** en un pin
- Apaga el otro pin con `LOW`

Así se controla:
- Dirección
- Velocidad

---

## 🧮 Función `motorMap()`

```cpp
int motorMap(float value, float fromLow, float fromHigh, float toLow, float toHigh)
```

Esta función convierte un número flotante (por ejemplo `0.5`) en un valor de **PWM (0 a 255)**.

Ejemplo:
- `0.5` → aproximadamente `127`
- `1.0` → `255`

Es similar a la función `map()` de Arduino, pero adaptada para valores decimales.

---

## 🧪 Qué verás al ejecutarlo

El motor:

1. Gira fuerte hacia adelante
2. Se detiene
3. Gira fuerte hacia atrás
4. Se detiene
5. Gira lento hacia adelante
6. Se detiene
7. Gira lento hacia atrás
8. Se detiene

Cada paso dura **2 segundos**.

---

## 🧰 Cómo usarlo en Arduino IDE

1. Instala **Arduino IDE**
2. Instala soporte para **ESP32**
3. Conecta el ESP32 por USB
4. Abre `PruebaMotores.ino`
5. Selecciona:
   - **Tools → Board → ESP32**
   - **Tools → Port → tu puerto**
6. Presiona **Upload**

Opcional:
- Abre el **Serial Monitor**
- Baud rate: **115200**

---

## ❗ Errores comunes

### El motor no se mueve
- Revisa tener el jumper de la placa en Vin-Select y que tenga las baterias conectadas y encendidas.

### El motor gira al revés
- Dale la vuelta a los cables del motor.

### Velocidad extraña
- Algunos drivers no responden igual al PWM
- Ajusta valores o prueba otro pin PWM

---

## 🌟 Ideas de mejora

- Agregar control del **Motor B**
- Controlar ambos motores con una sola función
- Controlar velocidad desde el **Monitor Serial**
- Usar botones o joystick