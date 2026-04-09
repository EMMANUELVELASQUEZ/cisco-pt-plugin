#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║   Claude + Cisco Packet Tracer Plugin PRO            ║
║   Universidad Veracruzana - CCNA 2                   ║
║   Emmanuel Velasquez Geron - S23023048               ║
╚══════════════════════════════════════════════════════╝
"""

import subprocess
import sys
import os
import time
import shutil
from datetime import datetime

# ============================================================
# COLORES Y ESTILOS
# ============================================================
class C:
    NEGRO    = '\033[30m'
    ROJO     = '\033[91m'
    VERDE    = '\033[92m'
    AMARILLO = '\033[93m'
    AZUL     = '\033[94m'
    MAGENTA  = '\033[95m'
    CYAN     = '\033[96m'
    BLANCO   = '\033[97m'
    BOLD     = '\033[1m'
    DIM      = '\033[2m'
    SUBRAY   = '\033[4m'
    BG_AZUL  = '\033[44m'
    BG_VERDE = '\033[42m'
    BG_ROJO  = '\033[41m'
    BG_NEGRO = '\033[40m'
    RESET    = '\033[0m'

# ============================================================
# UTILIDADES DE TERMINAL
# ============================================================
def limpiar():
    os.system('clear')

def ancho():
    return shutil.get_terminal_size().columns

def centrar(texto, color=""):
    w = ancho()
    limpio = texto.replace('\033[0m','').replace('\033[1m','').replace('\033[92m','') \
                  .replace('\033[94m','').replace('\033[96m','').replace('\033[93m','') \
                  .replace('\033[95m','').replace('\033[91m','').replace('\033[97m','') \
                  .replace('\033[2m','').replace('\033[4m','').replace('\033[44m','') \
                  .replace('\033[42m','').replace('\033[40m','')
    espacios = max(0, (w - len(limpio)) // 2)
    print(color + " " * espacios + texto + C.RESET)

def linea(char="─", color=C.AZUL):
    print(color + char * ancho() + C.RESET)

def linea_doble(color=C.CYAN):
    print(color + "═" * ancho() + C.RESET)

def esperar(seg=0.03):
    time.sleep(seg)

def typing(texto, color=C.VERDE, delay=0.02):
    print(color, end="", flush=True)
    for c in texto:
        print(c, end="", flush=True)
        time.sleep(delay)
    print(C.RESET)

def barra_progreso(titulo, total=20):
    print(f"\n  {C.AMARILLO}{titulo}{C.RESET}")
    print("  [", end="", flush=True)
    for i in range(total):
        time.sleep(0.04)
        print(f"{C.VERDE}█{C.RESET}", end="", flush=True)
    print(f"] {C.VERDE}✓ Listo{C.RESET}\n")

# ============================================================
# BANNER PRINCIPAL
# ============================================================
def banner():
    limpiar()
    w = ancho()
    linea_doble(C.CYAN)
    print()
    centrar("╔═══════════════════════════════════════════════╗", C.CYAN + C.BOLD)
    centrar("║                                               ║", C.CYAN + C.BOLD)
    centrar("║     🌐  CISCO PACKET TRACER PLUGIN  🌐        ║", C.CYAN + C.BOLD)
    centrar("║                                               ║", C.CYAN + C.BOLD)
    centrar("║         Powered by Claude AI Logic            ║", C.MAGENTA + C.BOLD)
    centrar("║                                               ║", C.CYAN + C.BOLD)
    centrar("╚═══════════════════════════════════════════════╝", C.CYAN + C.BOLD)
    print()
    centrar("Universidad Veracruzana  │  CCNA 2", C.DIM)
    centrar("Emmanuel Velasquez Geron  │  S23023048", C.DIM)
    print()
    linea_doble(C.CYAN)
    print()

# ============================================================
# MENU PRINCIPAL
# ============================================================
def menu_principal():
    w = ancho()
    pad = max(0, (w - 52) // 2)
    sp = " " * pad

    print(f"\n{sp}{C.AZUL}{C.BOLD}┌─────────────────────────────────────────────────┐{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}          {C.BLANCO}{C.BOLD}⚡  MENU PRINCIPAL  ⚡{C.RESET}                  {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}├─────────────────────────────────────────────────┤{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}                                                 {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}   {C.VERDE}[1]{C.RESET}  🔒  Port Security                          {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}   {C.VERDE}[2]{C.RESET}  🔀  Configurar VLANs                       {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}   {C.VERDE}[3]{C.RESET}  🔐  Configurar SSH                         {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}   {C.VERDE}[4]{C.RESET}  🛡️   Configurar TACACS                      {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}   {C.VERDE}[5]{C.RESET}  📶  Seguridad Wireless WRT300N             {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}   {C.VERDE}[6]{C.RESET}  💻  Conexion SSH desde PC                  {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}                                                 {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}├─────────────────────────────────────────────────┤{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}   {C.ROJO}[7]{C.RESET}  ❌  Salir                                  {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}└─────────────────────────────────────────────────┘{C.RESET}\n")

# ============================================================
# INPUT ESTILIZADO
# ============================================================
def pedir(pregunta, default=""):
    hint = f" [{C.DIM}{default}{C.RESET}]" if default else ""
    val = input(f"  {C.CYAN}▶{C.RESET}  {pregunta}{hint}: ").strip()
    return val if val else default

def titulo_seccion(icono, nombre):
    limpiar()
    linea("═", C.CYAN)
    centrar(f"{icono}  {nombre}  {icono}", C.CYAN + C.BOLD)
    linea("═", C.CYAN)
    print()

def mostrar_comandos(titulo, cmds):
    limpiar()
    linea("═", C.VERDE)
    centrar(f"✅  COMANDOS GENERADOS: {titulo}", C.VERDE + C.BOLD)
    linea("═", C.VERDE)
    print()

    w = ancho()
    pad = max(0, (w - 60) // 2)
    sp = " " * pad

    print(f"{sp}{C.AZUL}┌{'─'*58}┐{C.RESET}")
    for linea_cmd in cmds.split('\n'):
        # Truncar si es muy larga
        visible = linea_cmd[:56] if len(linea_cmd) > 56 else linea_cmd
        espacios = 56 - len(visible)
        print(f"{sp}{C.AZUL}│{C.RESET} {C.VERDE}{visible}{C.RESET}{' ' * espacios} {C.AZUL}│{C.RESET}")
    print(f"{sp}{C.AZUL}└{'─'*58}┘{C.RESET}")
    print()

def resultado_final(path, copiado):
    linea("─", C.DIM)
    if copiado:
        print(f"\n  {C.BG_VERDE}{C.NEGRO}{C.BOLD}  ✅ COMANDOS COPIADOS AL PORTAPAPELES  {C.RESET}")
        print(f"\n  {C.AMARILLO}➡️  Ve a Packet Tracer → CLI → pega con {C.BOLD}Cmd+V{C.RESET}")
    print(f"\n  {C.CYAN}💾 Guardado en:{C.RESET}")
    print(f"  {C.DIM}{path}{C.RESET}\n")
    linea("─", C.DIM)

# ============================================================
# COPIAR Y GUARDAR
# ============================================================
CARPETA = os.path.expanduser("~/claude-pt-plugin/comandos")
os.makedirs(CARPETA, exist_ok=True)

def copiar(texto):
    try:
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.communicate(texto.encode('utf-8'))
        return True
    except:
        return False

def guardar(nombre, texto):
    ts = datetime.now().strftime("%H%M%S")
    path = f"{CARPETA}/{nombre}_{ts}.txt"
    with open(path, 'w') as f:
        f.write(f"# Plugin Claude PT PRO\n# {datetime.now().strftime('%Y-%m-%d %H:%M')}\n# {nombre}\n\n")
        f.write(texto)
    return path

def procesar(nombre, cmds):
    barra_progreso("Generando comandos...")
    mostrar_comandos(nombre, cmds)
    ok = copiar(cmds)
    path = guardar(nombre, cmds)
    resultado_final(path, ok)

# ============================================================
# 1. PORT SECURITY
# ============================================================
def port_security():
    titulo_seccion("🔒", "PORT SECURITY")

    print(f"  {C.AMARILLO}Configuracion del Switch:{C.RESET}\n")
    sw     = pedir("Nombre del switch", "SW1")
    print()
    print(f"  {C.AMARILLO}Puerto 1:{C.RESET}")
    fa1    = pedir("Puerto", "fa0/1")
    mac1   = pedir("Direccion MAC", "000A.F371.C91B")
    print()
    print(f"  {C.AMARILLO}Puerto 2:{C.RESET}")
    fa2    = pedir("Puerto", "fa0/2")
    mac2   = pedir("Direccion MAC", "0030.A34E.6B14")
    print()
    print(f"  {C.AMARILLO}Seguridad:{C.RESET}")
    modo   = pedir("Violation mode (shutdown/restrict/protect)", "shutdown")
    sticky = pedir("Activar sticky (s/n)", "s")
    aging  = pedir("Aging time en minutos", "10")
    print()
    print(f"  {C.AMARILLO}Puertos vacios:{C.RESET}")
    v_desde = pedir("Desde puerto", "fa0/3")
    v_hasta = pedir("Hasta puerto", "fa0/24")

    sticky_cmd = "\nswitchport port-security mac-address sticky" if sticky.lower() == 's' else ""

    cmds = f"""enable
