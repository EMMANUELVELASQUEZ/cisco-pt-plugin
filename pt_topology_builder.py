#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║   Cisco PT Topology Builder PRO                      ║
║   Universidad Veracruzana - CCNA 2                   ║
║   Emmanuel Velasquez Geron - S23023048               ║
╚══════════════════════════════════════════════════════╝
Genera comandos completos para toda una topologia
y los copia automaticamente al portapapeles
"""

import subprocess
import sys
import os
import time
import shutil
from datetime import datetime

class C:
    ROJO     = '\033[91m'
    VERDE    = '\033[92m'
    AMARILLO = '\033[93m'
    AZUL     = '\033[94m'
    MAGENTA  = '\033[95m'
    CYAN     = '\033[96m'
    BLANCO   = '\033[97m'
    BOLD     = '\033[1m'
    DIM      = '\033[2m'
    BG_AZUL  = '\033[44m'
    BG_VERDE = '\033[42m'
    BG_NEGRO = '\033[40m'
    RESET    = '\033[0m'

CARPETA = os.path.expanduser("~/claude-pt-plugin/topologias")
os.makedirs(CARPETA, exist_ok=True)

def limpiar():
    os.system('clear')

def w():
    return shutil.get_terminal_size().columns

def linea(char="═", color=C.CYAN):
    print(color + char * w() + C.RESET)

def centrar(texto, color=""):
    limpio = ''.join(c for c in texto if ord(c) > 31 or c == ' ')
    # Remove ANSI codes for length calculation
    import re
    ansi = re.compile(r'\033\[[0-9;]*m')
    limpio_sin_ansi = ansi.sub('', texto)
    espacios = max(0, (w() - len(limpio_sin_ansi)) // 2)
    print(color + " " * espacios + texto + C.RESET)

def copiar(texto):
    try:
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.communicate(texto.encode('utf-8'))
        return True
    except:
        return False

def guardar(nombre, texto):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{CARPETA}/{nombre}_{ts}.txt"
    with open(path, 'w') as f:
        f.write(f"# PT Topology Builder PRO\n")
        f.write(f"# {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"# Emmanuel Velasquez Geron - S23023048\n\n")
        f.write(texto)
    return path

def pedir(pregunta, default=""):
    hint = f" {C.DIM}[{default}]{C.RESET}" if default else ""
    val = input(f"  {C.CYAN}▶{C.RESET}  {pregunta}{hint}: ").strip()
    return val if val else default

def barra(titulo, total=20):
    print(f"\n  {C.AMARILLO}{titulo}{C.RESET}")
    print(f"  {C.DIM}[{C.RESET}", end="", flush=True)
    for i in range(total):
        time.sleep(0.03)
        print(f"{C.VERDE}█{C.RESET}", end="", flush=True)
    print(f"{C.DIM}]{C.RESET} {C.VERDE}✓{C.RESET}\n")

def banner():
    limpiar()
    linea()
    print()
    centrar("╔═══════════════════════════════════════════════════════╗", C.CYAN + C.BOLD)
    centrar("║                                                       ║", C.CYAN + C.BOLD)
    centrar("║      🏗️   PT TOPOLOGY BUILDER PRO   🏗️                ║", C.CYAN + C.BOLD)
    centrar("║                                                       ║", C.CYAN + C.BOLD)
    centrar("║   Construye topologias completas automaticamente      ║", C.DIM)
    centrar("║   Universidad Veracruzana  •  CCNA 2                  ║", C.DIM)
    centrar("║   Emmanuel Velasquez Geron  •  S23023048              ║", C.DIM)
    centrar("║                                                       ║", C.CYAN + C.BOLD)
    centrar("╚═══════════════════════════════════════════════════════╝", C.CYAN + C.BOLD)
    print()
    linea()
    print()

def menu():
    pad = max(0, (w() - 54) // 2)
    sp = " " * pad
    print(f"\n{sp}{C.AZUL}{C.BOLD}┌───────────────────────────────────────────────────┐{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}        {C.BLANCO}{C.BOLD}⚡  ELIGE TU TOPOLOGIA  ⚡{C.RESET}              {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}├───────────────────────────────────────────────────┤{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}                                                   {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.VERDE}[1]{C.RESET}  🔒  Port Security completo              {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.VERDE}[2]{C.RESET}  🔀  VLANs completo                      {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.VERDE}[3]{C.RESET}  🔐  SSH completo                        {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.VERDE}[4]{C.RESET}  🛡️   TACACS completo                     {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.VERDE}[5]{C.RESET}  📶  Wireless completo                   {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.VERDE}[6]{C.RESET}  🏆  TOPOLOGIA COMPLETA DEL EXAMEN       {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.VERDE}[7]{C.RESET}  ⚙️   Topologia personalizada             {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}                                                   {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}├───────────────────────────────────────────────────┤{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}│{C.RESET}  {C.ROJO}[8]{C.RESET}  ❌  Salir                               {C.AZUL}{C.BOLD}│{C.RESET}")
    print(f"{sp}{C.AZUL}{C.BOLD}└───────────────────────────────────────────────────┘{C.RESET}\n")

def mostrar_resultado(titulo, secciones):
    """Muestra los comandos generados por secciones"""
    limpiar()
    linea("═", C.VERDE)
    centrar(f"✅  {titulo}", C.VERDE + C.BOLD)
    linea("═", C.VERDE)
    print()

    todo = ""
    for nombre_sec, cmds in secciones:
        pad = max(0, (w() - 60) // 2)
        sp = " " * pad
        print(f"{sp}{C.AMARILLO}{C.BOLD}▶ {nombre_sec}{C.RESET}")
        print(f"{sp}{C.AZUL}{'─'*58}{C.RESET}")
        for linea_cmd in cmds.split('\n')[:8]:
            vis = linea_cmd[:56] if len(linea_cmd) > 56 else linea_cmd
            print(f"{sp}{C.VERDE}{vis}{C.RESET}")
        print(f"{sp}{C.DIM}... ({cmds.count(chr(10))+1} comandos totales){C.RESET}")
        print()
        todo += f"\n{'='*50}\n{nombre_sec}\n{'='*50}\n{cmds}\n"

    return todo

def finalizar(nombre, todo):
    linea("─", C.DIM)
    ok = copiar(todo)
    path = guardar(nombre, todo)
    print()
    if ok:
        print(f"  {C.BG_VERDE}{C.BOLD}  ✅ TODOS LOS COMANDOS COPIADOS AL PORTAPAPELES  {C.RESET}")
        print(f"\n  {C.AMARILLO}➡️  Ve a PT → CLI de cada switch → pega con {C.BOLD}Cmd+V{C.RESET}")
    print(f"\n  {C.CYAN}💾 Guardado en: {path}{C.RESET}\n")
    linea("─", C.DIM)

# ============================================================
# GENERADORES DE COMANDOS
# ============================================================

def gen_port_security(sw, puertos_macs, modo, aging, vacios):
    """Genera comandos completos de Port Security"""
    cmds = f"""enable
