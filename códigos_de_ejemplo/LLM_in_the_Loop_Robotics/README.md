## Robótica LLM-in-the-Loop

Tomás de Camino Beck, Ph.D.  
Universidad CENFOTEC  

![sumobotLLM](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/LLM_in_the_Loop_Robotics/ArqSumobotGemini.png)

Robótica LLM-in-the-Loop o planificación autónoma con LLM, describe un sistema en el cual un modelo de lenguaje grande (LLM) está en el ciclo de control o decisión de un robot. El robot no solo ejecuta instrucciones, sino que consulta al LLM en tiempo real para:

- Interpretar situaciones del entorno
- Generar o adaptar planes de acción
- Traducir lenguaje natural a código o comandos
- Resolver ambigüedad o ajustar comportamientos

El programa [`code_grid_gemini.py`](https://github.com/Universidad-Cenfotec/ExpoCenfo/blob/main/Ejemplos_LLM_ESP32/LLM_in_the_Loop_Robotics/code_grid_gemini.py) implementa un sistema robótico que combina navegación autónoma con generación de instrucciones usando inteligencia artificial generativa. Es un ejemplo práctico de:

* **AGVs (Automated Guided Vehicles)**: robots que se mueven en un entorno siguiendo rutas definidas. Puede aprender más sobre AGV con el sumobot en [este link](https://github.com/Universidad-Cenfotec/Sumobot/tree/main/c%C3%B3digos_de_ejemplo/AGVs)
* **LLM-in-the-Loop Robotics**: una arquitectura donde un modelo de lenguaje grande (LLM) como Gemini participa en tiempo real en la toma de decisiones del robot.

El robot se desplaza sobre una cuadrícula de líneas negras utilizando sensores infrarrojos para mantenerse en el camino y un giroscopio para girar con precisión. La secuencia de movimientos no está preprogramada; en cambio, se genera dinámicamente al enviar un "prompt" a Gemini, que devuelve una lista de comandos como `F, L, R` (Forward, Left, Right).

Para este ejercicio, se utiliza el [Sumobot de CENFOTEC](https://github.com/Universidad-Cenfotec/Sumobot) pero aplica en general para cualquier robot que cuente con giroscópio, y sensores IR seguidores de Línea

Detalles de como conectar el ESP32 a Gemini lo spueden ver en [este video](https://youtu.be/rFI_8TIMCNI?si=_rteSFMyBVmcoIL1). Este código utiliza ese ejemplo de base.

---

## Componentes clave del sistema

### Conexión a red y configuración

El bloque inicial configura el robot para conectarse a una red WiFi usando las credenciales definidas en el archivo `secrets.py`. Luego establece una sesión HTTPS con la API de Gemini.

### Botón de activación

Se configura el pin `IO0` (botón BOOT del ESP32) como entrada digital. Solo cuando este botón es presionado y soltado, el robot solicita instrucciones a Gemini y ejecuta la secuencia generada. Esto permite control manual sobre cuándo iniciar una navegación.

```python
keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)
```

---

## Interacción con Gemini (LLM-in-the-Loop)

### `obtener_movimientos(inicio, final)`

Genera un texto (prompt) como el siguiente:

> Necesito una secuencia de comandos c1,c2,c3,... donde cada comando c puede ser F, L o R, para que un robot se mueva del punto (0, 0) al punto (2, 3)...

Este prompt se envía a Gemini, y se espera una respuesta directa con una lista de comandos, por ejemplo:

```
F,F,L,F,F,R,F
```

### `preguntar_gemini(prompt)`

Hace la solicitud HTTP a Gemini usando el método POST. Si la respuesta es válida, extrae el texto generado por el modelo.

---

## Movimiento y navegación

### `forward_line_stop()`

Esta función hace que el robot avance sobre una línea negra, utilizando dos sensores delanteros y dos traseros. Se detiene cuando detecta una intersección (ambos sensores traseros detectan línea negra).

### `girar_grados(grados, drift)`

Usa el giroscopio para girar con precisión 90 grados a la izquierda o derecha, compensando el drift del sensor (deriva natural que se calibra previamente).

---

## Ejecución de la secuencia

### `execute(commandlist)`

Recorre la lista de comandos `['F', 'F', 'L', 'F']` y ejecuta la función correspondiente:

* `F` llama a `forward_line_stop()`
* `L` llama a `girar_grados(-90)`
* `R` llama a `girar_grados(90)`

Este mecanismo abstrae las acciones concretas del robot, permitiendo que las decisiones de alto nivel sean tomadas por el LLM.

---

## Loop principal

```python
while True:
    event = keys.events.get()
    if event and event.released:
        ...
```

Solo si se presiona y suelta el botón, el robot solicitará la ruta a Gemini, la interpretará y la ejecutará. Esto previene ejecuciones accidentales o en bucle.

te y adaptable. Representa una convergencia entre robótica física y modelos generativos, y puede considerarse una introducción experimental a las arquitecturas **LLM-in-the-Loop**, donde la lógica de comportamiento no es codificada directamente, sino generada en tiempo real mediante IA.

---

## EL "Prompt"

```
    Objetivo
    Devuelve solo una secuencia separada por comas con los comandos mínimos que llevan al robot
    desde {inicio} hasta {final} sobre una cuadrícula cartesiana.
    
    reglas:
    1.La cuadrícula cartesiana (x,y), tiene su punto (0,0) a la izquierda abajo

    2. El robot siempre inicia mirando hacia el eje "y" positivo

    3. Comandos permitidos
    F – Avanza 1 unidad en la dirección actual  
    L – Gira 90° a la izquierda en su lugar  
    R – Gira 90° a la derecha en su lugar  

    4. Restricciones de salida
    - Sin texto adicional, títulos, comillas ni espacios.
    - Usa mayúsculas.  
    - Los comandos debe ser uno a uno, y estar separados solo por coma
      (ej.: L,F,F,R,F).

    5. Parámetros de entrada
    - inicio = {inicio}  ➜  tupla (x₀, y₀) 
    - final  = {final}   ➜  tupla (x₁, y₁)  

    6. El robot siempre temina mirando hacia el eje "y" positivo igual que como comenzó


    Ejemplo de salida con inicio (0,0) y final (3,2) válida es:  
    R,F,F,F,L,F,F

```

---

### Explicación de cada elemento

| Sección                        | Qué comunica                                                                                                                           | Por qué es importante                                                                                                                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Objetivo**                | “Devuelve solo una secuencia…”<br>Explica en una sola frase lo que se espera como resultado.                                           | - Los LLM responden mejor cuando se enuncia explícitamente la tarea.<br>- Un **verbo de acción** (“Devuelve”) evita ambigüedad.                                                                        |
| **2. Contexto geométrico**     | Describe la cuadrícula (origen en la esquina inferior izquierda, formato (x, y)) y la orientación inicial (mirando al eje y positivo). | - El modelo necesita un marco de referencia para razonar sobre posiciones y giros.<br>- Fijar la orientación inicial simplifica la búsqueda de rutas mínimas.                                          |
| **3. Comandos permitidos**     | F, L, R con definiciones concisas.                                                                                                     | - Limitar el vocabulario evita que el LLM genere tokens inesperados.<br>- Cada comando está **en mayúscula y en una línea aparte**, facilitando el “pattern matching”.                                 |
| **4. Restricciones de salida** | Lista de reglas de formato (sin texto extra, mayúsculas, separados por comas, sin espacios).                                           | - Actúa como una **política de validación**; el robot puede rechazar cualquier cadena que no cumpla todas las reglas.<br>- La ausencia de espacios reduce el pre-procesamiento en el microcontrolador. |
| **5. Parámetros de entrada**   | Explica `{inicio}` y `{final}` como tuplas y reitera la orientación final.                                                             | - Poner ejemplos de tipo y semántica de cada parámetro disminuye los errores de interpretación del LLM.<br>- Repetir la orientación final aclara la “meta-condición” que el plan debe cumplir.         |
| **6. Ejemplo**                 | `L,F,F,F,R,F,F`                                                                                                                        | - Proveer un **ejemplo canónico** sirve como “few-shot” oculto: el modelo imita el patrón sin sobre-explicar.<br>- Valida que las reglas dan un output humano-legible y máquina-parseable.             |


#### Por qué es adecuado para *LLM-in-the-Loop Robotics*

* **Claridad semántica**: el LLM recibe un dominio de comandos cerrado, lo que facilita validación automática y evita acciones ambiguas.
* **Formato estrictamente controlado**: permite que el software embarcado parsee la respuesta sin preprocesamiento complejo.
* **Variables inyectables**: `{inicio}` y `{final}` pueden sustituirse dinámicamente en cada iteración del bucle de control, integrando al modelo dentro del ciclo de decisión del robot.
* **Ejemplo orientativo**: reduce la entropía de la salida, algo crítico cuando la respuesta se usará directamente para ejecutar hardware.

---

## Posibles inconsistencias y retroalimentación en LLM-in-the-loop Robotics

Uno de los posibles problemas al utilizar un modelo de lenguaje como parte del sistema de control de un robot (*LLM-in-the-loop*) es que las respuestas generadas pueden ser **inconsistentes, ambiguas o no cumplir completamente con las restricciones** definidas en el prompt. Por ejemplo, el LLM podría devolver:

* Comandos con espacios o minúsculas (`"f, f, L"`)
* Texto explicativo antes o después de la secuencia (`"Aquí tienes la ruta: F,F,L"`)
* Secuencias que no llevan correctamente del punto de inicio al final

Estas fallas no son infrecuentes, ya que los LLM priorizan la *coherencia lingüística* sobre la precisión estructural, especialmente cuando no se les entrena directamente para tareas de control robótico.

#### Solución: retroalimentación desde el robot

Una de las ventajas del enfoque *in-the-loop* es que el propio robot puede actuar como **verificador de consistencia** y **orquestador de nuevas peticiones**:

* **Verifica localmente** si la secuencia cumple con el patrón esperado (usando expresiones regulares u otras validaciones simples).
* **Simula** (si tiene mapa) o **ensaya parcialmente** el trayecto para confirmar que el plan lo lleva al destino con la orientación final correcta.
* **Solicita una nueva respuesta** si detecta errores o inconsistencias, ajustando incluso el prompt para aclarar restricciones malinterpretadas.

Este ciclo de acción-validación-repetición convierte al LLM en un **colaborador iterativo**, no en una fuente única de verdad. La robustez del sistema no depende únicamente de la calidad del LLM, sino de la capacidad del robot para *evaluar* y *dialogar* con él de forma crítica.

Este patrón de colaboración es una de las características más prometedoras del paradigma *LLM-in-the-loop Robotics*, donde la inteligencia no reside en un solo componente, sino en la **interacción adaptativa** entre máquina física y modelo generativo.


