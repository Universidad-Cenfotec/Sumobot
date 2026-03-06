# Programación física del Sumobot usando sensores infrarrojos

**Fiorella Pérez López**  
Universidad CENFOTEC

---

# Introducción

Este ejemplo muestra cómo utilizar los **sensores infrarrojos del Sumobot** para implementar un sistema de **programación física del robot**.

En lugar de escribir código en una computadora para definir cada movimiento que ejecutará el robot, los estudiantes pueden **programarlo colocando patrones físicos blanco/negro bajo los sensores**.

El robot interpreta estos patrones como **códigos binarios de 4 bits** y ejecuta acciones.

Este enfoque permite introducir conceptos de programación mediante **interacción tangible**, lo que lo hace especialmente útil para **niños o estudiantes que comienzan en robótica**.

---

# ¿Qué es programación física?

La **programación física** consiste en utilizar **objetos o patrones reales** para representar instrucciones de un programa.

En este ejemplo el proceso ocurre de la siguiente manera:

- Cada patrón blanco/negro representa un **número binario**
- El robot **lee ese patrón con sensores infrarrojos**
- El robot **interpreta el código**
- El robot **ejecuta una acción**

De esta forma, los estudiantes pueden **programar el robot sin escribir código**, utilizando únicamente **patrones físicos sobre el suelo o una cuadrícula de programación**.

---

# Lectura de sensores infrarrojos

El robot utiliza **cuatro sensores infrarrojos** ubicados en la parte inferior.

Cada sensor detecta si la superficie debajo es:

- blanca
- negra

Esta información se convierte en un **bit binario**.

| Superficie | Bit |
|------------|-----|
| Blanco | 1 |
| Negro | 0 |

Al utilizar **cuatro sensores**, el robot genera un **código binario de 4 bits**.

Ejemplo:

Patrón detectado:

⬜ ⬜ ⬛ ⬛

Código generado:
  **1100**

# Interpretación de códigos binarios

Cada combinación de bits corresponde a una **acción del robot**.

Los sensores infrarrojos detectan blanco o negro y generan un código de **4 bits**, el cual se interpreta como una instrucción.

## Códigos utilizados en este ejemplo

| Código | Acción |
|------|------|
| 1100 | Avanzar |
| 0011 | Retroceder |
| 1001 | Girar derecha |
| 0110 | Girar izquierda |
| 1110 | Giro 180° |
| 0101 | LED verde |
| 0010 | LED rojo |
| 0001 | LED azul |
| 0111 | Celebración |
| 0000 | Detener |
| 1111 | Iniciar programación |

---

# Posibles combinaciones no utilizadas

Un sistema de **4 bits permite 16 combinaciones posibles**.

En este ejemplo no todas las combinaciones se utilizan, lo que permite **extender el sistema con nuevas funciones**.

| Código | Posible uso futuro |
|------|------|
| 1010 | Cambiar velocidad |
| 1011 | Repetir instrucción |
| 0100 | Pausa programada |
| 1101 | Ejecutar bucle |

Estas combinaciones podrían utilizarse para **agregar nuevas capacidades al robot en futuras versiones del proyecto**.

---

# Archivos principales del proyecto

El sistema se compone de tres archivos principales.

| Archivo | Descripción |
|------|------|
| `README.md` | Documentación del proyecto y explicación del sistema |
| `robot_programable.py` | Código principal del robot con programación física |
| `prueba_sensores_ir.py` | Programa de prueba para calibrar sensores infrarrojos |

El archivo de prueba de sensores genera automáticamente un archivo llamado:
  **datos_bits.txt**
Este archivo guarda registros de lectura de sensores para **ajustar correctamente los umbrales de detección de blanco y negro**.

### Ejemplo de contenido generado en `datos_bits.txt`

```txt
------ Lectura de sensores ------
Sensor 1 (Delantero izquierdo) : valor=2581 -> bit=1
Sensor 2 (Delantero derecho)   : valor=62655 -> bit=0
Sensor 3 (Trasero izquierdo)   : valor=31357 -> bit=0
Sensor 4 (Trasero derecho)     : valor=2819 -> bit=1
Combinación binaria detectada: 1001
---------------------------------

------ Lectura de sensores ------
Sensor 1 (Delantero izquierdo) : valor=2561 -> bit=1
Sensor 2 (Delantero derecho)   : valor=62655 -> bit=0
Sensor 3 (Trasero izquierdo)   : valor=31218 -> bit=0
Sensor 4 (Trasero derecho)     : valor=2819 -> bit=1
Combinación binaria detectada: 1001
---------------------------------

------ Lectura de sensores ------
Sensor 1 (Delantero izquierdo) : valor=2541 -> bit=1
Sensor 2 (Delantero derecho)   : valor=62377 -> bit=0
Sensor 3 (Trasero izquierdo)   : valor=2819 -> bit=1
Sensor 4 (Trasero derecho)     : valor=2819 -> bit=1
Combinación binaria detectada: 1011
---------------------------------

------ Lectura de sensores ------
Sensor 1 (Delantero izquierdo) : valor=2541 -> bit=1
Sensor 2 (Delantero derecho)   : valor=62417 -> bit=0
Sensor 3 (Trasero izquierdo)   : valor=2819 -> bit=1
Sensor 4 (Trasero derecho)     : valor=2819 -> bit=1
Combinación binaria detectada: 1011
---------------------------------