configure terminal
hostname {sw}
banner motd #
==========================================
 ACCESO RESTRINGIDO - SOLO AUTORIZADO
 Universidad Veracruzana - UV
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
service password-encryption"""

    for puerto, mac in puertos_macs:
        cmds += f"""
interface {puerto}
 description PC-{mac}
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address {mac}
 switchport port-security violation {modo}
 switchport port-security mac-address sticky
 switchport port-security aging time {aging}
 exit"""

    cmds += f"""
interface range {vacios}
 description PUERTO-NO-USADO
 shutdown
 exit
exit
show port-security
show port-security address
write memory"""
    return cmds

def gen_vlans(sw, vlans, trunk):
    """Genera comandos completos de VLANs"""
    cmds = f"enable\nconfigure terminal\nhostname {sw}\n"
    for vid, vnom, _ in vlans:
        cmds += f"vlan {vid}\n name {vnom}\n exit\n"
    for vid, vnom, vpuerto in vlans:
        cmds += f"interface {vpuerto}\n description {vnom}-VLAN{vid}\n switchport mode access\n switchport access vlan {vid}\n exit\n"
    cmds += f"interface {trunk}\n switchport mode trunk\n exit\nexit\nshow vlan brief\nshow interfaces trunk\nwrite memory"
    return cmds

def gen_ssh(sw, ip, mask, gw, dom, user, passwd):
    """Genera comandos completos de SSH"""
    return f"""enable
configure terminal
hostname {sw}
ip domain-name {dom}
username {user} privilege 15 secret {passwd}
interface vlan 1
 ip address {ip} {mask}
 no shutdown
 exit
ip default-gateway {gw}
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

