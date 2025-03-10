![SumoBot](imagenes/SumobotBanner.png)

# Código y Diseños del Sumobot

El Sumobot es un robot simple, 100% desarrollado en Costa Rica, para competencias colegiales de Sumobot. Fue diseñado por el profesor Tomás de Camino Beck para la Universidad Cenfotec como parte de un programa de transformación educativa, con el objetivo de ampliar las capacidades de pensamiento computacional tanto en estudiantes de colegio como en estudiantes universitarios.

El Sumobot utiliza la placa [IdeaBoard](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki), desarrollada por CrCibernética. Esta placa, que es Open Source, tiene un ESP32 como microcontrolador y facilita la conexión de sensores, motores y su programación a través de USB o Wi‑Fi.

Puede ver este [video resumen](https://youtu.be/L98O-mApjXQ) de la primera competencia de Sumobot de Costa Rica, celebrada en el Maker Faire San José 2023.

---
## Componentes del Sumobot 2025

El Sumobot de el 2025 es un modelo nuevo, con más sensores y capacidades comparado con el Sumobot del 2024.

- En Construcción



Todos los componentes se pueden encontrar en Costa Rica en [CrCibernética](https://www.crcibernetica.com/sumobot-universidad-cenfotec/). [Aquí pueden ver un video](https://youtu.be/N60gXp_uzeo?si=2TApsz6n20wZ9ZoX) de los componentes que vienen como parte del kit.

---

## Chasis del Sumobot 2025

- En Construcción

---

# Armando el Sumobot 2026

- En Construcción
  
## Kit Sumobot 2025

- En Construcción

## Esquema de conexiones 2025

- En Construcción

## Baterías Sumobot 2025

- En Construcción

## Software para programar el Sumobot 2025

Para programar el Sumobot se utiliza Thonny, el cual se puede descargar desde este [enlace](https://thonny.org/).

### Instrucciones:
- Descargar la última versión de Thonny.
- Instalar.
- Una vez instalado, ir al menú "Herramientas > Opciones" o "Tools > Options" en inglés.
- En la pestaña "Intérprete" (o "Interpreter" en inglés), seleccionar "CircuitPython (Generic)".
- ¡Listo!
- [Video con detalles](https://youtu.be/Zc3oaAbVAdc)

## Código

El código "code.py" está desarrollado en CircuitPython. CircuitPython es un subconjunto de Python desarrollado para microcontroladores y facilita la portabilidad y programabilidad de dispositivos como el ESP32, entre otros. El Sumobot ya viene preparado para trabajar con CircuitPython y no es necesario cargar archivos adicionales. Si por alguna razón se debe "reflashear" el IdeaBoard, siga las instrucciones en este [enlace](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki/3.-Installation).

El código "hcsr04.mpy" corresponde a la librería para el sensor de distancia, el cual se utiliza para detectar otro robot que esté al frente del Sumobot.

### Funciones Básicas

- **wiggle(t, n, speed):** Hace que el bot se mueva de izquierda a derecha durante _t_ segundos, a velocidad _speed_, repitiéndolo _n_ veces.
- **forward(t, speed):** Mueve el bot hacia adelante durante _t_ segundos a velocidad _speed_.
- **backward(t, speed):** Mueve el bot hacia atrás durante _t_ segundos a velocidad _speed_.
- **left(t, speed):** Mueve el bot hacia la izquierda durante _t_ segundos a velocidad _speed_.
- **right(t, speed):** Mueve el bot hacia la derecha durante _t_ segundos a velocidad _speed_.
- **stop():** Detiene el bot.
- **randomTurn(t, speed):** Gira al azar a la izquierda o a la derecha durante _t_ segundos a velocidad _speed_.
- **lookForward():** Realiza la lectura del sensor ultrasónico y retorna la distancia en cm de lo que esté en frente del bot.
- **scan():** Rota hacia un lado hasta que detecta algo adelante o hasta que gire un número determinado de veces.
- **forwardCheck(t, speed):** Mueve hacia adelante, pero verifica, mediante el sensor IR, que no se salga del dojo. Cuando detecta el borde, realiza un movimiento hacia atrás y luego gira.

### Recuperar la configuración inicial

Si por alguna razón se desea resetear el Sumobot a los archivos iniciales, cargue, a través de Thonny en el dispositivo CircuitPython (con el Sumobot conectado), todos los archivos que vienen en el archivo ZIP "SumoBot_Device_Files.zip".

---

## Videos Instructivos
- En Construcción


---

# Competencia SumoBot

- En Construcción

## Formato de competición

- En Construcción

## Principios del juego

- En Construcción

---

# Reglamento

## DEFINICIONES:
1. **Sumobot:** El robot Sumobot es un robot de combate autónomo programado por el usuario, que deberá sacar a su rival del área de combate (dojo), ya sea empujándolo, arrastrándolo o dejándolo inhabilitado.
2. **Partida:** Enfrentamiento entre 2 robots de diferentes equipos, dividido en 3 combates.
3. **Maker Space:** Laboratorio de innovación de la Universidad CENFOTEC.
4. **GitHub:** Plataforma para crear proyectos abiertos de herramientas y aplicaciones, caracterizada, sobre todo, por sus funciones colaborativas que ayudan a que todos puedan aportar su granito de arena para mejorar el código.
5. **Mesa de arbitraje:** Persona o grupo de personas con autoridad, responsables de presidir el juego desde un punto de vista neutral y de tomar decisiones sobre la marcha que hagan cumplir las reglas de este reglamento.
6. **Dojo:** Área de combate, el espacio formado por la tarima circular y un espacio circundante denominado "área exterior de seguridad".
7. **Ronda:** Sistema en torneos en el que el perdedor de un encuentro queda inmediatamente eliminado de la competición, mientras que el ganador avanza a la siguiente fase. Se juegan rondas y, en cada una de ellas, se elimina a la mitad de los participantes hasta dejar un único competidor que se corona como campeón.

## ESPECIFICACIONES DEL ROBOT
- En Construcción

## REGLAS DEL JUEGO
- En Construcción

## SANCIONES Y APELACIONES

- En Construcción
---

# Preguntas Frecuentes

1. **¿El código se puede modificar?**  
   R: Sí, se puede modificar.

2. **¿Se pueden agregar partes al robot?**  
   R: No se permiten modificaciones estructurales del robot. Se puede adaptar para colocarle más sensores, pero no se permiten agregar puntas o extensiones para otros propósitos.

3. **¿Se puede modificar el hardware?**  
   R: Se pueden agregar sensores adicionales que no impliquen modificaciones en el robot (por ejemplo, modificar el chasis). Es decir, se pueden incorporar a la estructura del chasis sin agregar nada más. Cada robot será revisado antes de cada torneo de competencia.

4. **¿Se pueden agregar sensores de toque, por ejemplo?**  
   R: Se pueden agregar sensores adicionales que no impliquen modificaciones en el robot.

5. **¿Los estudiantes llevan la programación hecha o la memorizan?**  
   R: Los estudiantes llevan el programa hecho y, en el mismo evento, pueden modificar la programación. Si no cuentan con computador, se les facilitará uno en el evento.

---

# Algunas cosas por mejorar
- Algunos motores presentan problemas y generan un corto.
- Los cables de los motores deben ser más largos. Por el momento se están utilizando extensiones.

---

[Nombre del proyecto]

# Licencia

Sumobot es un robot desarrollado con el propósito de potenciar el aprendizaje de computación en colegios. Este proyecto está abierto a contribuciones y estamos encantados de recibir nuevas ideas.

Este robot está protegido por una licencia Creative Commons. Específicamente, se trata de la licencia CC BY‑NC‑SA 4.0, que significa Atribución‑NoComercial‑CompartirIgual 4.0 Internacional.

Bajo esta licencia, se permite el uso, distribución y modificación del robot, pero con las siguientes condiciones:
- **Atribución** — Debes dar el crédito correspondiente, proporcionar un enlace a la licencia e indicar si se han realizado cambios.
- **NoComercial** — No puedes utilizar el material para una finalidad comercial.
- **CompartirIgual** — Si remezclas, transformas o creas a partir del material, debes distribuir tus contribuciones bajo la misma licencia que el original.

Para obtener más detalles sobre la licencia, por favor visita [https://creativecommons.org/].

![CC](imagenes/Reconocimiento-no-comercial-sin-obra-derivada.png)

# Contribuciones

Si estás interesado en contribuir al Sumobot, por favor revisa las guías de contribución disponibles en la sección de "Documentación". Todas las contribuciones son bienvenidas, sin importar cuán pequeñas sean. Juntos podemos hacer que Sumobot sea mejor para todos.

![SumoBot1](imagenes/sumobot_varias.JPG)
