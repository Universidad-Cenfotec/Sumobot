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

## Sumobot_Chasis.svg

Archivo en formato SVG para corte láser del chasis de Sumobot.  Se puede cortar tanto en acrílico como MDF de 3mm


## code.py

El código base está desarrollado en CircuitPython. El Sumobot viene preparado para trabajar con Circuit Python. Si por alguna razón debe "reflashear" el IdeaBorad, siga las instrucciones en este [link](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki/3.-Installation)