def gen_tacacs(sw, ip_sw, mask, ip_srv, key, user, passwd):
    """Genera comandos completos de TACACS"""
    return f"""enable
configure terminal
hostname {sw}
interface vlan 1
 ip address {ip_sw} {mask}
 no shutdown
 exit
username {user} privilege 15 secret {passwd}
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

# ============================================================
# TOPOLOGIAS
# ============================================================

def topologia_port_security():
    limpiar()
    linea("═", C.CYAN)
    centrar("🔒  PORT SECURITY COMPLETO", C.CYAN + C.BOLD)
    linea("═", C.CYAN)
    print()
    print(f"  {C.AMARILLO}Configura SW1:{C.RESET}\n")

    sw    = pedir("Nombre del switch", "SW1")
    n_pcs = int(pedir("Numero de PCs", "2"))

    puertos_macs = []
    for i in range(n_pcs):
        print(f"\n  {C.DIM}PC{i+1}:{C.RESET}")
        puerto = pedir(f"Puerto", f"fa0/{i+1}")
        mac    = pedir(f"MAC", f"000A.F371.C9{i+1:02d}")
        puertos_macs.append((puerto, mac))

    print()
    modo   = pedir("Violation mode", "shutdown")
    aging  = pedir("Aging time", "10")
    vacios = pedir("Puertos vacios (rango)", f"fa0/{n_pcs+1}-24")

    barra("Generando topologia Port Security...")

    cmds = gen_port_security(sw, puertos_macs, modo, aging, vacios)
    todo = mostrar_resultado("PORT SECURITY", [(f"Configuracion {sw}", cmds)])
    finalizar(f"PortSecurity_{sw}", todo)

def topologia_vlans():
    limpiar()
    linea("═", C.CYAN)
    centrar("🔀  VLANs COMPLETO", C.CYAN + C.BOLD)
    linea("═", C.CYAN)
    print()

    sw    = pedir("Nombre del switch", "SW1")
    n_vl  = int(pedir("Numero de VLANs", "3"))

    vlans = []
    for i in range(n_vl):
        print(f"\n  {C.DIM}VLAN {i+1}:{C.RESET}")
        vid    = pedir("ID", str((i+1)*10))
        vnom   = pedir("Nombre", ["VENTAS","RRHH","TI"][i] if i < 3 else f"VLAN{i+1}")
        vpuerto= pedir("Puerto", f"fa0/{i+1}")
        vlans.append((vid, vnom, vpuerto))

    trunk = pedir("\nPuerto trunk", "fa0/24")

    barra("Generando topologia VLANs...")

    cmds = gen_vlans(sw, vlans, trunk)
    todo = mostrar_resultado("VLANs", [(f"Configuracion {sw}", cmds)])
    finalizar(f"VLANs_{sw}", todo)

def topologia_ssh():
    limpiar()
    linea("═", C.CYAN)
    centrar("🔐  SSH COMPLETO", C.CYAN + C.BOLD)
    linea("═", C.CYAN)
    print()

    sw     = pedir("Nombre del switch", "SW1")
    ip     = pedir("IP del switch", "192.168.1.1")
    mask   = pedir("Mascara", "255.255.255.0")
    gw     = pedir("Gateway", "192.168.1.254")
    dom    = pedir("Dominio", "universidad.edu")
    user   = pedir("Usuario SSH", "admin")
    passwd = pedir("Password", "cisco123")

    barra("Generando topologia SSH...")

    cmds = gen_ssh(sw, ip, mask, gw, dom, user, passwd)
    todo = mostrar_resultado("SSH", [(f"Configuracion {sw}", cmds)])

    print(f"\n  {C.AMARILLO}📌 Conexion desde PC:{C.RESET}")
    print(f"  {C.CYAN}  ssh -l {user} {ip}{C.RESET}\n")

    finalizar(f"SSH_{sw}", todo)

def topologia_tacacs():
    limpiar()
    linea("═", C.CYAN)
    centrar("🛡️  TACACS COMPLETO", C.CYAN + C.BOLD)
    linea("═", C.CYAN)
    print()

    sw     = pedir("Nombre del switch", "SW1")
    ip_sw  = pedir("IP del switch", "192.168.1.1")
    mask   = pedir("Mascara", "255.255.255.0")
    ip_srv = pedir("IP servidor TACACS", "192.168.1.100")
    key    = pedir("Clave TACACS", "cisco123")
    user   = pedir("Usuario local", "admin")
    passwd = pedir("Password local", "cisco123")

    barra("Generando topologia TACACS...")

    cmds = gen_tacacs(sw, ip_sw, mask, ip_srv, key, user, passwd)
    todo = mostrar_resultado("TACACS", [(f"Configuracion {sw}", cmds)])

    print(f"\n  {C.AMARILLO}📌 Configurar Servidor AAA en PT:{C.RESET}")
    pasos = [
        f"1. Server → Services → AAA → ON",
        f"2. Network Config: Client={sw}, IP={ip_sw}, Secret={key}, Type=TACACS+ → Add",
        f"3. User Setup: User={user}, Pass={passwd} → Add",
    ]
    for p in pasos:
        print(f"  {C.CYAN}  {p}{C.RESET}")
    print()

    finalizar(f"TACACS_{sw}", todo)

def topologia_wireless():
    limpiar()
    linea("═", C.CYAN)
    centrar("📶  WIRELESS COMPLETO", C.CYAN + C.BOLD)
    linea("═", C.CYAN)
    print()

    ssid   = pedir("SSID", "UV-Emmanuel")
    passwd = pedir("Password WiFi", "UV2026secure")
    rpass  = pedir("Password Router", "UV2026")
    mac    = pedir("MAC Laptop", "0001.635A.6994")

    barra("Generando topologia Wireless...")

    pasos_txt = f"""WIRELESS WRT300N - PASOS EN PT GUI
