#Tomás de Camino Beck
#Universidad CENFOTEC

# Importa el módulo 'board' que proporciona acceso a los pines del microcontrolador
import board

# Importa el módulo 'keypad' para manejar entradas desde botones o matrices de teclas
import keypad

# Configura un objeto 'Keys' que monitorea el pin IO0 como entrada de botón.
# IO0 está conectado al botón que dice "BOOT" al lado del "reset". 
# Este botón queda libre una vez iniciado el ideaboard.
# value_when_pressed=False indica que el pin se activa cuando está en bajo (LOW)
# pull=True activa la resistencia de pull-up interna del pin
keys = keypad.Keys((board.IO0,), value_when_pressed=False, pull=True)

# Bucle principal que se ejecuta indefinidamente
while True:
    # Obtiene el siguiente evento de botón, si existe (presionado o liberado)
    event = keys.events.get()

    # Si no hay evento, 'event' será None, así que se verifica si existe
    if event:
        # Si el evento indica que el botón fue liberado
        if event.released:
            # Imprime "Botón" en la consola
            print("Botón")
