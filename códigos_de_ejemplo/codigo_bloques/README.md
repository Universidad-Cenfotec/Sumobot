# Control Bluetooth del Sumobot en una Cuadrícula
Tomás de Camino Beck, Ph.D.  
Universidad CENFOTEC

![icon](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/codigo_bloques/icono_sumobot.jpeg)


## ¿Qué es esta aplicación?

Es una herramienta educativa visual que permite programar un **Sumobot** para moverse sobre una cuadrícula de líneas negras (como los AGV industriales), usando comandos de **avance, giro a la izquierda y giro a la derecha**, todo mediante **Bluetooth Low Energy (BLE)**.

---

## Componentes principales de la Web App

### 1. **Caja de Herramientas**

Bloques que representan movimientos:

* 🔼 Avanzar (`F`)
* ◀️ Izquierda (`L`)
* ▶️ Derecha (`R`)

### 2. **Espacio de Trabajo**

Zona donde el usuario arrastra y ordena los bloques para construir la secuencia de movimientos.

### 3. **Controles**

* 🔷 **Conectar:** inicia conexión BLE con el robot.
* ▶️ **Ejecutar:** envía la secuencia al robot.
* 🗑️ **Limpiar:** borra los bloques y el registro.

### 4. **Registro**

Muestra el historial de conexión, secuencia enviada y estado de ejecución.

---

## Conexión BLE al Sumobot

1. Enciende el Sumobot.
2. Presiona el botón **“Conectar”** en la web.
3. Selecciona el dispositivo BLE llamado `Sumobot_BLE_1`.
4. Una vez conectado, verás el mensaje “Conectado a: Sumobot\_BLE\_1”.

> Es necesario usar **Google Chrome** o **Microsoft Edge**.

---

## Crear y Ejecutar una Secuencia

1. **Arrastra** bloques al área de trabajo.
2. El orden define los movimientos que realizará el robot (por ejemplo: `F, L, F, R`).
3. Haz clic en **“Ejecutar”**:

   * Se enviará una cadena de comandos como `F,L,F,R` vía BLE.
   * El robot ejecutará la secuencia sobre la cuadrícula, reconociendo intersecciones mediante sensores.

---

## ¿Qué contiene el repositorio?

El repositorio incluye **dos archivos esenciales**:

### 1. `code_grid_ble.py`

Este archivo contiene el código que debe cargarse en el Sumobot. Controla:

* Movimiento con motores
* Lectura de sensores IR
* Giros con giroscopio
* Interpretación de comandos BLE (`F`, `L`, `R`)

### 2. `coding_blocks_spanish.html`

Es la interfaz gráfica en la que el usuario arma las secuencias de comandos y se conecta vía BLE.

---

## ¿Cómo se usa?

### Paso 1: Cargar el código al Sumobot

1. Conecta el Sumobot a tu computadora por USB.
2. Copia **los archivos `code_grid_ble.py` y renómbralo a `code.py`**.
3. Pégalos en el directorio raíz de la placa (llamada CIRCUITPY).
4. El robot reiniciará automáticamente con el nuevo código cargado.

### Paso 2: Ejecutar la Web App

Puede ejecutar el Web App directamente en [este link](https://universidad-cenfotec.github.io/SumoBlock.github.io/), o puede usar la siguiente opción si quiere correr desde su computadora,

1. Descarga el archivo `coding_blocks_spanish.html` del repositorio.
2. Ábrelo en tu navegador **Chrome** o **Edge** (solo requiere doble clic).
3. Asegúrate de que el robot esté encendido.
4. Conéctate, crea la secuencia y ejecuta.

Perfecto. Aquí tienes una sección para agregar al manual, explicando cómo preparar la superficie de la cuadrícula que utilizará el Sumobot:

---

## Superficie de Navegación: Cuadrícula de Líneas Negras

Para que el **Sumobot** pueda navegar correctamente y detectar intersecciones, necesita una superficie de fondo blanco con **líneas negras bien definidas**, al estilo de los **vehículos AGV**.

### ¿Cómo es la cuadrícula?

La cuadrícula que utiliza el Sumobot es similar al archivo `cuadricula_lineas_negras.svg` incluido en el repositorio. Esta cuadrícula:

* Tiene un fondo **blanco**.
* Presenta una malla de **líneas negras horizontales y verticales** que forman intersecciones.
* Está diseñada para que el robot avance en línea recta hasta una intersección, la detecte con sensores infrarrojos, y pueda girar 90° con precisión.

### Dimensiones recomendadas

Puedes construir esta superficie fácilmente con materiales accesibles:

* **Material base:** cartulina blanca o cartón blanco.
* **Líneas negras:** cinta eléctrica negra (tape aislante).
* **Espaciado entre líneas:** **20 cm** entre centros.
* **Ancho de las líneas negras:** **2 cm**.
* **Tamaño recomendado de la cuadrícula:** al menos de **80 cm x 80 cm** (una cuadrícula de 4x4 líneas es ideal para comenzar).

### Instrucciones para hacerla en casa o en el aula

1. Coloca una cartulina blanca o una plancha blanca rígida sobre una superficie plana.
2. Con una regla y lápiz, marca líneas horizontales y verticales separadas cada 20 cm.
3. Pega cuidadosamente cinta eléctrica negra sobre las líneas marcadas.
4. Asegúrate de que las intersecciones queden limpias y perpendiculares.

> Las líneas deben tener buen contraste con el fondo para que los sensores IR funcionen correctamente.