configure terminal
hostname {sw}
banner motd #
==========================================
 ACCESO RESTRINGIDO - SOLO AUTORIZADO
 Universidad Veracruzana
==========================================
#
enable secret cisco123
line console 0
password cisco123
login
exit
line vty 0 4
password cisco123
login
exit
service password-encryption
interface {fa1}
description PC1-{mac1}
switchport mode access
switchport port-security
switchport port-security maximum 1
switchport port-security mac-address {mac1}
switchport port-security violation {modo}{sticky_cmd}
switchport port-security aging time {aging}
exit
interface {fa2}
description PC2-{mac2}
switchport mode access
switchport port-security
switchport port-security maximum 1
switchport port-security mac-address {mac2}
switchport port-security violation {modo}{sticky_cmd}
switchport port-security aging time {aging}
exit
interface range {v_desde} - {v_hasta}
description PUERTO-NO-USADO
shutdown
exit
exit
show port-security
show port-security address
write memory"""

    procesar(f"PortSecurity_{sw}", cmds)

# ============================================================
# 2. VLANs
# ============================================================
def vlans():
    titulo_seccion("🔀", "CONFIGURAR VLANs")

    sw = pedir("Nombre del switch", "SW1")
    print()

    print(f"  {C.AMARILLO}Ingresa las VLANs (Enter vacio para terminar):{C.RESET}\n")
    vlans_lista = []
    i = 1
    while True:
        vid = pedir(f"VLAN {i} - ID (ej: 10)", "")
        if not vid: break
        vnom    = pedir(f"VLAN {i} - Nombre", f"VLAN{vid}")
        vpuerto = pedir(f"VLAN {i} - Puerto", f"fa0/{i}")
        vlans_lista.append((vid, vnom, vpuerto))
        i += 1

    if not vlans_lista:
        vlans_lista = [("10","VENTAS","fa0/1"),("20","RRHH","fa0/2"),("30","TI","fa0/3")]

    trunk = pedir("Puerto trunk", "fa0/24")

    crear = ""
    for vid, vnom, _ in vlans_lista:
        crear += f"vlan {vid}\nname {vnom}\nexit\n"

    asignar = ""
    for vid, vnom, vp in vlans_lista:
        asignar += f"interface {vp}\ndescription {vnom}-VLAN{vid}\nswitchport mode access\nswitchport access vlan {vid}\nexit\n"

    cmds = f"""enable
