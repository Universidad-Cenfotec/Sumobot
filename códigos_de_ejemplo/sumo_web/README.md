
# Control remoto del Sumobot mediante Bluetooth Low Energy (BLE)

Fiorella Pérez López  
Universidad CENFOTEC

---

# Introducción

Este proyecto muestra cómo controlar un **Sumobot de forma remota utilizando Bluetooth Low Energy (BLE)** y una **interfaz web accesible desde el navegador**.

En lugar de utilizar un control físico o un programa instalado en la computadora, el robot puede ser controlado directamente desde una **página web interactiva**. Esta página permite enviar comandos de movimiento al robot, el cual los interpreta y ejecuta en tiempo real.

El robot utiliza un **sistema de control PDI basado en giroscopio** para mantener trayectorias rectas al avanzar o retroceder, compensando pequeñas diferencias entre los motores.

Este proyecto combina conceptos de:

- robótica móvil  
- sistemas embebidos  
- comunicación inalámbrica  
- control automático  
- interfaces web interactivas  
- desarrollo web aplicado a robótica  

---

# ¿Qué es el control mediante BLE?

Bluetooth Low Energy (BLE) es un protocolo de comunicación inalámbrica diseñado para dispositivos que requieren **bajo consumo energético**.

En este proyecto, BLE permite que un **navegador web se conecte directamente al robot** sin necesidad de instalar aplicaciones adicionales.

El proceso de comunicación ocurre de la siguiente manera:

1. El robot inicia un servicio BLE.
2. El navegador busca dispositivos BLE cercanos.
3. El usuario selecciona el robot.
4. La página web establece la conexión.
5. La interfaz envía comandos de movimiento.
6. El robot recibe los comandos y ejecuta la acción correspondiente.

Este método permite controlar el robot de forma sencilla desde distintos dispositivos.

---

# Interfaz web de control

La página se encuentra publicada mediante **GitHub Pages**, lo que permite acceder a ella desde cualquier navegador compatible.

### 🌐 Acceso a la interfaz

https://aggy2025.github.io/cenfobot-control/

No es necesario instalar ninguna aplicación.  
El control se realiza directamente desde el navegador.

---

# Compatibilidad con dispositivos

La interfaz fue diseñada para ser **responsive**, lo que significa que se adapta automáticamente al tamaño de la pantalla.

Esto permite controlar el robot desde distintos dispositivos.

| Dispositivo | Compatibilidad |
|-------------|---------------|
| Computadora (PC o laptop) | ✔ Compatible |
| Teléfono móvil | ✔ Compatible |
| Tablet | ✔ Compatible |

El control funciona en navegadores que soportan **Web Bluetooth**, como:

- Google Chrome  
- Microsoft Edge  
- Opera  

Actualmente **Safari no soporta Web Bluetooth**.

---

# Características de la interfaz

La página web incluye varios elementos para facilitar el control del robot.

Entre ellos:

- botones de dirección para controlar el movimiento
- control deslizante para ajustar la velocidad
- indicador de estado de conexión BLE
- registro de mensajes enviados al robot
- botón para limpiar el registro
- LED virtual que muestra el estado del robot

---

# Arquitectura del sistema

El sistema se compone de tres componentes principales.

### Robot Sumobot

- controla los motores
- lee el giroscopio
- aplica el control PDI
- recibe comandos BLE
- controla el LED NeoPixel

### Interfaz Web

- permite enviar comandos desde el navegador
- muestra indicadores visuales del estado del robot
- permite ajustar la velocidad
- registra los comandos enviados

### Comunicación BLE

- conecta la interfaz web con el robot
- transmite instrucciones de movimiento en tiempo real
- utiliza el servicio **BLE UART**
