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


## ESPECIFICACIONES DEL CENFOBOT

- **Peso máximo:** El Cenfobot no deberá pesar más de 315 gramos, incluyendo baterías y cualquier sensor o componente adicional.

- **Fuente de energía:** El Cenfobot debe utilizar exactamente 4 baterías AA como fuente de energía.Se pueden utilizar baterías AA recargables, pero deben tener en cuenta que estas pueden afectar el peso del Cenfobot. Adicionalmente baterías recargables tienen por lo general una carga de 1.2V lo que puede afectar la potencia de los motores. NO se pueden colocar baterías de 9V, pues además los motores aunque inicialmente funcionan con 9V, soportan solo 6V, y terminarán quemados.

- **Contacto con el oponente:** No se permite ninguna modificación que genere contacto físico intencional con el Cenfobot contrincante. Esto incluye extensiones, accesorios, armas, mecanismos de empuje artificiales o cualquier otro elemento diseñado para tocar directamente al oponente.

- **Modificaciones para sensores:** Se permite realizar agujeros o adaptaciones en la estructura del Cenfobot únicamente para la instalación de sensores, siempre que dichas modificaciones no generen contacto físico con el Cenfobot oponente ni representen un riesgo durante el combate. Todo orificio o adaptación visible deberá contar obligatoriamente con un sensor funcional instalado; en caso contrario, el Cenfobot será considerado no apto para la competencia y no podrá participar hasta que la situación sea corregida y validada por la mesa de arbitraje.

- **Sensores adicionales:** Se podrán añadir sensores adicionales, siempre y cuando el peso total del Cenfobot no exceda los 315 gramos y las modificaciones cumplan con las demás especificaciones técnicas establecidas en este reglamento.

- **Modificaciones estéticas:** El Cenfobot podrá ser pintado, decorado o personalizado mediante calcomanías u otros elementos estéticos.

- **Modificaciones Físicas:** El Cenfobot no se puede modificar físicamente agregando extensiones, que hagan contacto con el oponente. Tampoco se puede reducir la altura de los soportes que se encuentran abajo a los lados de los sensores infrarrojos. La razón es porque los sensores pueden fallar en su lectura al estar tan cerca del piso, y porque le da ventaja al Cenfobot más bajo en choques de frente.

- Todos los equipos competirán utilizando Cenfobots oficiales suministrados por la Universidad CENFOTEC. Asimismo, se aceptarán Cenfobots de versiones anteriores únicamente si han sido actualizados y son técnicamente equivalentes al modelo oficial 2025–2026, estos serán validados y previamente aprobados por la organización.

- Cualquier Cenfobot que no cumpla estrictamente con las especificaciones del modelo 2025–2026 no será autorizado para competir. Si tiene dudas, comuníquese con los organizadores lo antes posible.

---

## Objetivo del Juego
El objetivo de cada robot Cenfobot es expulsar a su oponente fuera del dojo, ya sea empujándolo, arrastrándolo o inmovilizándolo. Los combates se desarrollan de forma autónoma, basados en la programación del Cenfobot.

---

## Formato del Torneo

- El torneo se organiza en dos fases, fase inicial que es la fase de grupos y la segunda fase que puede ser de eliminación directa y/o triangulares.

- Cada encuentro entre dos Cenfobots se denomina partida (encuentro entre dos equipos) y consta de 3 combates (luchas entre los Cenfobot).

- Cada combate tiene una duración máxima de **1 minuto y 30 segundos.**

- El ganador de un combate recibirá 3 puntos y el perdedor obtendrá 0 puntos, en caso de empate se otorgará 1 punto a cada equipo, Si ninguno de los participantes se presenta al combate, ambos recibirán 0 puntos.

- Entre cada combate hay 1 minuto de pausa para ajustes técnicos o de estrategia.

- En cada partida, únicamente un (1) integrante del equipo podrá ingresar al área de competencia (Dojo); el resto de los miembros deberá permanecer fuera de dicha área durante el desarrollo de los combates.

---

##  Dinámica del Combate

![ganador](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/ganador2025.JPG)

Los Cenfobots deberán iniciar su comportamiento de forma totalmente autónoma, ubicados en la posición indicada por el juez.

Una vez que el juez declare el inicio del combate, ningún participante podrá tocar, manipular o intervenir el Cenfobot bajo ninguna circunstancia. En caso de incumplimiento, el juez indicará la pérdida del combate.

### Condiciones de un combate

