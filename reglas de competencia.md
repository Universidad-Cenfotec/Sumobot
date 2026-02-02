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

- **Cenfobots oficiales:** Todos los equipos competirán utilizando **Cenfobots oficiales** suministrados por la Universidad CENFOTEC.  
  Se aceptarán Cenfobots de versiones anteriores **únicamente si han sido actualizados** y son técnicamente equivalentes al modelo oficial **2025–2026**. Estos deberán ser validados y aprobados previamente por la organización.

- **Cumplimiento del reglamento:** Cualquier Cenfobot que **no cumpla estrictamente** con las especificaciones del modelo **2025–2026** no será autorizado para competir.  
  En caso de dudas, se recomienda comunicarse con los organizadores **lo antes posible**.


## Objetivo del Juego
El objetivo de cada robot Cenfobot es expulsar a su oponente fuera del dojo, ya sea empujándolo, arrastrándolo o inmovilizándolo. Los combates se desarrollan de forma autónoma, basados en la programación del Cenfobot.

---

## Formato del Torneo

- El torneo se organiza en dos fases, fase inicial que es la fase de grupos y la segunda fase que puede ser de eliminación directa y/o triangulares.

- Cada encuentro entre dos Cenfobots se denomina partida (encuentro entre dos equipos) y consta de 3 combates (luchas entre los Cenfobot).

- Cada combate tiene una duración máxima de 1 minuto y 30 segundos.

- El ganador de un combate recibirá 3 puntos y el perdedor obtendrá 0 puntos, en caso de empate se otorgará 1 punto a cada equipo, Si ninguno de los participantes se presenta al combate, ambos recibirán 0 puntos.

- Entre cada combate hay 1 minuto de pausa para ajustes técnicos o de estrategia.

- En cada partida, únicamente un (1) integrante del equipo podrá ingresar al área de competencia (Dojo); el resto de los miembros deberá permanecer fuera de dicha área durante el desarrollo de los combates.

---

##  Dinámica del Combate

![ganador](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/ganador2025.JPG)

Los Cenfobots deberán iniciar su comportamiento de forma totalmente autónoma, ubicados en la posición indicada por el juez.

Una vez que el juez declare el inicio del combate, ningún participante podrá tocar, manipular o intervenir el Cenfobot bajo ninguna circunstancia. En caso de incumplimiento, el juez determinará la sanción correspondiente, la cual podrá incluir la pérdida del combate.

### Condiciones de un combate

Un Cenfobot será declarado ganador del combate si se cumple cualquiera de las siguientes condiciones:

- Expulsa a su oponente completamente fuera del círculo negro interno del dojo.
- El Cenfobot oponente sale por su cuenta completamente fuera del círculo negro interno del dojo.
- El Cenfobot oponente no ejecuta ningún movimiento durante el tiempo límite del combate.
- El Cenfobot oponente queda inmovilizado debido a fallos mecánicos o como resultado del enfrentamiento.

### Condiciones de empate

- Si ninguno de los Cenfobot ejecuta movimiento alguno durante el tiempo de combate.
- Si, al finalizar el tiempo límite, ninguno de losCenfobot ha salido ni ha sido expulsado del círculo negro interno del dojo.

---

## Configuración Inicial del Combate

![configuracion](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/combates.jpg)

Cada combate inicia con una disposición distinta:

1. **Frente a frente** con la parte trasera cerca del borde blanco (aproximadamente).
2. **Lado a lado**, en direcciones opuestas.
3. **Espalda con espalda**.

---

## Revisión y Arbitraje

Previo a cada partida, todos los Cenfobots deberán someterse a una inspección técnica, con el fin de verificar el cumplimiento de las especificaciones establecidas en este reglamento. La organización se reserva el derecho de repetir la inspección en cualquier momento de la partida y cuando el equipo realice cambio de Cenfobot.

La mesa de arbitraje constituye la autoridad máxima durante la competencia y tendrá la potestad de:

- Interpretar y hacer cumplir el presente reglamento.
- Resolver disputas, incidencias técnicas o situaciones no previstas.
- Tomar decisiones inmediatas durante los combates.

Las decisiones de la mesa de arbitraje serán definitivas e inapelables.

## Causales de Penalización

Un equipo podrá ser penalizado en la competencia si incurre en cualquiera de las siguientes faltas:

- Realizar modificaciones estructurales no autorizadas al Cenfobot.
- No presentarse a una partida en el horario asignado.
- Exceder el peso máximo permitido del Cenfobot (315 gramos, incluyendo baterías).
- Utilizar baterías, motores, neumáticos u otros componentes distintos a los incluidos en el kit oficial autorizado.
- Incumplir de forma reiterada las instrucciones de la mesa de arbitraje o las normas de conducta establecidas.

La penalización será impuesta por el juez de partida y, en caso de una descalificación, deberá ser ratificada por el juez de mesa.

---

## Progreso del Torneo

El torneo se desarrollará en las siguientes etapas:

- La competencia iniciará con una **fase de grupos**, en la cual los equipos serán distribuidos mediante un **sorteo público**, realizado en una reunión virtual en vivo, organizada por la Universidad CENFOTEC.

- El procedimiento del sorteo será comunicado previamente a los equipos inscritos. La conformación final de los grupos será anunciada y validada oficialmente por la organización una vez realizado el sorteo.

- Una vez concluida la fase de grupos, los equipos clasificados avanzarán a una **segunda fase**, cuyo formato podrá ser de **eliminación directa, triangular u otro sistema competitivo**, según la cantidad de equipos clasificados y criterios definidos por la organización.

- En caso de empate en una partida que impida definir un ganador, este será determinado mediante **lanzamiento de moneda**, realizado por la mesa de arbitraje u otra forma que se defina entre los equipos y el juez de mesa.

- La organización podrá habilitar la clasificación de un número determinado de **“mejores segundos lugares”** para avanzar a la siguiente fase, de acuerdo con la cantidad de equipos inscritos y la estructura del torneo.

- Las decisiones relacionadas con la conformación de grupos, criterios de clasificación y ajustes al formato serán responsabilidad exclusiva de la organización.


---

## Sanciones y Ausencias

- Si un equipo no se presenta a un combate en el horario establecido, el equipo contrario será declarado ganador automático de dicho combate.

- Durante la segunda fase, si ningún equipo se presenta a la partida en el horario establecido, la organización podrá designar equipos sustitutos, seleccionados entre los mejores segundos lugares, de acuerdo con los criterios definidos por el comité organizador.

- Un equipo que llegue tarde a la partida perderá automáticamente su primer combate de la partida; sin embargo, podrá participar en los combates restantes, siempre que se presente antes de la hora estipulada para el combate respectivo.

- La mesa de arbitraje y el comité organizador tendrán la potestad de evaluar situaciones excepcionales y aplicar sanciones adicionales si lo consideran necesario.


---

## Espíritu del Torneo

La Competencia Sumobot tiene como objetivo principal fomentar el aprendizaje, la creatividad, la innovación y el trabajo en equipo.

Se promueve un ambiente de respeto, colaboración y sana competencia, permitiendo el apoyo entre equipos y la orientación por parte de docentes o tutores. No obstante, se enfatiza que el liderazgo en el diseño, armado y programación del Cenfobot debe recaer en los estudiantes, como parte fundamental del proceso formativo.


