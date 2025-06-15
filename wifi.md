# Control Wi-Fi para SumoBot con CircuitPython y ESP32
**Autor:** Javier Ortiz – CTP Escazú 
**Fecha de documento:** 14/06/25 

# Control Remoto SumoBot - IdeaBoard ESP32

Este proyecto básico demuestra cómo utilizar una placa **IdeaBoard con ESP32** y CircuitPython para controlar un robot SumoBot mediante una interfaz web alojada directamente en el dispositivo.

## 1. Archivos principales del proyecto

- `wifiApp.py`: Controla la conexión Wi-Fi y la interfaz web de control remoto del robot.
- `buscar_ip_sumobot.py`: Ejecutable desde tu computadora con Visual Studio Code para detectar la dirección IP del SumoBot en la red local.

## 2. Requisitos previos

- Placa **IdeaBoard ESP32** con CircuitPython instalado.
- Archivos del proyecto cargados en la placa.
- Acceso a red Wi-Fi 2.4 GHz.

## 3. Instalación de librerías

Para poder ejecutar este proyecto correctamente, debes instalar la siguiente librería adicional en la carpeta `/lib` de tu IdeaBoard:

### Paso 1: Descargar el paquete de librerías

Descarga el paquete oficial desde este enlace:

🔗 [Descargar Adafruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20250614/adafruit-circuitpython-bundle-9.x-mpy-20250614.zip)

### Paso 2: Copiar la librería requerida

Del contenido descargado, ubica y **sube a la placa** la carpeta:

- `adafruit_httpserver`

Puedes hacerlo desde Visual Studio Code con la extensión para CircuitPython, tal como se muestra en la imagen:

![Subir librerías a lib](attachment:65ecabfb-3a8a-4363-a6b4-669597547899.png)

## 4. Ejecutar el escáner IP

Desde tu computadora, puedes ejecutar el script `buscar_ip_sumobot.py` en Visual Studio Code para encontrar automáticamente la URL de control del SumoBot. El script buscará dispositivos conectados en tu red que estén sirviendo en el puerto **80**.

### Ejemplo de salida esperada:

```
http://192.168.1.87:80
```

Puedes hacer clic directamente en ese enlace desde la terminal para abrir el panel de control del robot.

## 5. ¿Qué hace este proyecto?

Este es un ejercicio básico para demostrar las capacidades del entorno CircuitPython en la **IdeaBoard**:

- Conexión a Wi-Fi con seguridad.
- Servidor web embebido para recibir comandos como:
  - adelante, atrás, izquierda, derecha, alto.
- Interfaz web con estilo futurista.
- Interacción desde cualquier navegador.

Además, este tipo de servidor es capaz de:

- **Consumir APIs externas** (como APIs de clima, sensores, etc.).
- **Mostrar datos en tiempo real**.
- **Servir archivos estáticos o dashboards** simples.

## 6. Variables de entorno para conexión Wi-Fi

Para conectarse a una red inalámbrica, se utilizan dos variables fundamentales:

```python
ssid = os.getenv("CIRCUITPY_WIFI_SSID")
password = os.getenv("CIRCUITPY_WIFI_PASSWORD")
```

### ¿Qué hacen?

- **`CIRCUITPY_WIFI_SSID`**: El nombre de la red Wi-Fi a la que se desea conectar la placa.
- **`CIRCUITPY_WIFI_PASSWORD`**: La contraseña de dicha red.

### ¿Dónde se configuran?

En el archivo `settings.toml` en la raíz del dispositivo, con el siguiente contenido:

```toml
CIRCUITPY_WIFI_SSID = "NombreDeTuRed"
CIRCUITPY_WIFI_PASSWORD = "TuContraseñaWiFi"
```

> ⚠️ No compartas este archivo públicamente si contiene credenciales reales.
