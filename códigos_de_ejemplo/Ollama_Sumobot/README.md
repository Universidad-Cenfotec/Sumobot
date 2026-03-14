
Instructivo para conectar Ollama con Llama 3.2 y Sumobot usando una página HTML
Este instructivo explica cómo montar un proyecto local en el que una página web recibe instrucciones en lenguaje natural, se las envía a Ollama con el modelo Llama 3.2, convierte la instrucción en una secuencia simple de comandos, y luego envía esa secuencia al Sumobot por Bluetooth Low Energy, BLE.
La idea pedagógica del proyecto es muy clara. El estudiante puede ver, en un solo flujo, cómo se conectan estas capas
una interfaz web
un modelo de lenguaje local
una traducción de lenguaje natural a comandos discretos
un robot físico que ejecuta la secuencia
---
1. Objetivo del proyecto
Construir una aplicación local donde el estudiante escriba una instrucción como esta
> avanza dos veces, gira a la izquierda y retrocede una vez
La página HTML debe
enviar esa instrucción a Ollama
pedirle a Llama 3.2 que la convierta en comandos simples
recibir una respuesta como
```text
F,F,L,B
```
mostrar la secuencia en pantalla
enviarla al robot Sumobot por BLE
---
2. Qué aprende el estudiante
Este proyecto sirve para enseñar varios conceptos a la vez
uso local de modelos de lenguaje
comunicación entre frontend y servidor local
prompting estructurado
traducción de lenguaje natural a símbolos discretos
conexión BLE desde el navegador
relación entre software, interpretación y acción física
También permite discutir una idea importante. El LLM no controla directamente los motores. Lo que hace es traducir intención humana a una secuencia formal de comandos. El robot solo ejecuta esa secuencia.
---
3. Requisitos
Hardware
una computadora con Windows, Linux o macOS
Sumobot con firmware BLE activo
Bluetooth en la computadora
Software
Ollama
modelo `llama3.2` descargado en Ollama
navegador basado en Chromium, por ejemplo Chrome o Edge, porque Web Bluetooth normalmente funciona allí
Python instalado, para correr un servidor local simple
el archivo HTML del proyecto
---
4. Estructura general del sistema
El sistema tiene este flujo
```text
Estudiante escribe instrucción
        ↓
Página HTML local
        ↓
Ollama con Llama 3.2
        ↓
Secuencia F,B,L,R
        ↓
BLE desde el navegador
        ↓
Sumobot
```
---
5. Preparación del entorno
Paso 1. Instalar Ollama
Instale Ollama desde su sitio oficial.
Una vez instalado, verifique que funciona desde terminal
```bash
ollama --version
```
Paso 2. Descargar Llama 3.2
Descargue el modelo
```bash
ollama pull llama3.2
```
Luego puede probarlo con
```bash
ollama run llama3.2
```
Si el modelo responde en consola, ya está listo.
Paso 3. Colocar el HTML en una carpeta de trabajo
Guarde el archivo HTML en una carpeta, por ejemplo
```text
C:\Users\Tomas\Downloads\Sumobot LLM Local
```
Paso 4. Levantar un servidor web local
Desde esa carpeta ejecute
```bash
python -m http.server 8000
```
Después abra en el navegador
```text
http://127.0.0.1:8000/robot_llm_ble.html
```
Esto es importante porque muchas funciones del navegador, incluyendo BLE y peticiones desde archivo local, funcionan mejor cuando la página se sirve desde un servidor local y no abriendo el archivo con doble clic.
---
6. Cómo funciona la HTML del proyecto
La página tiene cuatro áreas principales
Conexiones
Permite
verificar si Ollama está respondiendo
conectarse al robot por BLE
Instrucción
El estudiante escribe una orden en lenguaje natural.
Secuencia generada
La respuesta del modelo se muestra como texto, por ejemplo `F,F,L,R`, y además como indicadores visuales.
Log
Muestra mensajes del sistema, errores y confirmaciones de envío.
---
7. Variables clave del código
En la sección JavaScript aparecen varias constantes importantes
```javascript
const OLLAMA_URL = "http://127.0.0.1:11434/api/generate";
const MODEL = "llama3.2";

const SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e";
const CHAR_UUID    = "6e400002-b5a3-f393-e0a9-e50e24dcca9e";
```
Qué significa cada una
`OLLAMA_URL`
Es la ruta local donde la página le hace la petición a Ollama.
`MODEL`
Indica el modelo que se usará. En este proyecto es `llama3.2`.
`SERVICE_UUID`
Es el UUID del servicio BLE del robot.
`CHAR_UUID`
Es el UUID de la característica BLE a la que se le escribe la secuencia de comandos.
---
8. El lenguaje de comandos del robot
El proyecto usa cuatro comandos simples
`F` para avanzar, forward
`B` para retroceder, back
`L` para girar a la izquierda, left
`R` para girar a la derecha, right
Ejemplo
```text
F,F,L,R,B
```
Esto es útil didácticamente porque reduce la complejidad. El estudiante puede concentrarse en la traducción entre intención y acción.
---
9. Cómo la página verifica Ollama
Cuando se presiona Verificar, la función `checkOllama()` envía una petición POST a Ollama con un prompt mínimo.
```javascript
body: JSON.stringify({ model: MODEL, prompt: "Respond with OK", stream: false })
```
Si responde bien, la interfaz muestra que Ollama está conectado.
Idea pedagógica
Aquí se puede explicar que el navegador no está ejecutando el modelo. El navegador solo hace una petición HTTP a un servicio local que ya está corriendo en la máquina.
---
10. Cómo la página se conecta al robot por BLE
Cuando se presiona Conectar, la función `connectBLE()` utiliza Web Bluetooth.
```javascript
device = await navigator.bluetooth.requestDevice({
  filters: [{ services: [SERVICE_UUID] }],
  optionalServices: [SERVICE_UUID]
});
```
Luego obtiene el servicio y la característica donde escribirá los datos.
```javascript
const server = await device.gatt.connect();
const service = await server.getPrimaryService(SERVICE_UUID);
characteristic = await service.getCharacteristic(CHAR_UUID);
```
Idea pedagógica
Aquí conviene explicar que BLE trabaja con servicios y características. En este caso, la página no manda un archivo ni un mensaje complejo, sino una cadena corta de texto con la secuencia de comandos.
---
11. Cómo el LLM convierte la instrucción en comandos
La función `askLLM()` toma el texto escrito por el estudiante y construye un prompt como este
```text
Translate the instruction into robot commands.

Allowed commands:
F = forward
B = back
L = left
R = right

Rules:
Return ONLY a sequence separated by commas, nothing else.

Example:
F,F,L,R,B

Instruction:
avanza dos veces, gira a la izquierda y retrocede una vez
```
Ese prompt le dice al modelo exactamente qué formato debe devolver.
Idea pedagógica
Este es un excelente ejemplo de prompting con restricción de salida. No se busca una respuesta conversacional, sino una salida formal y predecible.
---
12. Limpieza de la salida del modelo
Después de recibir la respuesta, el código la limpia así
```javascript
let text = (data.response || "").trim().replace(/[^FBLR,]/g, "");
```
Esto elimina cualquier carácter que no sea
`F`
`B`
`L`
`R`
`,`
Por qué esto es importante
Aunque el prompt pide una secuencia limpia, un modelo podría devolver texto adicional. Esta línea reduce errores y refuerza la robustez del sistema.
---
13. Envío automático al robot
Si la secuencia generada es válida, la HTML la envía automáticamente al robot.
```javascript
if (text) {
  log(`Secuencia generada: ${text}`, "ok");
  await sendRobot(true);
}
```
Y luego la función `sendRobot()` escribe la secuencia por BLE
```javascript
const encoder = new TextEncoder();
await characteristic.writeValueWithoutResponse(encoder.encode(lastSequence));
```
Idea pedagógica
Aquí el estudiante ve un ciclo completo
intención humana
interpretación por IA
codificación simbólica
envío físico a un sistema embebido
---
14. Cómo ejecutar la demostración en clase
Secuencia sugerida
Parte 1. Mostrar el sistema completo
abrir la página
verificar Ollama
conectar el robot
escribir una instrucción simple
generar y enviar
observar el movimiento del Sumobot
Parte 2. Analizar las capas
Explique cada capa por separado
HTML como interfaz
Ollama como servidor local
Llama 3.2 como traductor de intención
BLE como canal físico de comunicación
Sumobot como actuador
Parte 3. Hacer pruebas con estudiantes
Pida ejemplos como estos
avanza una vez
gira a la derecha y avanza dos veces
retrocede una vez y gira a la izquierda
avanza tres veces y gira a la derecha
Luego compare lo que el estudiante quiso decir con la secuencia producida.
---
15. Actividades didácticas recomendadas
Actividad 1. Predicción antes de ejecutar
Antes de presionar el botón, los estudiantes deben predecir qué secuencia devolverá el modelo.
Actividad 2. Diseño de prompts mejores
Pida a los estudiantes que mejoren el prompt para manejar casos más ambiguos.
Por ejemplo
dos pasos adelante
media vuelta
gira dos veces a la izquierda
Actividad 3. Validación de comandos
Pida a los estudiantes que modifiquen la HTML para detectar secuencias vacías o demasiado largas.
Actividad 4. Del lenguaje natural al autómata
Relacione la secuencia `F,B,L,R` con símbolos de entrada en una máquina de estados.
Actividad 5. Registro experimental
Haga que cada grupo documente
instrucción escrita
secuencia generada
comportamiento real del robot
errores observados
mejoras propuestas
---
16. Problemas comunes y cómo resolverlos
Ollama no responde
Posibles causas
Ollama no está corriendo
el modelo `llama3.2` no está descargado
el puerto `11434` no está disponible
Pruebas útiles
```bash
ollama list
ollama run llama3.2
```
La página abre pero no funciona bien
Posibles causas
se abrió el HTML con doble clic en vez de usar servidor local
el navegador bloquea alguna función
Solución
Ejecutar
```bash
python -m http.server 8000
```
No aparece el robot BLE
Posibles causas
Bluetooth apagado
firmware del Sumobot no está anunciando el servicio correcto
UUID no coincide con el del robot
El robot se conecta pero no se mueve
Posibles causas
el firmware no interpreta bien la cadena
el robot espera otro formato, por ejemplo salto de línea o separador distinto
la característica BLE correcta no es `6e400002-b5a3-f393-e0a9-e50e24dcca9e`
El modelo responde texto raro
Posibles causas
prompt demasiado ambiguo
el modelo agrega explicaciones
Soluciones
reforzar el prompt
mantener la limpieza con expresión regular
agregar validación extra antes de enviar al robot
---
17. Mejoras sugeridas para futuras versiones
Estas extensiones pueden servir como proyectos posteriores
agregar un botón para solo generar, sin enviar todavía
agregar una vista paso a paso de la secuencia
incluir comandos compuestos, por ejemplo `F2` o `L90`
registrar historial de instrucciones y movimientos
usar otro modelo local y comparar resultados
hacer que el robot devuelva confirmación por BLE
conectar esto con una cuadrícula física y navegación más estructurada
---
18. Valor pedagógico del proyecto
Este proyecto es valioso porque convierte un tema que a veces se ve abstracto, los modelos de lenguaje, en una experiencia concreta y visible.
Aquí la IA no aparece como algo mágico. Aparece como una capa intermedia entre
el lenguaje humano
una representación simbólica mínima
la acción física del robot
Eso lo vuelve muy útil para enseñar computación, robótica, interacción humano-máquina y diseño de sistemas inteligentes.
---
19. Sugerencia de explicación breve para estudiantes
Se puede presentar así al inicio de la clase
> En este proyecto vamos a usar un modelo de lenguaje corriendo de manera local para traducir instrucciones humanas a comandos simples de robot. La página web actúa como puente entre lo que escribimos, el modelo de lenguaje y el Sumobot. Así podemos ver cómo una intención expresada en lenguaje natural termina convirtiéndose en movimiento físico.
---
20. Archivos recomendados en el repositorio GitHub
Una estructura sencilla del repositorio podría ser esta
```text
sumobot-ollama-llama32/
│
├── robot_llm_ble.html
├── README.md
├── img/
│   └── esquema_general.png
└── docs/
    └── instructivo_ollama_llama32_sumobot.md
```
Si quiere, este mismo instructivo puede usarse como `README.md` principal o adaptarse a un formato más corto para la portada del repositorio.
---
21. Comandos mínimos para arrancar rápido
```bash
ollama pull llama3.2
ollama run llama3.2
cd "C:\Users\Tomas\Downloads\Sumobot LLM Local"
python -m http.server 8000
```
Luego abrir en el navegador
```text
http://127.0.0.1:8000/robot_llm_ble.html
```
---
22. Cierre
Este proyecto permite enseñar algo muy potente, un modelo de lenguaje local no solo conversa, también puede integrarse en sistemas interactivos reales. En este caso, sirve como traductor entre lenguaje natural y comportamiento robótico.
Desde el punto de vista didáctico, es un proyecto excelente porque une IA, web, BLE y robótica en una sola experiencia.
