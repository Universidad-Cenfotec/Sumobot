![SumoBot](SumobotBanner.png)

# Código y Diseños del Sumobot

El Sumobot es un robot simple pra competencias de sumobot. Fue diseñaro por Tomás de Camino Beck, para Universidad Cenfotec, como parte de un programa de trnasofrmación educativa, para ampliar capacidades de pensmaiento cpmputacional, tanto en estudiantes de colegio como en estudiantes de la universidad.

El Sumobot utiliza la placa [IdeaBoard](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki), desarrollada por CrCiberética. esta placa tiene un ESP32.

![SumoBot Parts](SumoBot_Parts.JPG)

## Componetes del Sumobot 
- [IdeaBoard (ESP32)](https://www.crcibernetica.com/crcibernetica-ideaboard/)
- 2 x [Micro motores](https://www.crcibernetica.com/micro-gearmotor/) de 200rpm
- [Sesnor IR](https://www.crcibernetica.com/track-sensor-module/)
- [Sensor ultrasónico](https://www.crcibernetica.com/hc-sr05-ultrasonic-distance-sensor/) de distanca (HCSR04)

Todos los componetes se puede encontrar en Costa Rica.

## Chasis del SumoBot

Archivo "Sumobot_Chasis.svg" está en formato SVG para corte láser del chasis de Sumobot.  Se puede cortar tanto en acrílico como MDF de 3mm


## Código

El código "code.py" está desarrollado en CircuitPython que es un subconjunto de Python desarrollado para microcontroladores. El Sumobot ya viene preparado para trabajar con Circuit Python y no hay que cargar archivos adicionales. Si por alguna razón debe "reflashear" el IdeaBorad, siga las instrucciones en este [link](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki/3.-Installation)

El código "hcsr04.mpy" corresponde a la librería para el sensor de distancia.

### Funciones Básicas

- wiggle(t,n,speed) Hace que el bot se mueva izqiuerda derecha pot tiepo t (segundos), velocidad speed, n veces
- forward(t,speed) Mueve el bot hacia adelante por tiepo t (segundos), velocidad speed
- backward(t,speed) Mueve el bot hacia atras por tiepo t (segundos), velocidad speed
- left(t,speed) Mueve el bot hacia la izquierda por tiepo t (segundos), velocidad speed
- right(t,speed) Mueve el bot hacia la derecha por tiepo t (segundos), velocidad speed
- stop() detiene el bot
- randomTurn(t,speed) Gira izq o der al azar, por tiempo t y velocidad speed
- lookForward() Hace una lectura del sensor ultrasónico y retorna la distancia en cm de lo que esté en frente del bot
- scan() Rota hacia un lado hacta que detecte algo adelante, o gire un núero determinado de veces
- forwardCheck(t, speed) Mueve hacia adelante, pero verifica con el sensor IR que no se salga del dojo.  Cuando detecta el borde hace un movimiento hacia atras y luego gira.

![SumoBot_Dojo](SumoBot_Dojo.JPG)

## Competencia SumoBot

### Formato de competición

- El torneo SumoBot se estructura como un torneo por eliminatoria.
- Dos robot compiten en un Dojo y el que es sacado del ring, o deja de funcionar, pierde
- Los encuentros de dos robots iniciales serán seleccionados al azar
- Cada Set consiste de 3 juegos de un minuto, con una pausa de un minuto entre juegos
- El “Dojo” es un ring circular de 120 cm de diámetro, con 10 cm de linea de borde, de fondo negro con línea blanca (para que los robots identifiquen el ring)

### Especificaciones del Robot
- El robot es entregado por Universidad Cenfotec
- No se permiten medificaciones estructurales del robot
- Se puede agregar sensores adicionales que no impliquen modificaciones del robot
- Cada robot será revisado antes de cada torneo competencia


### Principios del juego

- La mesa de arbitraje revisará el robot para determinar que sigue las especificaciones requeridas
- Son tres match por set , y gana el que gane dos o más match
- Pierde el robot que sea removido del dojo más allá de la línea blanca del borde, o que no ejecute ningún movimiento en ese tiempo
- Cada batalla tiene una duración máxima de 1:30 minutos
- En caso de empate (no sea el robot sacado del dojo), la mesa de arbitraje considerará ganador el robot con mayor número de ataques
- Las tres acciones de batalla son atacar, defender y buscar
- La competencia es por eliminación, y van clasificando en pares hasta la final.



![SumoBot1](SumoBot_1.JPG)
