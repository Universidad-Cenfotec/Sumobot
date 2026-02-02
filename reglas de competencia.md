# Reglas del Juego e Indicaciones del Torneo 

## Definiciones

- **Cenfobot:** Robot de combate autónomo programado por el equipo participante, cuyo objetivo es sacar a su oponente del área de combate (dojo), ya sea empujándolo, arrastrándolo o dejándolo inhabilitado.
- **Equipo:** Conjunto de estudiantes inscritos oficialmente en la competencia.
- **Partida:** Enfrentamiento oficial entre dos (2) equipos distintos, compuesto por tres (3) combates.
- **Combate:** Enfrentamiento individual entre dos Cenfobots dentro del dojo, correspondiente a una de las instancias que conforman una partida.
- **Dojo:** Área donde se desarrollan los combates.
- **Mesa de arbitraje:** Persona o grupo de personas designadas por la organización con autoridad para supervisar los combates, aplicar el reglamento y tomar decisiones durante el desarrollo del torneo.
- **Fases:** Etapa del torneo en la cual los equipos compiten según el formato establecido. Dependiendo de la fase, el perdedor de una partida puede quedar eliminado, mientras que el ganador avanza a la siguiente etapa.
- **Empate:** Situación en la que ninguno de los Cenfobots logra la victoria bajo las condiciones establecidas para un combate o para una partida, según corresponda.
- **Maker Space:** Laboratorio de innovación de la Universidad CENFOTEC donde se desarrollan actividades y talleres relacionados con la competencia.
- **GitHub:** Plataforma de desarrollo colaborativo utilizada por la organización para publicar documentación, código base y recursos oficiales de la competencia.


## Especificaciones del Cenfobot

- **Peso máximo:** El Cenfobot no deberá pesar más de **315 gramos**, incluyendo baterías y cualquier sensor o componente adicional.
- **Fuente de energía:** El Cenfobot debe utilizar **exactamente cuatro (4) baterías AA** como fuente de energía.  
  - Se permite el uso de baterías AA recargables; sin embargo, debe considerarse que estas pueden afectar el peso total del Cenfobot.  
  - Adicionalmente, las baterías recargables suelen tener un voltaje nominal de **1.2 V**, lo cual puede afectar la potencia de los motores.  
  - **No se permite el uso de baterías de 9 V**, ya que, aunque los motores pueden funcionar inicialmente con este voltaje, están diseñados para soportar únicamente hasta **6 V**, lo que podría provocar daños permanentes.
- **Contacto con el oponente:** No se permite ninguna modificación que genere **contacto físico intencional** con el Cenfobot contrincante. Esto incluye extensiones, accesorios, armas, mecanismos de empuje artificiales o cualquier otro elemento diseñado para tocar directamente al oponente.
- **Modificaciones para sensores:** Se permite realizar agujeros o adaptaciones en la estructura del Cenfobot **únicamente para la instalación de sensores**, siempre que dichas modificaciones:
  - No generen contacto físico con el Cenfobot oponente.
  - No representen un riesgo durante el combate.
    
  Todo orificio o adaptación visible deberá contar obligatoriamente con un **sensor funcional instalado**. En caso contrario, el Cenfobot será considerado **no apto para la competencia** y no podrá participar hasta que la situación sea corregida y validada por la mesa de arbitraje.

- **Sensores adicionales:** Se podrán añadir sensores adicionales siempre y cuando:
  - El peso total del Cenfobot no exceda los **315 gramos**.
  - Las modificaciones cumplan con todas las demás especificaciones técnicas establecidas en este reglamento.

- **Modificaciones estéticas:** El Cenfobot podrá ser pintado, decorado o personalizado mediante calcomanías u otros elementos **exclusivamente estéticos**.

- **Modificaciones físicas:**  
  - No se permite modificar físicamente el Cenfobot agregando extensiones que hagan contacto con el oponente.  
  - No se permite reducir la altura de los soportes ubicados en la parte inferior, a los lados de los sensores infrarrojos.  
    - Esto se debe a que los sensores pueden fallar en su lectura al estar demasiado cerca del piso.
    - Además, reducir esta altura otorga una ventaja indebida al Cenfobot más bajo en choques frontales.

- **Cenfobots oficiales:**  
  Todos los equipos competirán utilizando **Cenfobots oficiales** suministrados por la Universidad CENFOTEC.  
  Se aceptarán Cenfobots de versiones anteriores **únicamente si han sido actualizados** y son técnicamente equivalentes al modelo oficial **2025–2026**. Estos deberán ser validados y aprobados previamente por la organización.

- **Cumplimiento del reglamento:**  
  Cualquier Cenfobot que **no cumpla estrictamente** con las especificaciones del modelo **2025–2026** no será autorizado para competir.  
  En caso de dudas, se recomienda comunicarse con los organizadores **lo antes posible**.




## Objetivo del Juego
El objetivo de cada robot Cenfobot es expulsar a su oponente fuera del dojo, ya sea empujándolo, arrastrándolo o inmovilizándolo. Los combates se desarrollan de forma autónoma, basados en la programación del Cenfobot.

---

## Formato de Competencia

- El torneo se organiza en formato de eliminación directa.
- Cada encuentro entre dos robots se denomina **partida** y consta de **3 combates**.
- Cada combate tiene una duración máxima de **1 minuto y 30 segundos**.
- La primera ronda, el ganador recibe 3 puntos por ganar y 1 punto en caso de empate. En las rondas eliminatorias, el equipo que gane **al menos 2 de los 3 combates** avanza a la siguiente ronda.
- Entre cada combate hay **1 minuto de pausa** para ajustes técnicos o de estrategia.

---

##  Dinámica del Combate

![ganador](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/ganador2025.JPG)

- Los robots deben iniciar su comportamiento autónomo en la posición indicada por el juez.  
- Una vez que el juez indica que el combate inicia, ningún participante puede tocar el robot.
- Se consideran válidas tres acciones: **atacar**, **defender** y **buscar**.
- Cada robot gana un combate si:
  - Expulsa a su oponente completamente fuera del área negra de juego (el robot queda fuera o encima totalmente de la linea blanca).
  - Su oponente no ejecuta movimientos durante el tiempo límite.
  - Su oponente queda inmovilizado por fallos mecánicos o por efecto del enfrentamiento.
- SI ninguno de los robots se mueve, se declara un empate.

---

## Configuración Inicial del Combate

![configuracion](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/combates.jpg)

Cada combate inicia con una disposición distinta:

1. **Frente a frente** con la parte trasera cerca del borde blanco (aproximadamente).
2. **Lado a lado**, en direcciones opuestas.
3. **Espalda con espalda**.

---

## Revisión y Arbitraje

- Cada robot será inspeccionado antes del combate para asegurar que cumple con las **especificaciones técnicas**.
- La **mesa de arbitraje** será la autoridad principal y podrá tomar decisiones sobre disputas o situaciones no previstas.
- Un equipo puede ser descalificado si:
  - Realiza cambios estructurales no autorizados al robot.
  - No se presenta a su partida asignada.
  - Excede el peso permitido (260 g – 295 g incluyendo baterías).
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

