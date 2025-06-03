# Cálculo de Gradiente

Tomás de Camino Beck, Ph.D.  
Universidad CENFOTEC  

## ¿Qué es Wombling?

El código [`code_gradiente.py`](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/code_gradiente.py) calcula la magnitud y dirección de un gradiente de grises. **Wombling** es una técnica utilizada en análisis espacial para **detectar gradientes** o **bordes significativos** dentro de un campo escalar continuo, es decir, en regiones donde una variable medida (como temperatura, altitud, concentración, etc.) cambia rápidamente en el espacio.
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

