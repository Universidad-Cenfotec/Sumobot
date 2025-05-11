![SumoBot](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/SumobotBanner2025.png)

# ¿Que es el SumoBot de CENFOTEC? (o CenfoBot)

El Sumobot es un robot simple, 100% desarrollado en Costa Rica, para competencias colegiales de Sumobot. Fue diseñado por el profesor Tomás de Camino Beck para la Universidad Cenfotec como parte de un programa de transformación educativa, con el objetivo de ampliar las capacidades de pensamiento computacional tanto en estudiantes de colegio como en estudiantes universitarios.

El Sumobot utiliza la placa [IdeaBoard](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki), desarrollada por CrCibernética. Esta placa, que es Open Source, tiene un ESP32 como microcontrolador y facilita la conexión de sensores, motores y su programación a través de USB o Wi‑Fi.

Puede ver este [video resumen](https://youtu.be/L98O-mApjXQ) de la primera competencia de Sumobot de Costa Rica, celebrada en el Maker Faire San José 2023. Y acá pueden ver un [video resumen](https://youtu.be/9zarR0cKY90?si=D4UTzPx91h4megWT) de la segunda edición en el 2024

---

- [Componentes del Sumobot](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/componentes2025.md)
- [Armado del Sumobot](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/armado_2025.md)
- [Programación del Sumobot](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/programacion.md)


---

# Reglas del Juego e Indicaciones del Torneo – SumoBot 2025

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

## Objetivo del Juego
El objetivo de cada robot Sumobot es expulsar a su oponente fuera del dojo, ya sea empujándolo, arrastrándolo o inmovilizándolo. Los combates se desarrollan de forma autónoma, basados en la programación del robot.

---

## Formato de Competencia

- El torneo se organiza en formato de eliminación directa.
- Cada encuentro entre dos robots se denomina **partida** y consta de **3 combates**.
- Cada combate tiene una duración máxima de **1 minuto y 30 segundos**.
- La primera ronda, el ganador recibe 3 puntos por ganar y 1 punto en caso de empate. En las rondas eliminatorias, el equipo que gane **al menos 2 de los 3 combates** avanza a la siguiente ronda.
- Entre cada combate hay **1 minuto de pausa** para ajustes técnicos o de estrategia.

---

##  Dinámica del Combate

- Los robots deben iniciar su comportamiento autónomo en la posición indicada por el juez.  
- Una vez que el juez indica que el combate inicia, ningún participante puede tocar el robot.
- Se consideran válidas tres acciones: **atacar**, **defender** y **buscar**.
- Cada robot gana un combate si:
  - Expulsa a su oponente completamente fuera de la línea blanca del dojo.
  - Su oponente no ejecuta movimientos durante el tiempo límite.
  - Su oponente queda inmovilizado por fallos mecánicos o por efecto del enfrentamiento.

---

## Configuración Inicial del Combate

Cada combate inicia con una disposición distinta:

1. **Frente a frente** a 10 cm de distancia.
2. **Espalda con espalda**.
3. **Lado a lado**, en direcciones opuestas.

---

## Revisión y Arbitraje

- Cada robot será inspeccionado antes del combate para asegurar que cumple con las **especificaciones técnicas**.
- La **mesa de arbitraje** será la autoridad principal y podrá tomar decisiones sobre disputas o situaciones no previstas.
- Un equipo puede ser descalificado si:
  - Realiza cambios estructurales no autorizados al robot.
  - No se presenta a su partida asignada.
  - Excede el peso permitido (260 g – 290 g).
  - Utiliza baterías, motores o neumáticos distintos a los del kit oficial.

---

## Progreso del Torneo

- El torneo comienza con una **fase de grupos**.
- A partir de la segunda ronda, la competición es de eliminación directa.
- En caso de empate total en una partida, el ganador será decidido por **lanzamiento de moneda**.
- Se podrá seleccionar un número determinado de **"mejores segundos lugares"** para avanzar en el torneo, si así lo definen los organizadores.

---

##  Sanciones y Ausencias

- Si un equipo no se presenta a un combate, el equipo contrario gana automáticamente.
- Si ningún equipo se presenta, se escogerán equipos sustitutos de entre los mejores perdedores.
- Un equipo que llegue tarde pierde automáticamente su primer combate, pero puede competir en los siguientes.

---

##  Espíritu del Torneo

Este torneo busca fomentar el aprendizaje, la creatividad y el trabajo en equipo. Se permite el apoyo entre equipos y la colaboración con docentes, siempre motivando a que sean los estudiantes quienes lideren el diseño, armado y programación del robot.

---

##  Preguntas Frecuentes

1. **¿Se puede modificar el código del robot?**
   - Sí, el código puede ser adaptado libremente.

2. **¿Se pueden agregar sensores?**
   - Sí, siempre y cuando no impliquen modificaciones estructurales al robot, y no exceda el peso permitido.

3. **¿Se puede modificar el chasis o los motores?**
   - No. Las partes estructurales, motores, ruedas y baterías deben permanecer como en el kit oficial.

4. **¿Los estudiantes deben llevar el código memorizado?**
   - No, pueden llevarlo preparado y modificarlo durante el evento. Se les proporcionará equipo si no tienen acceso a uno.

---

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

![SumoBot1](imagenes/abajo2025.png)
