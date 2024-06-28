![SumoBot](imagenes/SumobotBanner.png)

# Código y Diseños del Sumobot

El Sumobot es un robot simple, 100% desarrollado en Costa Rica, para competencias colegiales de sumobot. Fue diseñado por el profesor Tomás de Camino Beck para la Universidad Cenfotec como parte de un programa de transformación educativa con el objetivo de ampliar capacidades de pensamiento computacional tanto en estudiantes de colegio como en estudiantes de la universidad.

El Sumobot utiliza la placa [IdeaBoard](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki), desarrollada por CrCibernética, esta placa que es Open Source tiene un ESP32 como microcontrolador, y facilita la conexión de sensores, motores y su programación a través de USB o Wifi.

Pueder ver este [video de un resúmen](https://youtu.be/L98O-mApjXQ) de la primera competencia de Sumobot de Costa Rica, celebrada en el Maker Faire San José 2023



## Componentes del Sumobot 
![SumoBot Parts](imagenes/piezas_sumobot.jpg)

- [IdeaBoard (ESP32)](https://www.crcibernetica.com/crcibernetica-ideaboard/)
- Cable USB C
- Tiras de plástico de 2.5mm
- Tornillos y tuercas para colocar la placa IdeaBoard
- Tornillos adicionales para sostener motores
- 2 x Soportes de motor microgear
- 2 x [Micro motores](https://www.crcibernetica.com/micro-gearmotor/) de 200 RPM
- 2 X ruedas
- Soporte de 4 baterías AA
- [Sensor IR](https://www.crcibernetica.com/track-sensor-module/)
- [Sensor ultrasónico](https://www.crcibernetica.com/hc-sr05-ultrasonic-distance-sensor/) de distanca (HCSR04)
- Piezas de acrílico de 3mm [Ver archivo de corte láser](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/archivos_de_fabricacion/chasis_sumobot.svg)

Todos los componetes se puede encontrar en Costa Rica en [CrCibernética](https://www.crcibernetica.com/sumobot-universidad-cenfotec/). [Acá pueden ver un video](https://youtu.be/N60gXp_uzeo?si=2TApsz6n20wZ9ZoX) de los componntes que vienen parte del Kit.

## Chasis del SumoBot

Archivo "Sumobot_Chasis.svg" está en formato SVG para corte láser del chasis de Sumobot.  Se puede cortar tanto en acrílico como MDF u otro material con espesor de 3mm. 

También con el [chasis_sumobot_2024_3D.stl](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/archivos_de_fabricacion/chasis_sumobot2024_3D.stl) pueden utilizar imprimir el chasis en impresora 3D. Esto facilita agregar estructuras más complejas que no son posibles en 2D.

El chasis del robot se une con tiras (gasas) de plástico de 2.5mm, esto facilita el armado y la reparación, o modificación de algunas partes.

También hay una [versión](https://github.com/Universidad-Cenfotec/Sumobot/tree/main/archivos_de_fabricacion/FeeCAD_model) que es "snap" y que no ocupa ni pegamento ni tiras de plástico.

---

# Armando el Sumobot

Pueden ver [este video detallado](https://youtu.be/m4y3BSPjgoc?si=vLK6NNjRJQF1DbDc) de cómo armar el Sumobot.

## Kit Sumobot
![Kit Sumobot](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/kit_sumobot_2024.jpg)

El Kit Sumobot es creación de Universidad CENFOTEC, y lo distribuye CrCibernética.com. SI desean adquierir el kit pueden libremente contactar a CrCibernética.

## Esquema de conexiones

- el sensor infrarojo va conectado en el IO033
- El sensor ultrasónico conectado en IO026 (trig) y I0025(Echo)
- Los motores van en Motor 1 y Motor 2 (con posiciones invertidas)

![SumoBot_Conexions](imagenes/SumoBotCon.png)

## Baterías
- Las baterías se conectan, el cable rojo al pin marcado como "+" y el negro al pin "-", como se muestra en el siguiente esquema:

![SumoBot_baterías](imagenes/SumobotBat.png)

## Software para programar el Sumobot

Para programar el sumobot se utiliza Thonny, el cual pueden descargar en este [link](https://thonny.org/)

### Instrucciones:
- Descargar la última versión de Thonny
- Instalar
- Una vez instalado, ir al menú "Herramientas > Opciones" o "Tools > Options" en inglés
- En la pestaña de "Intérprete" (o "Interpreter" en inglés), seleccionar "CyrcuitPyton (Generic)"
- Listo!
- [Video con detalles](https://youtu.be/Zc3oaAbVAdc)

## Código

El código "code.py" está desarrollado en CircuitPython. Circuit Python es un subconjunto de Python desarrollado para microcontroladores, y facilita la portabilidad y programabilidad de micrcontroladores como el ESP32 y otros. El Sumobot ya viene preparado para trabajar con Circuit Python y no hay que cargar archivos adicionales. Si por alguna razón debe "reflashear" el IdeaBorad, siga las instrucciones en este [link](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki/3.-Installation)

El código "hcsr04.mpy" corresponde a la librería para el sensor de distancia. Que se utiliza para detectar otro robot que esté al frente del sumobot.


### Funciones Básicas

- wiggle(t,n,speed) Hace que el bot se mueva izquierda derecha por tiempo t (segundos), velocidad speed, n veces
- forward(t,speed) Mueve el bot hacia adelante por tiempo t (segundos), velocidad speed
- backward(t,speed) Mueve el bot hacia atras por tiempo t (segundos), velocidad speed
- left(t,speed) Mueve el bot hacia la izquierda por tiempo t (segundos), velocidad speed
- right(t,speed) Mueve el bot hacia la derecha por tiempo t (segundos), velocidad speed
- stop() detiene el bot
- randomTurn(t,speed) Gira izq o der al azar, por tiempo t y velocidad speed
- lookForward() Hace una lectura del sensor ultrasónico y retorna la distancia en cm de lo que esté en frente del bot
- scan() Rota hacia un lado hasta que detecte algo adelante, o gire un número determinado de veces
- forwardCheck(t, speed) Mueve hacia adelante, pero verifica con el sensor IR que no se salga del dojo.  Cuando detecta el borde hace un movimiento hacia atras y luego gira.

### Recuperar la configuración inicial

Si por alguna razón quiere resetear el Sumobot a los archivos iniciales, cargue a través de Thonny en el CircuitPython Device (el sumobot conectado) todos los archivos que vienen en el archivo ZIP "SumoBot_Device_Files.zip"

---

## Videos Instructivos
- [Cómo instalar Thonny](https://youtu.be/Zc3oaAbVAdc)
- [Conectar el Sumobot a Thonny](https://youtu.be/SpIcqRKmczk)
- [Instalando las baterías del Sumobot](https://youtu.be/ndWJ0q0M8CI)
- [Calibrando el sensor infrrarojo](https://youtu.be/XXJbzzaVefk) 
- [El código principal del Sumobot](https://youtu.be/86sQCr-bjjk)
- [CircuitPython: Programando el LED RGB](https://youtu.be/5ezFqexHwQE)
- [Programando el sensor infrarrojo](https://youtu.be/1JA3G-FPpJ4)
- [Programando el sensor ultrasónico](https://youtu.be/RwY2lEPkyg8)
- [Motores DC con el Sumobot](https://youtu.be/MybJACeDIgA)

---

# Competencia SumoBot
![SumoBot_Dojo](imagenes/competencia_sumobot.jpg)

## Formato de competición

- El torneo SumoBot se estructura como un torneo por eliminatoria.
- Dos robots compiten en un "Dojo". El que es sacado del ring, deja de funcionar , o sin posibilidad de movimiento, pierde
- Se define una llave previa donde los equipos serán asignados al azar.
- Los encuentros de dos robots los denominamos "Set"
- Cada Set consiste de 3 juegos (Match) de un minuto y medio, con una pausa de un minuto entre juegos, para ajustes o cambios de estrategia
- El “Dojo” es un ring circular de 80 cm de diámetro, de fondo negro, con 5 cm de linea de borde blanca. De esta manera los robots pueden indentificar cuando están dentro o fuera del ring, y detectar el borde a través de un sensor infrarojo.
- En este archivo PDF tiene el diseño del [Mini-Dojo](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/circulo_10cmEspesor.pdf). El mini-Dojo se puede utilizar para probar diferentes ideas y garantizar de que funciona el robot, pero siempre se debe tener en cuenta que el dojo de la competencia es mucho más grande y que encima tiene una lamina de acrilico de 3mm.

![Dojo](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/imagenes/Dojo.png)

## Principios del juego

- La mesa de arbitraje revisará el robot para determinar que sigue las especificaciones requeridas
- Son tres "COmbates" por partida , yse gana por puntos.
- Un robot perderá si es removido del dojo más allá de la línea blanca del borde, o si no ejecuta ningún movimiento dentro del tiempo establecido
- Cada batalla tiene una duración máxima de 1:00 minutos
- En caso de empate (no sea el robot sacado del dojo), la mesa de arbitraje considerará ganador el robot con mayor número de ataques
- Las tres acciones de batalla son atacar, defender y buscar
- La competencia es por eliminación, y van clasificando en pares hasta la final.
- El código de los dos primeros lugares será publicado de forma abierta en este GitHub, con el fin de ir mejorando el nivel año con año. 

# Reglamento

## DEFINICIONES:
1. Sumobot: El robot sumobot es un robot de combate autónomo programado por el usuario, que deberá sacar a su rival del área de combate (dojo) ya sea empujando o arrastrando, o dejándolo inhabilitado.
2. Partida: enfrentamiento entre 2 robots de diferentes equipos, dividido en 3 combates
3. Maker Space: laboratorio de innovación de la Universidad CENFOTEC.
4. GitHub: plataforma para crear proyectos abiertos de herramientas y aplicaciones, y se caracteriza sobre todo por sus funciones colaborativas que ayudan a que todos puedan aportar su granito de arena para mejorar el código.
5. Mesa de arbitraje: es la o las persona con autoridad responsable de presidir el juego desde un punto de vista neutral y de tomar decisiones sobre la marcha que hacen cumplir las reglas de este reglamento.
6. Dojo: área de combate, el espacio formado por la tarima circular y un espacio circundante denominado área exterior de seguridad
7. Ronda: Sistema en torneos que consiste en que el perdedor de un encuentro queda inmediatamente eliminado de la competición, mientras que el ganador avanza a la siguiente fase. Se van jugando rondas y en cada una de ellas se elimina la mitad de participantes hasta dejar un único competidor que se corona como campeón


## ESPECIFICACIONES DEL ROBOT
1. Los robots son entregados por la Universidad CENFOTEC. Los robots deben ser armados por los colegios, con las instrucciones publicadas por Universidad CENFOTEC en el GitHub
2. El peso del robot con caja y las baterías su peso es de 260 g. El peso debe mantenerse siempre entre 260-290 gramos. Al agregar otros sensores, el peso puede aumentar ligeramente (por ejemplo, un sensor ultrasónico pesa aproximadamente 8.5 gramos).
3. No se permiten modificaciones estructurales en el robot. Se pueden adaptar para colocar más sensores, pero no se pueden agregar puntas o extensiones para otros propósitos.
4. Se pueden agregar sensores adicionales que no impliquen modificaciones en la estructura del robot.
5. No se pueden cambiar los neumáticos o las ruedas del robot para asegurar condiciones de igualdad entre los robots y que el ganador se determine por estrategia.
6. No se pueden cambiar los motores
7. No se puede utilizar otro tipo de baterías
8. Cada robot será revisado antes de cada competencia.
9. En situaciones especiales con respecto a las especificaciones del robot, su estructura y funcionamiento, que no estén claramente definidos en las reglas, quedará a criterio unificado de los jueces.

## REGLAS DEL JUEGO
1. Un fiscal revisará cada robot para asegurarse de que cumple con las especificaciones requeridas. En caso de duda, será verificado por jueces.
2. Cada "Partida" consta de tres "combates". Cada equipo, en un combate, da 3 puntos por ganar, 1 punto si es empate, y 0 si pierde
3. Al iniciar la partida, el equipo debe programar el robot para que espere 3 segundos antes de comenzar sus movimientos y actividad
4. Un robot pierde si es removido del dojo más allá de la línea blanca del borde o si no ejecuta ningún movimiento durante el tiempo asignado, o queda inmovilizado por el oponente.
5. Cada batalla tiene una duración máxima de 1 minuto y 30 segundos.
6. En caso de empate en un combate, cada equipo gana 1 punto.
7. La competencia incia por grupos, y las siguientes rondas son por eliminación y los equipos avanzan en pares hasta la final.
8. Cada combate comienza diferente. Primero con los robots frente a frente a una distancia aproximada de 10 cm, Luego espalda a espalda pegados. y luego lado a lado pegados viendo en direcciones opuestas.
9. Entre cada combate se tiene 1 minuto para revisar el robot y hacer posibles cambios
10. De todos los equipos que perdieron en la primera ronda, se escogen un número, por definir, de los segundos mejores.
11. Si en una partida no se presenta uno de los equipos, ganará el que se presentó (gana 9 puntos por partida en la primera ronda, o pasa a la siguiente ronda a partir de la segunda ronda)
12. Si en una partida no se presenta ninguno de los equipos, para la siguiente ronda se escogerá de los mejores segundos lugares

## SANCIONES Y APELACIONES
1. Si un equipo no se presenta para un "match" en el día del evento, el equipo oponente clasificará automáticamente.


## DISPOSICIONES FINALES
Este evento tiene cómo objetivo colaborar, apoyar y estimular la comunidad, por lo cual cada colegio representado podrá recibir apoyo de sus oponentes en el momento que ellos así lo manifiesten. Los docentes pueden ayudar y asesorar a sus equipos. Se espera de los docentes que dejen y estimulen a sus estudiantes a realizar el 100% del trabajo. 

# Preguntas Frecuentes

1.	¿Código se puede modificar?
R/ Si se puede modificar

2. ¿Se puede agregar partes al robot?
R/ No se permiten modificaciones estructurales del robot. Se puede adaptar para colocarle más sensores, pero no se permiten agregar puntas, o extensiones para otros propósitos

3. ¿El hardware se puede modificar? 
R/ Se puede agregar sensores adicionales que no impliquen modificaciones del robot (modificar el chasis). Es decir, se pueden incorporar a la estructura del chasis sin agregar nada más.Cada robot será revisado antes de cada torneo competencia

4. ¿Se puede agregar sensores de toque por ejemplo?
R/ Se puede agregar sensores adicionales que no impliquen modificaciones del robot

5.  ¿Esa programación la llevan los estudiantes hechos o la llevan memorizada?
R/Los estudaintes llevan el programa heho, y en el mismo evento pueden modificar la programación. Si no cuentan con computador, se les facilitará uno en el evento.

# Algunas cosas por mejorar
- Algunos motores presentan problemas, y generan un corto
- Los cables de motores deben ser más largos. Por el momento se están utilizando extensiones

[Nombre del proyecto] 
# Licencia

Sumobot es un robot desarrollado con el propósito de potenciar el aprendizaje de computación en colegios. Este proyecto está abierto a contribuciones y estamos encantados de recibir nuevas ideas.

Este robot está protegido por una licencia Creative Commons. Específicamente, se trata de una licencia CC BY-NC-SA 4.0, que significa Atribución-NoComercial-CompartirIgual 4.0 Internacional.

Bajo esta licencia, se permite el uso, distribución y modificación del robot, pero con las siguientes condiciones:
- Atribución — Debes dar el crédito correspondiente, proporcionar un enlace a la licencia e indicar si se han realizado cambios.
- NoComercial — No puedes utilizar el material para una finalidad comercial.
- CompartirIgual — Si remezclas, transformas o creas a partir del material, debes distribuir tus contribuciones bajo la misma licencia que el original.

Para obtener más detalles sobre la licencia, por favor visita [https://creativecommons.org/]

![CC](imagenes/Reconocimiento-no-comercial-sin-obra-derivada.png)

# Contribuciones
Si estás interesado en contribuir a el Sumobot, por favor, revisa las guías de contribución disponibles en la sección de 'Documentación'. Todas las contribuciones son bienvenidas, no importa cuán pequeñas sean. Juntos podemos hacer que Sumobot sea mejor para todos.

![SumoBot1](imagenes/sumobot_varias.JPG)