===================================
SSID: {ssid}
Password WiFi: {passwd}
Password Router: {rpass}
MAC Laptop permitida: {mac}

PASOS:
1. Doble clic WRT300N → GUI
2. Administration → Management → Password: {rpass} → Remote: Disabled → Save
3. Wireless → Basic → SSID: {ssid} → Broadcast: Disabled → Save
4. Security → Firewall → SPI: ON → Save
5. Wireless → Security → WPA2 Personal → AES → Key: {passwd} → Save
6. Wireless → MAC Filter → Enable → Permit → MAC: {mac} → Save
7. Laptop: instalar WPC300N → PC Wireless → {ssid} → Key: {passwd}"""

    limpiar()
    linea("═", C.VERDE)
    centrar("✅  WIRELESS WRT300N", C.VERDE + C.BOLD)
    linea("═", C.VERDE)
    print()

    pasos = [
        f"Administration → Management → Password: {C.BOLD}{rpass}{C.RESET} → Remote: Disabled",
        f"Wireless → Basic → SSID: {C.BOLD}{ssid}{C.RESET} → Broadcast: Disabled",
        f"Security → Firewall → SPI Firewall: ON",
        f"Wireless → Security → WPA2 Personal → AES → Key: {C.BOLD}{passwd}{C.RESET}",
        f"Wireless → MAC Filter → Enable → Permit → MAC: {C.BOLD}{mac}{C.RESET}",
        f"Laptop: WPC300N → PC Wireless → {ssid} → Key: {passwd}",
    ]
    for i, p in enumerate(pasos, 1):
        print(f"  {C.VERDE}{C.BOLD}[{i}]{C.RESET}  {p}")
        print()

    finalizar("Wireless_WRT300N", pasos_txt)

def topologia_examen():
    """Topologia completa del examen con todos los temas"""
    limpiar()
    linea("═", C.CYAN)
    centrar("🏆  TOPOLOGIA COMPLETA DEL EXAMEN", C.CYAN + C.BOLD)
    centrar("Port Security + VLANs + SSH + TACACS + Wireless", C.DIM)
    linea("═", C.CYAN)
    print()
    print(f"  {C.AMARILLO}Ingresa los datos de tu red:{C.RESET}\n")

    # Datos generales
    print(f"  {C.CYAN}{C.BOLD}--- SWITCHES ---{C.RESET}")
    sw1    = pedir("Switch principal", "SW1")
    ip_sw1 = pedir("IP SW1", "192.168.1.1")
    mask   = pedir("Mascara", "255.255.255.0")
    gw     = pedir("Gateway", "192.168.1.254")

    print(f"\n  {C.CYAN}{C.BOLD}--- PORT SECURITY ---{C.RESET}")
    mac1   = pedir("MAC PC1", "000A.F371.C91B")
    mac2   = pedir("MAC PC2", "0030.A34E.6B14")
    modo   = pedir("Violation mode", "shutdown")

    print(f"\n  {C.CYAN}{C.BOLD}--- VLANs ---{C.RESET}")
    v1id   = pedir("VLAN 1 ID", "10")
    v1nom  = pedir("VLAN 1 Nombre", "VENTAS")
    v2id   = pedir("VLAN 2 ID", "20")
    v2nom  = pedir("VLAN 2 Nombre", "RRHH")

    print(f"\n  {C.CYAN}{C.BOLD}--- SSH ---{C.RESET}")
    dom    = pedir("Dominio", "universidad.edu")
    user   = pedir("Usuario", "admin")
    passwd = pedir("Password", "cisco123")

    print(f"\n  {C.CYAN}{C.BOLD}--- TACACS ---{C.RESET}")
    ip_srv = pedir("IP servidor TACACS", "192.168.1.100")
    key    = pedir("Clave TACACS", "cisco123")

    print(f"\n  {C.CYAN}{C.BOLD}--- WIRELESS ---{C.RESET}")
    ssid   = pedir("SSID", "UV-Emmanuel")
    wpass  = pedir("Password WiFi", "UV2026secure")
    rpass  = pedir("Password Router", "UV2026")
    mac_lap= pedir("MAC Laptop", "0001.635A.6994")

    barra("Construyendo topologia completa del examen...", 30)

    # Generar todos los comandos
    ps_cmds = gen_port_security(
        sw1,
        [("fa0/1", mac1), ("fa0/2", mac2)],
        modo, "10", "fa0/3-22"
    )

    # VLANs van en el mismo switch
    vlan_cmds = f"""enable
