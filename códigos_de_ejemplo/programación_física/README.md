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
