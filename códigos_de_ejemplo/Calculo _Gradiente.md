# Cálculo de Gradiente

Tomás de Camino Beck, Ph.D.  
Universidad CENFOTEC  

## ¿Qué es Wombling?

El código [`code_gradiente.py`](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/code_gradiente.py) calcula la magnitud y dirección de un gradiente de grises. **Wombling** es una técnica utilizada en análisis espacial para **detectar gradientes** o **bordes significativos** dentro de un campo escalar continuo, es decir, en regiones donde una variable medida (como temperatura, altitud, concentración, cantidad de luz, etc.) cambia rápidamente en el espacio.
La técnica fue originalmente propuesta por **William H. Womble** en 1951 para identificar zonas de transición en paisajes biológicos, pero se ha aplicado en una amplia variedad de disciplinas: geografía, ecología, epidemiología, robótica y análisis de sensores.

---

## Fundamento matemático

En términos generales, el **gradiente** de una función escalar $f(x, y)$ representa la **dirección y magnitud del cambio más rápido** de esa función. El gradiente se define como:

$$
\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)
$$

Donde:

* La **dirección** del gradiente apunta hacia donde el campo cambia más rápidamente.
* La **magnitud** indica cuán rápido está ocurriendo ese cambio.

---

## ¿Cómo se aplica Wombling en la práctica?

Como en muchos casos no tenemos una función matemática continua sino **puntos de muestreo discretos**, la técnica de Wombling estima el gradiente a partir de estos puntos. Para eso:

### 1. Se toma una cuadrícula local de puntos, típicamente 2x2.

Por ejemplo, en un robot con sensores de distancia dispuestos así:

```
s2 --- s1
 |     |
s4 --- s3
```

### 2. Se estima el gradiente espacial a partir de las diferencias entre los valores:

Usando combinaciones de las diferencias en cada eje:

$$
dx = s4 - s3 + 0.5 \cdot ((s3 - s4) + (s2 - s1))
$$

$$
dy = s1 - s3 + 0.5 \cdot ((s3 - s4) + (s2 - s1))
$$

Estas fórmulas estiman la derivada parcial en cada dirección, tomando en cuenta tanto la dirección principal como las diferencias diagonales.

### 3. Se calcula:

Los valores $dx$ y $dy$ representan las magnitudes de las aristas de un vector que indica la magnitud y dirección del gradiente. Se calcula de la siguiente manera, siguiendo pitágoras y trignometría,

* **Magnitud del gradiente**:

$$
\text{mag} = \sqrt{dx^2 + dy^2}
$$

* **Dirección (ángulo)**:

$$
\text{ang} = \text{atan2}(dx, dy)
$$

Esto da como resultado un vector que indica **dónde y cómo está cambiando más el valor medido**.

---

## Aplicaciones de Wombling

* **Robótica móvil**: para detectar cambios en la superficie, bordes de una línea, límites entre zonas, etc.
* **Geografía/Cartografía**: para localizar bordes entre diferentes tipos de terreno o zonas geológicas.
* **Ecología**: para detectar límites entre hábitats o zonas de transición biológica.
* **Epidemiología**: para encontrar fronteras espaciales en la propagación de enfermedades.

---

## Ventajas

* Funciona bien con **datos dispersos o discretos**.
* No requiere una superficie continua o derivables.
* Se puede aplicar en tiempo real en microcontroladores o entornos embebidos.

---

## Limitaciones

* Sensible al **ruido**: pequeñas variaciones pueden generar falsos positivos de gradientes.
* Depende de la **disposición y densidad** de los puntos sensados.
* Puede requerir técnicas de **suavizado (smoothing)** si los datos son ruidosos.

Claro, aquí tienes una sección dedicada a la **aplicación de la técnica de Wombling en un Sumobot** con sensores infrarrojos (IR) para detección de gradientes en el suelo:

---

## Aplicación de Wombling en un Sumobot con Sensores Infrarrojos

En el contexto de un **Sumobot**, la técnica de **Wombling** permite detectar **cambios de intensidad en el suelo**, que usualmente corresponden a superficies con gradientes de grises. Para esto se aprovechan **sensores infrarrojos (IR) analógicos**, que miden niveles de reflectancia del suelo —es decir, qué tan claro u oscuro es.

### Disposición típica de sensores

Los Sumobots utilizan comúnmente **cuatro sensores IR** colocados en las esquinas del chasis, formando una cuadrícula 2x2:

```
s2 --- s1    ← parte frontal del robot
 |     |
s4 --- s3    ← parte trasera del robot
```

Cada sensor devuelve un valor proporcional a la cantidad de **luz reflejada**. Suelo blanco (reflejante) da valores altos; suelo negro (absorbente) da valores bajos.

---

### ¿Qué permite hacer la técnica?

La técnica de Wombling estima un **vector de gradiente** a partir de los valores de los sensores, el cual indica:

* **Magnitud del cambio**: cuán abrupto es el contraste entre zonas del suelo.
* **Dirección del cambio**: hacia dónde se encuentra la mayor diferencia de tonos (por ejemplo, hacia un borde o línea).

Esto permite al robot navegar por superficies que tengan gradientes de grises, como en una superficie que vaya de negro a blanco, donde el sumobot se puede ubicar en el espacio.