Un Cenfobot será declarado ganador del combate si se cumple cualquiera de las siguientes condiciones:

- Expulsa a su oponente completamente fuera del **círculo negro** interno del dojo.
- El Cenfobot oponente sale por su cuenta completamente fuera del círculo negro interno del dojo.
- El Cenfobot oponente no ejecuta ningún movimiento durante el tiempo límite del combate.
- El Cenfobot oponente queda inmovilizado debido a fallos mecánicos o como resultado del enfrentamiento (robot volcado por ejemplo).

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

### 1. Formato General del Torneo

1. Los equipos participantes serán distribuidos en grupos mediante un sorteo aleatorio realizado el día del evento.

2. La cantidad de grupos y el número de equipos por grupo serán definidos por la organización según la cantidad total de equipos inscritos. Los grupos podrán estar conformados por tres (3) o cuatro (4) equipos.

3. Durante la fase de grupos, cada equipo disputará una partida contra todos los demás equipos de su grupo.

4. Cada partida estará compuesta por tres (3) combates.

5. La puntuación de la fase de grupos será la siguiente:

   - Victoria en el combate: 3 puntos
   - Empate en el combate: 1 punto
   - Derrota en el combate: 0 puntos

###  2. Clasificación a la Segunda Fase

6. El equipo que ocupe el primer lugar de cada grupo clasificará automáticamente a la segunda fase.

7. La posición de los equipos dentro de cada grupo se determinará según la cantidad total de puntos obtenidos.

8. Si dos o más equipos finalizan con la misma cantidad de puntos en el mismo grupo, el desempate se realizará aplicando los siguientes criterios, en el orden indicado:

         a. Mayor diferencia de combates, calculada como: Diferencia de combates = Combates ganados − Combates perdidos

         b. Mayor cantidad total de combates ganados.

         c. Resultado directo entre los equipos empatados.

         d. Si el empate persiste, la organización podrá definir el clasificado mediante un combate de desempate o un sorteo realizado por la mesa de arbitraje.

###  3. Clasificación de Mejores Segundos Lugares

9. Cuando sea necesario completar el cuadro de la segunda fase, la organización podrá clasificar equipos adicionales entre los segundos lugares de cada grupo.

10. La clasificación de los segundos lugares se realizará utilizando el porcentaje de rendimiento, calculado de la siguiente forma: Porcentaje de rendimiento = (Puntos obtenidos / Puntos máximos posibles) × 100

11. Los puntos máximos posibles corresponden a ganar todas las partidas de la fase de grupos:

   - Grupo de 3 equipos: 18 puntos máximos.
   - Grupo de 4 equipos: 27 puntos máximos.

12. Los equipos con mayor porcentaje de rendimiento ocuparán las plazas disponibles para la segunda fase.

13. En caso de empate en porcentaje de rendimiento, se aplicarán sucesivamente los siguientes criterios:

         a. Resultado directo entre los equipos empatados, cuando corresponda.

         b. Combate de desempate o sorteo, según determine la organización.

###  4. Segunda Fase

14. Una vez concluida la fase de grupos, los equipos clasificados avanzarán a una segunda fase.

15. El formato de esta fase será definido por la organización según la cantidad de equipos clasificados y podrá consistir en eliminación directa, grupos triangulares, todos contra todos o cualquier otro formato competitivo equivalente.

16. La organización anunciará el formato antes del inicio de la segunda fase.

## 5. Empates en las Partidas

17. Una partida se considerará empatada cuando, al concluir los tres (3) combates reglamentarios, ninguno de los equipos haya obtenido ventaja suficiente para ser declarado ganador según las reglas de competencia.

18. Cuando el reglamento requiera determinar un ganador para efectos de clasificación o eliminación, el desempate podrá resolverse mediante un combate adicional, lanzamiento de moneda o cualquier otro mecanismo previamente anunciado por la organización y aplicado de forma uniforme a todos los participantes.

## 6. Disposiciones Generales

19. La organización tendrá la potestad de definir:

   - La cantidad y composición de los grupos.
   - El número de equipos que avanzan a la segunda fase.
   - La cantidad de mejores segundos lugares clasificados.
   - El formato de la segunda fase.
   - Los mecanismos de desempate no contemplados expresamente en este reglamento.

20. Todas las decisiones de la organización y de la mesa de arbitraje serán definitivas e inapelables.

21. La participación en el torneo implica la aceptación total de este reglamento por parte de todos los equipos y sus integrantes.




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


