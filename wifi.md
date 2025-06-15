
# Control Remoto SumoBot - IdeaBoard ESP32

Este proyecto básico demuestra cómo utilizar una placa **IdeaBoard con ESP32** y CircuitPython para controlar un robot SumoBot mediante una interfaz web alojada directamente en el dispositivo.

---

## 1. Archivos principales del proyecto

- `wifiApp.py`: Contiene toda la lógica de conexión Wi-Fi, control de motores y servidor web embebido.
- `buscar_ip_sumobot.py`: Utilidad que se ejecuta en tu computadora (por ejemplo, con Visual Studio Code) para encontrar la dirección IP del SumoBot en tu red local.

---

## 2. Instalación de los archivos en la placa IdeaBoard

### Subir el archivo principal

1. Abre Thonny y asegúrate de que tu IdeaBoard esté conectada.
2. Carga el archivo `wifiApp.py` en la raíz del dispositivo.
3. En el archivo `code.py` (también en la raíz de la placa), agrega la siguiente línea para importar el módulo de control:

```python
import wifiApp
```

> Esto hará que se inicie automáticamente el servidor web del SumoBot al encender la placa.

---

## 3. Instalación de la librería necesaria

Este proyecto requiere la librería `adafruit_httpserver`, que no viene incluida por defecto.

### Paso 1: Descargar el paquete de librerías

Descarga el bundle oficial de Adafruit para CircuitPython desde el siguiente enlace:

🔗 [Descargar Adafruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20250614/adafruit-circuitpython-bundle-9.x-mpy-20250614.zip)

### Paso 2: Copiar la librería a la placa

1. Extrae el archivo ZIP descargado.
2. Ubica la carpeta `adafruit_httpserver` dentro del directorio `lib` extraído.
3. En Thonny:
   - Abre el **Explorador de archivos**.
   - En la **parte superior izquierda**, navega en tu PC hasta la carpeta `adafruit_httpserver`.
   - En la **parte inferior izquierda**, entra a la carpeta `/lib` de la IdeaBoard.
   - Haz clic derecho sobre la carpeta `adafruit_httpserver` (en tu PC) y selecciona la opción **Upload to /lib**.

---

## 4. Uso de `buscar_ip_sumobot.py`

Para encontrar rápidamente la URL del panel de control del SumoBot en tu red local:

1. Ejecuta el script `buscar_ip_sumobot.py` desde tu PC.
2. El script escaneará tu red doméstica en busca de dispositivos que estén sirviendo contenido en el puerto **80** (puerto por defecto del servidor web del robot).

### Salida esperada:

```bash
Escaneando red 192.168.1.0/24 buscando dispositivos con puerto 80 abierto...
Dispositivos con puerto abierto encontrados:
http://192.168.1.87:80
```

Haz clic sobre esa URL para abrir directamente el panel de control web del robot.

---

## 5. Variables de entorno para conexión Wi-Fi

El archivo `wifiApp.py` utiliza dos variables críticas para conectarse a la red Wi-Fi:

```python
ssid = os.getenv("CIRCUITPY_WIFI_SSID")
password = os.getenv("CIRCUITPY_WIFI_PASSWORD")
```

### ¿Qué hacen?

- `CIRCUITPY_WIFI_SSID`: Define el nombre de tu red Wi-Fi.
- `CIRCUITPY_WIFI_PASSWORD`: Define la contraseña de tu red.

### ¿Dónde se configuran?

En el archivo `settings.toml`, ubicado en la raíz del dispositivo:

```toml
CIRCUITPY_WIFI_SSID = "NombreDeTuRedWiFi"
CIRCUITPY_WIFI_PASSWORD = "TuContraseñaWiFi"
```

⚠️ **Nota**: Este archivo debe crearse con cuidado y no debe compartirse públicamente.

---

## 6. ¿Qué demuestra este proyecto?

Este es un ejercicio introductorio para mostrar las capacidades de la placa **IdeaBoard con ESP32**:

- Conexión automática a redes Wi-Fi.
- Servidor web embebido con controles de movimiento del robot.
- Interfaz futurista y responsiva desde cualquier navegador.
- Posibilidad de expandirse para consumir **APIs externas** (por ejemplo, clima, sensores remotos, dashboards) y mostrar datos en tiempo real.

¡Una poderosa demostración de cómo tu IdeaBoard puede interactuar con el mundo a través de la red local! 🌐🤖