configure terminal
hostname {sw}
{crear}{asignar}interface {trunk}
switchport mode trunk
exit
exit
show vlan brief
show interfaces trunk
write memory"""

    procesar(f"VLANs_{sw}", cmds)

# ============================================================
# 3. SSH
# ============================================================
def ssh():
    titulo_seccion("🔐", "CONFIGURAR SSH")

    print(f"  {C.AMARILLO}Datos del Switch:{C.RESET}\n")
    sw       = pedir("Nombre del switch", "SW1")
    ip       = pedir("IP del switch", "192.168.1.1")
    mascara  = pedir("Mascara", "255.255.255.0")
    gateway  = pedir("Gateway", "192.168.1.254")
    print()
    print(f"  {C.AMARILLO}Configuracion SSH:{C.RESET}\n")
    dominio  = pedir("Dominio", "universidad.edu")
    usuario  = pedir("Usuario", "admin")
    password = pedir("Password", "cisco123")

    cmds = f"""enable
configure terminal
hostname {sw}
ip domain-name {dominio}
username {usuario} privilege 15 secret {password}
interface vlan 1
ip address {ip} {mascara}
no shutdown
exit
ip default-gateway {gateway}
crypto key generate rsa
1024
ip ssh version 2
ip ssh time-out 60
ip ssh authentication-retries 3
line vty 0 4
transport input ssh
login local
exit
exit
show ip ssh
write memory"""

    procesar(f"SSH_{sw}", cmds)

    print(f"\n  {C.AMARILLO}📌 Para conectarte desde PC en PT:{C.RESET}")
    print(f"  {C.CYAN}  ssh -l {usuario} {ip}{C.RESET}")
    print(f"  {C.DIM}  Password: {password}{C.RESET}\n")

# ============================================================
# 4. TACACS
# ============================================================
def tacacs():
    titulo_seccion("🛡️", "CONFIGURAR TACACS")

    print(f"  {C.AMARILLO}Datos del Switch:{C.RESET}\n")
    sw          = pedir("Nombre del switch", "SW1")
    ip_sw       = pedir("IP del switch", "192.168.1.1")
    mascara     = pedir("Mascara", "255.255.255.0")
    print()
    print(f"  {C.AMARILLO}Servidor TACACS:{C.RESET}\n")
    ip_srv      = pedir("IP del servidor TACACS", "192.168.1.100")
    key         = pedir("Clave secreta TACACS", "cisco123")
    print()
    print(f"  {C.AMARILLO}Usuario local de respaldo:{C.RESET}\n")
    usuario     = pedir("Usuario", "admin")
    password    = pedir("Password", "cisco123")

    cmds = f"""enable
