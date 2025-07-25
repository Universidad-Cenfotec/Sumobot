
# Programación del Sumobot


## Software para programar el Sumobot 2025

Para programar el Sumobot se utiliza Thonny, el cual se puede descargar desde este [enlace](https://thonny.org/).

### Instrucciones Rápidas:
- Descargar la última versión de Thonny.
- Instalar.
- Una vez instalado, ir al menú "Herramientas > Opciones" o "Tools > Options" en inglés.
- En la pestaña "Intérprete" (o "Interpreter" en inglés), seleccionar "CircuitPython (Generic)".
- ¡Listo!
- [Video con detalles](https://youtu.be/Zc3oaAbVAdc)

### Instruciones más detalladas:
- [Ver este enlace](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/instala_thonny.md)

### Iniciar Thonny
- [Seguir intrucciones acá](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/uso_thonny.md)
- [Ver video explicativo](https://youtu.be/EOnnslZhL2c?si=IYAHV_utJocjeJvx)

##  Resetear (Flashear) el IdeaBoard

Para resetear el IdeaBoard, se hace fácilmente a través de esta página:  [IdeaBoard Flasher](https://crcibernetica.github.io/ideaboard-terminal/) Asegurese que Thonny esté CERRADO, cuando intente reflashear o el flasher no va a encontrar el puerto cn el IdeaBoard.

En [este link hay un video que explica como hacerlo](https://youtu.be/sa7HqL8b7Vo?si=5yNcEPUFerEBaM1g)


## Código

> [Puede utilizar este asistente IA para ayudar a programar el Sumobot](https://chatgpt.com/g/g-6863f71f27b8819192a51ed05df367b0-asistente-de-programacion-sumobot-cenfotec)

El código "code.py" está desarrollado en CircuitPython. CircuitPython es un subconjunto de Python desarrollado para microcontroladores y facilita la portabilidad y programabilidad de dispositivos como el ESP32, entre otros. El Sumobot ya viene preparado para trabajar con CircuitPython y no es necesario cargar archivos adicionales. Si por alguna razón se debe "reflashear" el IdeaBoard, siga las instrucciones en este [enlace](https://github.com/CRCibernetica/circuitpython-ideaboard/wiki/3.-Installation).

El código "hcsr04.mpy" corresponde a la librería para el sensor de distancia, el cual se utiliza para detectar otro robot que esté al frente del Sumobot.

Un buen punto para comenzar es [este código](https://github.com/Universidad-Cenfotec/Sumobot/blob/main/c%C3%B3digos_de_ejemplo/code_scan.py).  En el el robot busca al enemigo, si lo encuentra ataca, y mantiene revisando si se sale del dojo.  Este código tiene mucho para mejorar pero les da un comienzo útil

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

## Videos Instructivos de Programación

Constantemente estaremos actualizando links cuando se vayan creando más videos:

- [Instalación de Thonny](https://youtu.be/Zc3oaAbVAdc?si=447Po0KyL_0hDAhJ)
- [Programación del Sumobot con Thonny](https://youtu.be/EOnnslZhL2c?si=rmjno9d8OHmJu21c)
- [Programación del NeoPixel](https://youtu.be/4abUHAFZwrY?si=RmHJYj71lK2cA2_J)
- [Programación de sensores Infrarrojos](https://youtu.be/1eArcnWW8Ek?si=TjnI8ONcFrolIb8A)
- [Programación de Motores](https://youtu.be/UMIWmT1n-kc?si=BwKY2DNXiGDF-0Ws)
- [Programación de Sensor Ultrasónico](https://youtu.be/RwY2lEPkyg8?si=KfbUV8WfN8I7yd2R)
