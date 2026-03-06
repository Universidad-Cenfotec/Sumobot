# Cuadrícula de programación (ejemplo)

Para mostrar cómo funciona la programación física del robot se utiliza una **cuadrícula de ejemplo de 4 × 4 casillas**.

Cada casilla contiene un **patrón blanco y negro** que representa un **código binario de 4 bits**.  
Cuando el robot se coloca sobre una casilla, sus **cuatro sensores infrarrojos inferiores** leen el patrón y lo interpretan como una instrucción.

## Características de la cuadrícula

- Tamaño de la cuadrícula: **4 × 4 casillas**
- Tamaño de cada casilla: **6 cm × 6 cm**
- Material utilizado: **cartón con pintura blanca y negra en aceite**

Esta cuadrícula funciona como un **ejemplo visual de cómo programar el robot utilizando patrones físicos**.

Los estudiantes pueden mover el robot de una casilla a otra para generar distintas instrucciones, permitiendo experimentar con la programación sin necesidad de escribir código.

## Ejemplo de lectura de un patrón

Cada sensor detecta si la superficie es blanca o negra:

| Superficie | Bit |
|------|------|
| Blanco | 1 |
| Negro | 0 |

Si el robot detecta el siguiente patrón:

⬜ ⬜ ⬛ ⬛

El código binario generado es:

```
1100
```

Ese código es interpretado por el programa del robot como una **instrucción específica**, por ejemplo avanzar.

## Imagen de la cuadrícula utilizada

![Cuadrícula de programación](img/Cuadricula.jpeg)