configure terminal
hostname {sw}
interface vlan 1
ip address {ip_sw} {mascara}
no shutdown
exit
username {usuario} privilege 15 secret {password}
aaa new-model
tacacs-server host {ip_srv}
tacacs-server key {key}
aaa authentication login default group tacacs+ local
line console 0
login authentication default
exit
line vty 0 4
login authentication default
exit
exit
show tacacs
write memory"""

    procesar(f"TACACS_{sw}", cmds)

    print(f"\n  {C.AMARILLO}📌 Configura el Servidor AAA en PT:{C.RESET}\n")
    pasos = [
        f"1. Doble clic Server → Services → AAA → ON",
        f"2. Network Config: Client={sw}, IP={ip_sw}, Secret={key}, Type=TACACS+ → Add",
        f"3. User Setup: Username={usuario}, Password={password} → Add",
    ]
    for p in pasos:
        print(f"   {C.CYAN}{p}{C.RESET}")
    print()

# ============================================================
# 5. WIRELESS
# ============================================================
def wireless():
    titulo_seccion("📶", "SEGURIDAD WIRELESS WRT300N")

    print(f"  {C.AMARILLO}Configuracion de la red WiFi:{C.RESET}\n")
    ssid      = pedir("Nombre SSID", "UV-Emmanuel")
    password  = pedir("Password WiFi", "UV2026secure")
    pw_router = pedir("Password del router", "UV2026")
    mac_lap   = pedir("MAC de la Laptop", "0001.635A.6994")

    limpiar()
    linea("═", C.CYAN)
    centrar("📶  PASOS EN PACKET TRACER  📶", C.CYAN + C.BOLD)
    linea("═", C.CYAN)

    w = ancho()
    pad = max(0, (w - 56) // 2)
    sp = " " * pad

    pasos = [
        ("1", "Administration → Management",
         [f"Router Password: {pw_router}", "Remote Management: Disabled", "→ Save Settings"]),
        ("2", "Wireless → Basic Wireless Settings",
         [f"SSID: {ssid}", "SSID Broadcast: Disabled", "→ Save Settings"]),
        ("3", "Security → Firewall",
         ["Enable SPI Firewall: ON", "→ Save Settings"]),
        ("4", "Wireless → Wireless Security",
         ["Security Mode: WPA2 Personal", "Encryption: AES",
          f"Passphrase: {password}", "→ Save Settings"]),
        ("5", "Wireless → Wireless MAC Filter",
         ["Enable: ON", "Permit PCs listed below",
          f"MAC 01: {mac_lap}", "→ Save Settings"]),
        ("6", "Conectar Laptop",
         ["Instalar tarjeta WPC300N",
          "Desktop → PC Wireless → Connect",
          f"Red: {ssid}",
          f"Pre-Shared Key: {password}"]),
    ]

    print()
    for num, titulo_paso, detalles in pasos:
        print(f"{sp}{C.VERDE}{C.BOLD}  [{num}] {titulo_paso}{C.RESET}")
        for d in detalles:
            print(f"{sp}      {C.CYAN}• {d}{C.RESET}")
        print()

    linea("─", C.DIM)

    texto = f"WIRELESS WRT300N\nSSID: {ssid}\nPassword: {password}\nRouter Password: {pw_router}\nMAC Laptop: {mac_lap}"
    copiar(texto)
    path = guardar("Wireless_WRT300N", texto)
    print(f"\n  {C.VERDE}✅ Info copiada al portapapeles{C.RESET}")
    print(f"  {C.CYAN}💾 {path}{C.RESET}\n")

# ============================================================
# 6. CONEXION SSH DESDE PC
# ============================================================
def conectar_ssh():
    titulo_seccion("💻", "CONEXION SSH DESDE PC")

    usuario = pedir("Usuario SSH", "admin")
    ip      = pedir("IP del switch", "192.168.1.1")

    cmd = f"ssh -l {usuario} {ip}"

    limpiar()
    linea("═", C.VERDE)
    centrar("💻  CONEXION SSH DESDE PC  💻", C.VERDE + C.BOLD)
    linea("═", C.VERDE)

    print(f"""
  {C.AMARILLO}Pasos en Packet Tracer:{C.RESET}

  {C.VERDE}1.{C.RESET} Doble clic en la {C.BOLD}PC{C.RESET}
  {C.VERDE}2.{C.RESET} Desktop → {C.BOLD}Command Prompt{C.RESET}
  {C.VERDE}3.{C.RESET} Escribe el siguiente comando:
