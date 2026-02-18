
# Archivos `.mpy` 🐍

Los archivos `.mpy` son archivos de código precompilado utilizados por **MicroPython** y **CircuitPython**.  
Funcionan como módulos o librerías convencionales de Python, pero al estar precompilados, su ejecución es más rápida en un microcontrolador en comparación con un archivo `.py` convencional.  
Sin embargo, debido a su naturaleza, presentan ciertas **limitaciones e incompatibilidades**.

---

## Incompatibilidad entre versiones

### **CircuitPython**

En CircuitPython existen dos versiones mayores al momento de escribir esto: **9.x y 10.x**.
El bytecode entre estas dos versiones es igual, por lo que una libreria `.mpy` para **Circuitpython 9.x** funcionará de la misma forma y sin problemas en una instalación de **Circuitpython 10.x**.

##### Versiones de Legado, Circuitpython
Algunas placas pueden estar usando una versión de legado de Circuitpython, como las versiones **8.x**
Un archivo `.mpy` compilado para una versión **8.x**, **no** funcionará en una instalación de **9.x** o superior. 
Recomendamos actualizar el firmware de la placa a una versión mas reciente.

Si intentas ejecutar un código que importa un archivo `.mpy` incompatible, aparecerá el siguiente error:

```
incompatible .mpy file
```
(O su equivalente en el idioma de tu firmware).

### **MicroPython**

Si estás usando **MicroPython**, consulta la siguiente tabla de compatibilidad entre versiones:
<a id="tabla-compatibilidad"></a>

| Versión de MicroPython | Versión de `.mpy` |
|------------------------|-------------------|
| v1.23.0 y posteriores  | 6.3               |
| v1.22.x                | 6.2               |
| v1.20 - v1.21.0        | 6.1               |
| v1.19.x                | 6                 |
| v1.12 - v1.18          | 5                 |
| v1.11                  | 4                 |
| v1.9.3 - v1.10         | 3                 |
| v1.9 - v1.9.2          | 2                 |
| v1.5.1 - v1.8.7        | 0                 |

[Fuente](https://docs.micropython.org/en/latest/reference/mpyfiles.html)

---

## **¿Cómo saber qué versión usar?**

### **CircuitPython**
Al conectar tu dispositivo con CircuitPython a **Thonny** u otro IDE para acceder al REPL, deberías ver un mensaje similar a este en la consola:

``` python
]0;🐍Wi-Fi: apagado | REPL | 8.2.0\

Adafruit CircuitPython 8.2.0 on 2023-07-05; CRCibernetica IdeaBoard with ESP32
```

En este caso, la versión es **8.2.0**, por lo que se debe usar un archivo `.mpy` compatible con **8.x**.  
Lo importante es el primer número: por ejemplo, si la versión fuera **10.0.3**, se necesitaría un archivo `.mpy` de **9.x** o **10.x**.

## **MicroPython**
Cuando accedas al REPL de micropython escribe el siguiente código y presiona *Enter*.

``` python
import os
print(os.uname())
```

Una vez hecho esto un mensaje como este deberá aparecer:

```python
(sysname='esp32', nodename='esp32', release='1.25.0-preview', version='8987b39e0 on 2025-02-18', machine="CRCibernetica's IdeaBoard with ESP32-WROOM-32E")
```
Aquí, `release` indica la versión de micropython que está corriendo el microcontrolador. [Ver la tabla de compatibilidad de MicroPython](#tabla-compatibilidad)


## Incompatibilidad entre **CircuitPython** y **MicroPython**

Aunque **CircuitPython** es un proyecto hijo de **MicroPython**, los archivos `.mpy` **no son compatibles entre ambas plataformas** debido a diferencias en el formato de bytecode y en la máquina virtual subyacente.

Si vas a implementar o utilizar una librería para un dispositivo, **siempre verifica si está diseñada para CircuitPython o MicroPython**, ya que usar un `.mpy` de una plataforma en la otra causará errores.