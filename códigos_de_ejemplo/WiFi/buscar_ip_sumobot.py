import socket
import ipaddress
import concurrent.futures
import sys

def obtener_red_local():
    """
    Obtiene la red local en formato CIDR basada en la IP local activa.
    
    Intenta obtener la IP local conectando a 8.8.8.8 UDP (sin enviar datos).
    Asume máscara /24 (común en redes domésticas).
    
    Returns:
        str: Red local en formato CIDR, por ejemplo "192.168.1.0/24".
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
    except Exception:
        print("No se pudo determinar la IP local, usa un rango de red manual.")
        sys.exit(1)
    finally:
        s.close()

    red_cidr = ip_local.rsplit('.', 1)[0] + ".0/24"
    return red_cidr

def check_port(ip, port=5000, timeout=0.5):
    """
    Intenta conectar al puerto TCP especificado en la IP dada.
    
    Args:
        ip (str or ipaddress.IPv4Address): Dirección IP a escanear.
        port (int): Puerto TCP a verificar.
        timeout (float): Tiempo máximo de espera en segundos.
    
    Returns:
        bool: True si el puerto está abierto (acepta conexiones), False si no.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((str(ip), port))
            return result == 0
    except:
        return False

def scan_network(network_cidr, port=80):
    """
    Escanea la red IP especificada buscando hosts con el puerto abierto.
    
    Args:
        network_cidr (str): Red en formato CIDR, por ejemplo "192.168.1.0/24".
        port (int): Puerto a escanear.
    
    Returns:
        list[str]: Lista de direcciones IP (str) con el puerto abierto.
    """
    active_ips = []
    net = ipaddress.ip_network(network_cidr, strict=False)
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(check_port, ip, port): ip for ip in net.hosts()}
        for future in concurrent.futures.as_completed(futures):
            ip = futures[future]
            if future.result():
                active_ips.append(str(ip))
    return active_ips

if __name__ == "__main__":
    red = obtener_red_local()
    puerto = 80
    print(f"Escaneando red {red} buscando dispositivos con puerto {puerto} abierto...")
    ips = scan_network(red, puerto)
    if ips:
        print("Dispositivos con puerto abierto encontrados:")
        for ip in ips:
            print(f"http://{ip}:{puerto}")
    else:
        print(f"No se encontraron dispositivos con puerto {puerto} abierto en la red.")