""")

    w = ancho()
    pad = max(0, (w - 50) // 2)
    sp = " " * pad
    print(f"{sp}{C.BG_NEGRO}{C.VERDE}{C.BOLD}  $ {cmd}  {C.RESET}\n")

    print(f"  {C.VERDE}4.{C.RESET} Cuando pida password escribe tu contrasena")
    print(f"  {C.VERDE}5.{C.RESET} Verifica con: {C.CYAN}show ip ssh{C.RESET}\n")

    linea("─", C.DIM)
    copiar(cmd)
    path = guardar("ConexionSSH", cmd)
    print(f"\n  {C.VERDE}✅ Comando copiado al portapapeles{C.RESET}")
    print(f"  {C.CYAN}💾 {path}{C.RESET}\n")

# ============================================================
# MAIN
# ============================================================
def main():
    banner()

    # Animacion de inicio
    barra_progreso("Iniciando plugin...", 15)

    print(f"  {C.VERDE}✅ Plugin listo{C.RESET}")
    print(f"  {C.CYAN}💾 Comandos se guardan en: {CARPETA}{C.RESET}\n")
    time.sleep(1)

    opciones = {
        '1': port_security,
        '2': vlans,
        '3': ssh,
        '4': tacacs,
        '5': wireless,
        '6': conectar_ssh,
    }

    while True:
        limpiar()
        banner()
        menu_principal()

        # Hora actual
        hora = datetime.now().strftime("%H:%M:%S")
        print(f"  {C.DIM}⏰ {hora}  │  📁 {CARPETA}{C.RESET}\n")

        op = input(f"  {C.CYAN}{C.BOLD}▶  Selecciona una opcion: {C.RESET}").strip()

        if op == '7':
            limpiar()
            linea_doble(C.CYAN)
            centrar("👋  ¡Hasta luego!", C.VERDE + C.BOLD)
            centrar("🔥  ¡Buena suerte en el examen!", C.AMARILLO + C.BOLD)
            linea_doble(C.CYAN)
            print()
            sys.exit(0)
        elif op in opciones:
            opciones[op]()
        else:
            print(f"\n  {C.BG_ROJO}{C.BLANCO}  ❌ Opcion no valida  {C.RESET}\n")
            time.sleep(1)
            continue

        input(f"\n  {C.DIM}Presiona Enter para volver al menu...{C.RESET}")

if __name__ == "__main__":
    main()