configure terminal
vlan {v1id}
 name {v1nom}
 exit
vlan {v2id}
 name {v2nom}
 exit
interface fa0/1
 switchport access vlan {v1id}
 exit
interface fa0/2
 switchport access vlan {v2id}
 exit
interface fa0/23
 switchport mode trunk
 exit
exit
show vlan brief
write memory"""

    ssh_cmds = gen_ssh(sw1, ip_sw1, mask, gw, dom, user, passwd)

    tacacs_cmds = gen_tacacs(sw1, ip_sw1, mask, ip_srv, key, user, passwd)

    wireless_pasos = f"""WIRELESS WRT300N - PASOS EN PT GUI
1. Administration → Management → Password: {rpass} → Remote: Disabled → Save
2. Wireless → Basic → SSID: {ssid} → Broadcast: Disabled → Save
3. Security → Firewall → SPI: ON → Save
4. Wireless → Security → WPA2 Personal → AES → Key: {wpass} → Save
5. Wireless → MAC Filter → Enable → Permit → MAC: {mac_lap} → Save
6. Laptop: WPC300N → PC Wireless → {ssid} → Key: {wpass}"""

    secciones = [
        (f"1. PORT SECURITY - {sw1}", ps_cmds),
        (f"2. VLANs - {sw1}", vlan_cmds),
        (f"3. SSH - {sw1}", ssh_cmds),
        (f"4. TACACS - {sw1}", tacacs_cmds),
        (f"5. WIRELESS - WRT300N (GUI)", wireless_pasos),
    ]

    todo = mostrar_resultado("TOPOLOGIA COMPLETA DEL EXAMEN", secciones)

    # Instrucciones adicionales
    print(f"\n  {C.AMARILLO}{C.BOLD}📋 ORDEN DE CONFIGURACION EN PT:{C.RESET}\n")
    orden = [
        f"Agregar: {sw1} (2960) + PCs + Server + WRT300N + Laptop",
        f"Conectar todo con Copper Straight-Through",
        f"Aplicar comandos Port Security en {sw1}",
        f"Aplicar comandos VLANs en {sw1}",
        f"Aplicar comandos SSH en {sw1}",
        f"Configurar Server AAA para TACACS",
        f"Aplicar comandos TACACS en {sw1}",
        f"Configurar WRT300N por GUI (ver pasos)",
        f"Conectar Laptop al WiFi: {ssid}",
    ]
    for i, o in enumerate(orden, 1):
        print(f"  {C.VERDE}[{i:02d}]{C.RESET}  {o}")

    print()
    finalizar("EXAMEN_COMPLETO", todo)

def topologia_personalizada():
    limpiar()
    linea("═", C.CYAN)
    centrar("⚙️  TOPOLOGIA PERSONALIZADA", C.CYAN + C.BOLD)
    linea("═", C.CYAN)
    print()
    print(f"  {C.AMARILLO}Selecciona los modulos que quieres incluir:{C.RESET}\n")

    modulos = {}
    opciones = [
        ("ps",      "🔒 Port Security"),
        ("vlan",    "🔀 VLANs"),
        ("ssh",     "🔐 SSH"),
        ("tacacs",  "🛡️  TACACS"),
        ("wifi",    "📶 Wireless"),
    ]

    for key, nombre in opciones:
        r = pedir(f"Incluir {nombre}? (s/n)", "s")
        modulos[key] = r.lower() == 's'

    print()
    secciones = []
    todo = ""

    if modulos.get("ps"):
        print(f"\n  {C.CYAN}--- Port Security ---{C.RESET}")
        sw   = pedir("Switch", "SW1")
        mac1 = pedir("MAC PC1", "000A.F371.C91B")
        mac2 = pedir("MAC PC2", "0030.A34E.6B14")
        modo = pedir("Violation", "shutdown")
        cmds = gen_port_security(sw, [("fa0/1",mac1),("fa0/2",mac2)], modo, "10", "fa0/3-24")
        secciones.append(("PORT SECURITY", cmds))

    if modulos.get("vlan"):
        print(f"\n  {C.CYAN}--- VLANs ---{C.RESET}")
        sw    = pedir("Switch", "SW1")
        vlans = [("10","VENTAS","fa0/1"),("20","RRHH","fa0/2"),("30","TI","fa0/3")]
        trunk = pedir("Puerto trunk", "fa0/24")
        cmds  = gen_vlans(sw, vlans, trunk)
        secciones.append(("VLANs", cmds))

    if modulos.get("ssh"):
        print(f"\n  {C.CYAN}--- SSH ---{C.RESET}")
        sw   = pedir("Switch", "SW1")
        ip   = pedir("IP", "192.168.1.1")
        dom  = pedir("Dominio", "universidad.edu")
        user = pedir("Usuario", "admin")
        pw   = pedir("Password", "cisco123")
        cmds = gen_ssh(sw, ip, "255.255.255.0", "192.168.1.254", dom, user, pw)
        secciones.append(("SSH", cmds))

    if modulos.get("tacacs"):
        print(f"\n  {C.CYAN}--- TACACS ---{C.RESET}")
        sw  = pedir("Switch", "SW1")
        ip  = pedir("IP switch", "192.168.1.1")
        srv = pedir("IP servidor", "192.168.1.100")
        key = pedir("Clave", "cisco123")
        cmds = gen_tacacs(sw, ip, "255.255.255.0", srv, key, "admin", "cisco123")
        secciones.append(("TACACS", cmds))

    if modulos.get("wifi"):
        print(f"\n  {C.CYAN}--- Wireless ---{C.RESET}")
        ssid = pedir("SSID", "UV-Emmanuel")
        pw   = pedir("Password", "UV2026secure")
        mac  = pedir("MAC Laptop", "0001.635A.6994")
        pasos = f"1. SSID: {ssid}\n2. WPA2 AES Key: {pw}\n3. MAC Filter: {mac}"
        secciones.append(("WIRELESS PASOS", pasos))

    if secciones:
        barra("Construyendo topologia personalizada...", 25)
        todo = mostrar_resultado("TOPOLOGIA PERSONALIZADA", secciones)
        finalizar("Topologia_Custom", todo)
    else:
        print(f"\n  {C.ROJO}No seleccionaste ningun modulo.{C.RESET}\n")

# ============================================================
# MAIN
# ============================================================
def main():
    banner()
    barra("Iniciando Topology Builder...", 15)
    print(f"  {C.VERDE}✅ Listo{C.RESET}")
    print(f"  {C.CYAN}💾 Topologias en: {CARPETA}{C.RESET}\n")
    time.sleep(0.8)

    opciones = {
        '1': topologia_port_security,
        '2': topologia_vlans,
        '3': topologia_ssh,
        '4': topologia_tacacs,
        '5': topologia_wireless,
        '6': topologia_examen,
        '7': topologia_personalizada,
    }

    while True:
        limpiar()
        banner()
        menu()

        hora = datetime.now().strftime("%H:%M:%S")
        print(f"  {C.DIM}⏰ {hora}{C.RESET}\n")

        op = input(f"  {C.CYAN}{C.BOLD}▶  Selecciona topologia: {C.RESET}").strip()

        if op == '8':
            limpiar()
            linea()
            centrar("👋  Hasta luego!", C.VERDE + C.BOLD)
            centrar("🔥  Buena suerte en el examen!", C.AMARILLO + C.BOLD)
            linea()
            print()
            sys.exit(0)
        elif op in opciones:
            opciones[op]()
        else:
            print(f"\n  {C.ROJO}Opcion no valida{C.RESET}\n")
            time.sleep(1)
            continue

        input(f"\n  {C.DIM}Presiona Enter para volver al menu...{C.RESET}")

if __name__ == "__main__":
    main()
