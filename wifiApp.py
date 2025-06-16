import os
import time
import wifi
import socketpool
from adafruit_httpserver import Server, Request, Response
from ideaboard import IdeaBoard

DIRECCIONES_VALIDAS = ["adelante", "atras", "izquierda", "derecha", "alto"]

ib = IdeaBoard()

def log_error(mensaje):
    """Guardar mensaje de error en error.out con timestamp."""
    try:
        with open("error.out", "a") as f:          
            f.write(f"{mensaje}\n")
    except Exception as e:
        print("Error log_error:", e)
        # En caso de error al escribir el log, imprimir en consola
        pass 

# Conexión Wi-Fi segura con manejo de errores
try:
    ssid = os.getenv("CIRCUITPY_WIFI_SSID")
    password = os.getenv("CIRCUITPY_WIFI_PASSWORD")
    wifi.radio.connect(ssid, password)
    print("Conectado a Wi-Fi:", ssid)
except Exception as e:
    print("Error al conectar a Wi-Fi:", e)
    log_error(f"Error al conectar a Wi-Fi: {e}")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

def detener():
    """Detiene los motores."""
    try:
        ib.motor_1.throttle = 0
        ib.motor_2.throttle = 0
    except Exception as e:
        print("Error en detener:", e)
        log_error(f"Error en detener(): {e}")

def mover(direccion, duracion=1):
    """Ejecuta movimiento según la dirección especificada y duración."""
    try:
        detener()
        if direccion == "adelante":
            ib.motor_1.throttle = 1.0
            ib.motor_2.throttle = 1.0
        elif direccion == "atras":
            ib.motor_1.throttle = -1.0
            ib.motor_2.throttle = -1.0
        elif direccion == "izquierda":
            ib.motor_1.throttle = -0.5
            ib.motor_2.throttle = 0.5
        elif direccion == "derecha":
            ib.motor_1.throttle = 0.5
            ib.motor_2.throttle = -0.5
        elif direccion == "alto":
            detener()
            return
        time.sleep(duracion)
        detener()
    except Exception as e:
        print("Error en mover:", e)
        log_error(f"Error en mover(direccion={direccion}, duracion={duracion}): {e}")

@server.route("/")
def controlar_robot(request: Request):
    """Controla el robot según parámetros 'direccion' y 'duracion' recibidos en la URL."""
    try:
        direccion = request.query_params.get("direccion", "").lower()
        duracion_raw = request.query_params.get("duracion", "1")

        # Validar duración
        try:
            duracion = float(duracion_raw)
            if duracion <= 0 or duracion > 10:
                duracion = 1
        except ValueError:
            duracion = 1

        if direccion in DIRECCIONES_VALIDAS:
            mover(direccion, duracion)
            mensaje = f"Moviendo: {direccion.upper()} durante {duracion:.1f} segundos"
        else:
            detener()
            mensaje = f"Dirección no válida: {direccion}"

        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Control Sumobot</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&display=swap');
                body {{
                    background: linear-gradient(to bottom, #0f0f0f, #1f1f1f);
                    color: #00ffe5;
                    font-family: 'Orbitron', sans-serif;
                    text-align: center;
                    padding: 20px;
                    margin: 0;
                }}
                h1 {{
                    font-size: 28px;
                    margin-bottom: 10px;
                    text-shadow: 0 0 10px #00ffe5;
                }}
                .mensaje {{
                    font-size: 18px;
                    margin-bottom: 30px;
                    color: #80ffd9;
                    text-shadow: 0 0 5px #00ffc3;
                }}
                .control {{
                    display: grid;
                    grid-template-columns: 1fr 1fr 1fr;
                    grid-template-rows: auto auto auto;
                    gap: 15px;
                    justify-items: center;
                    max-width: 360px;
                    margin: auto;
                }}
                button {{
                    width: 100px;
                    height: 60px;
                    border: 2px solid #00ffc3;
                    border-radius: 12px;
                    background: rgba(0, 255, 195, 0.1);
                    color: #00ffe5;
                    font-size: 16px;
                    text-shadow: 0 0 5px #00ffe5;
                    box-shadow: 0 0 12px #00ffc3;
                    cursor: pointer;
                    transition: all 0.25s ease-in-out;
                }}
                button:hover {{
                    background: #00ffc3;
                    color: #000;
                    box-shadow: 0 0 20px #00ffe5, 0 0 40px #00ffc3;
                }}
                .top    {{ grid-column: 2; }}
                .left   {{ grid-column: 1; }}
                .center {{ grid-column: 2; }}
                .right  {{ grid-column: 3; }}
                .bottom {{ grid-column: 2; }}

                /* Barra de progreso */
                .progress-container {{
                    width: 80%;
                    background-color: #333;
                    border-radius: 10px;
                    margin: 20px auto;
                    height: 20px;
                    overflow: hidden;
                    box-shadow: 0 0 10px #00ffc3;
                }}
                .progress-bar {{
                    height: 100%;
                    background: linear-gradient(to right, #00ffe5, #00ff88);
                    width: 0%;
                    transition: width linear;
                }}

                /* Responsive */
                @media (max-width: 400px) {{
                    .control {{
                        max-width: 300px;
                        grid-template-columns: 1fr 1fr 1fr;
                    }}
                    button {{
                        width: 80px;
                        height: 50px;
                        font-size: 14px;
                    }}
                }}
            </style>
        </head>
        <body>
            <h1>🎮 Panel de Control</h1>
            <p class="mensaje">{mensaje}</p>

            <div class="progress-container">
                <div class="progress-bar" id="barra"></div>
            </div>

            <form method="get">
                <div class="control">
                    <button class="top"    name="direccion" value="adelante">⬆ Adelante</button>
                    <button class="left"   name="direccion" value="izquierda">⬅ Izquierda</button>
                    <button class="center" name="direccion" value="alto">⏹ Alto</button>
                    <button class="right"  name="direccion" value="derecha">➡ Derecha</button>
                    <button class="bottom" name="direccion" value="atras">⬇ Atrás</button>
                </div>
                <br />
                <label for="duracion">Duración (segundos): </label>
                <input 
                    type="number" 
                    id="duracion" 
                    name="duracion" 
                    min="0.1" max="10" step="0.1" 
                    value="{duracion}"
                    style="width: 70px; text-align:center;"
                    required
                />
            </form>

            <script>
                const duracion = {duracion};
                const barra = document.getElementById("barra");
                if (barra) {{
                    barra.style.transitionDuration = duracion + "s";
                    setTimeout(() => {{
                        barra.style.width = "100%";
                    }}, 100);
                }}
            </script>
        </body>
        </html>
        """
        return Response(request, html, content_type="text/html")

    except Exception as e:
        error_msg = f"Error en controlar_robot: {e}"
        print(error_msg)
        log_error(error_msg)
        return Response(request, "Error interno del servidor", status=500)

try:
    server.start(str(wifi.radio.ipv4_address), port=80)
    print("🌐 Servidor en marcha en", wifi.radio.ipv4_address)
except Exception as e:
    print("Error iniciando servidor:", e)
    log_error(f"Error iniciando servidor: {e}")

while True:
    try:
        server.poll()
    except Exception as e:
        print("⚠️ Error en el servidor:", e)
        log_error(f"Error en el servidor: {e}")
