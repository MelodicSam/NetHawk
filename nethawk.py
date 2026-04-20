#!/usr/bin/env python3

import os
import sys
import time
import socket
import subprocess
import ipaddress
import requests
from datetime import datetime

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt
    from rich import box
except ImportError:
    print("Missing dependencies. Run: sudo bash setup.sh")
    sys.exit(1)

console = Console()

# ─── Banner ───────────────────────────────────────────────

BANNER = """
[cyan]
  _   _      _   _   _               _    
 | \ | | ___| |_| | | | __ ___      | | __
 |  \| |/ _ \ __| |_| |/ _` \ \ /\ / /| |/ /
 | |\  |  __/ |_|  _  | (_| |\ V  V / |   < 
 |_| \_|\___|\__|_| |_|\__,_| \_/\_/  |_|\_\\
[/cyan]
[dim]        Network Reconnaissance Toolkit[/dim]
[dim]              by [cyan]MelodicSam[/cyan][/dim]
"""

MENU = """
[bold cyan] ┌─────────────────────────────────────┐[/bold cyan]
[bold cyan] │[/bold cyan]         [bold white]NETHAWK MAIN MENU[/bold white]           [bold cyan]│[/bold cyan]
[bold cyan] ├─────────────────────────────────────┤[/bold cyan]
[bold cyan] │[/bold cyan]  [green][1][/green]  Network Scanner                  [bold cyan]│[/bold cyan]
[bold cyan] │[/bold cyan]  [green][2][/green]  Port Scanner                     [bold cyan]│[/bold cyan]
[bold cyan] │[/bold cyan]  [green][3][/green]  IP Info Lookup                   [bold cyan]│[/bold cyan]
[bold cyan] │[/bold cyan]  [green][4][/green]  My Network Info                  [bold cyan]│[/bold cyan]
[bold cyan] │[/bold cyan]  [green][5][/green]  MAC Address Changer              [bold cyan]│[/bold cyan]
[bold cyan] │[/bold cyan]  [red][0][/red]  Exit                             [bold cyan]│[/bold cyan]
[bold cyan] └─────────────────────────────────────┘[/bold cyan]
"""

# ─── Helpers ──────────────────────────────────────────────

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def header(title):
    clear()
    console.print(Panel(f"[bold cyan]{title}[/bold cyan]", box=box.ROUNDED, border_style="cyan"))
    console.print()

def back():
    console.print()
    input("  Press Enter to go back to menu...")

def check_root():
    if os.geteuid() != 0:
        console.print("[red]⚠  This feature requires root privileges. Run with sudo.[/red]")
        return False
    return True

# ─── 1. Network Scanner ───────────────────────────────────

def network_scanner():
    header("📡  Network Scanner")

    target = Prompt.ask("  Enter target network (e.g. 192.168.1.0/24) or press Enter for auto-detect")

    if not target.strip():
        try:
            result = subprocess.run(["ip", "route"], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if "src" in line and "kernel" in line:
                    parts = line.split()
                    target = parts[0]
                    console.print(f"  [dim]Auto-detected network: [cyan]{target}[/cyan][/dim]")
                    break
        except:
            target = "192.168.1.0/24"
            console.print(f"  [dim]Using default: {target}[/dim]")

    console.print()
    console.print(f"  [dim]Scanning {target} for live hosts...[/dim]")
    console.print()

    live_hosts = []

    try:
        network = ipaddress.ip_network(target, strict=False)
        hosts   = list(network.hosts())

        table = Table(box=box.SIMPLE_HEAVY, border_style="dim", header_style="bold cyan", padding=(0, 2))
        table.add_column("#",       width=4,  style="dim")
        table.add_column("IP Address", width=18)
        table.add_column("Hostname",   width=30)
        table.add_column("Status",     width=10)

        with console.status("[cyan]Scanning...[/cyan]"):
            for i, host in enumerate(hosts[:254]):
                ip = str(host)
                try:
                    result = subprocess.run(
                        ["ping", "-c", "1", "-W", "1", ip],
                        capture_output=True, timeout=2
                    )
                    if result.returncode == 0:
                        try:
                            hostname = socket.gethostbyaddr(ip)[0]
                        except:
                            hostname = "Unknown"
                        live_hosts.append(ip)
                        table.add_row(
                            str(len(live_hosts)),
                            f"[cyan]{ip}[/cyan]",
                            hostname,
                            "[green]● LIVE[/green]"
                        )
                except:
                    pass

        if live_hosts:
            console.print(table)
            console.print(f"\n  [green]Found {len(live_hosts)} live host(s)[/green]")
        else:
            console.print("  [yellow]No live hosts found. Try a different network range.[/yellow]")

    except ValueError as e:
        console.print(f"  [red]Invalid network: {e}[/red]")

    back()

# ─── 2. Port Scanner ──────────────────────────────────────

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 135: "RPC",
    139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    6379: "Redis", 8080: "HTTP-Alt", 8443: "HTTPS-Alt",
    27017: "MongoDB", 5900: "VNC"
}

def port_scanner():
    header("🔍  Port Scanner")

    target = Prompt.ask("  Enter target IP or hostname")
    mode   = Prompt.ask("  Scan mode", choices=["quick", "full"], default="quick")

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        console.print(f"  [red]Could not resolve host: {target}[/red]")
        back()
        return

    console.print(f"\n  [dim]Scanning [cyan]{ip}[/cyan] ({target})...[/dim]\n")

    ports    = list(COMMON_PORTS.keys()) if mode == "quick" else range(1, 1025)
    open_ports = []

    table = Table(box=box.SIMPLE_HEAVY, border_style="dim", header_style="bold cyan", padding=(0, 2))
    table.add_column("Port",    width=8)
    table.add_column("Service", width=14)
    table.add_column("Status",  width=10)
    table.add_column("Banner",  width=30)

    with console.status(f"[cyan]Scanning {'common ports' if mode == 'quick' else 'ports 1-1024'}...[/cyan]"):
        for port in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    service = COMMON_PORTS.get(port, "Unknown")
                    banner  = ""
                    try:
                        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                        raw = s.recv(256).decode(errors="ignore").strip()
                        banner = raw.split("\n")[0][:30] if raw else ""
                    except:
                        pass
                    open_ports.append(port)
                    table.add_row(
                        f"[cyan]{port}[/cyan]",
                        service,
                        "[green]OPEN[/green]",
                        f"[dim]{banner}[/dim]"
                    )
                s.close()
            except:
                pass

    if open_ports:
        console.print(table)
        console.print(f"\n  [green]{len(open_ports)} open port(s) found[/green]")
    else:
        console.print("  [yellow]No open ports found.[/yellow]")

    back()

# ─── 3. IP Info Lookup ────────────────────────────────────

def ip_info():
    header("🌐  IP Info Lookup")

    target = Prompt.ask("  Enter IP address (or press Enter for your public IP)")

    with console.status("[cyan]Fetching IP info...[/cyan]"):
        try:
            url  = f"https://ipapi.co/{target}/json/" if target.strip() else "https://ipapi.co/json/"
            resp = requests.get(url, timeout=8)
            data = resp.json()

            if "error" in data:
                console.print(f"  [red]Error: {data.get('reason', 'Unknown error')}[/red]")
                back()
                return

            table = Table(box=box.SIMPLE_HEAVY, border_style="dim", show_header=False, padding=(0, 2))
            table.add_column("Field", style="dim",       width=20)
            table.add_column("Value", style="bold white", width=40)

            fields = [
                ("IP Address",   data.get("ip", "N/A")),
                ("Hostname",     data.get("hostname", "N/A")),
                ("City",         data.get("city", "N/A")),
                ("Region",       data.get("region", "N/A")),
                ("Country",      f"{data.get('country_name', 'N/A')} ({data.get('country_code', '')})"),
                ("Postal Code",  data.get("postal", "N/A")),
                ("Latitude",     str(data.get("latitude", "N/A"))),
                ("Longitude",    str(data.get("longitude", "N/A"))),
                ("Timezone",     data.get("timezone", "N/A")),
                ("ISP / Org",    data.get("org", "N/A")),
                ("ASN",          data.get("asn", "N/A")),
                ("Currency",     data.get("currency_name", "N/A")),
            ]

            for field, value in fields:
                table.add_row(field, f"[cyan]{value}[/cyan]")

            console.print(table)

        except requests.exceptions.ConnectionError:
            console.print("  [red]No internet connection.[/red]")
        except Exception as e:
            console.print(f"  [red]Error: {e}[/red]")

    back()

# ─── 4. My Network Info ───────────────────────────────────

def my_network_info():
    header("💻  My Network Info")

    table = Table(box=box.SIMPLE_HEAVY, border_style="dim", show_header=False, padding=(0, 2))
    table.add_column("Field", style="dim",       width=22)
    table.add_column("Value", style="bold white", width=40)

    # Hostname
    hostname = socket.gethostname()
    table.add_row("Hostname", f"[cyan]{hostname}[/cyan]")

    # Local IP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
    except:
        local_ip = "Unknown"
    table.add_row("Local IP", f"[cyan]{local_ip}[/cyan]")

    # Public IP
    try:
        public_ip = requests.get("https://api.ipify.org", timeout=5).text
    except:
        public_ip = "Could not fetch"
    table.add_row("Public IP", f"[cyan]{public_ip}[/cyan]")

    # Gateway
    try:
        result = subprocess.run(["ip", "route"], capture_output=True, text=True)
        gateway = "Unknown"
        for line in result.stdout.splitlines():
            if line.startswith("default"):
                gateway = line.split()[2]
                break
        table.add_row("Default Gateway", f"[cyan]{gateway}[/cyan]")
    except:
        pass

    # Interfaces
    try:
        result = subprocess.run(["ip", "-br", "addr"], capture_output=True, text=True)
        interfaces = []
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 3:
                iface  = parts[0]
                state  = parts[1]
                addr   = parts[2] if len(parts) > 2 else "N/A"
                color  = "green" if state == "UP" else "red"
                interfaces.append(f"[{color}]{iface}[/{color}] {addr}")
        table.add_row("Interfaces", "\n".join(interfaces))
    except:
        pass

    # DNS
    try:
        with open("/etc/resolv.conf") as f:
            dns = [l.split()[1] for l in f if l.startswith("nameserver")]
        table.add_row("DNS Servers", "\n".join([f"[cyan]{d}[/cyan]" for d in dns]))
    except:
        pass

    table.add_row("Scan Time", f"[dim]{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/dim]")

    console.print(table)
    back()

# ─── 5. MAC Address Changer ───────────────────────────────

def mac_changer():
    header("🔀  MAC Address Changer")

    if not check_root():
        back()
        return

    # List interfaces
    try:
        result = subprocess.run(["ip", "-br", "link"], capture_output=True, text=True)
        console.print("  [dim]Available interfaces:[/dim]")
        for line in result.stdout.splitlines():
            parts = line.split()
            if parts:
                console.print(f"  [cyan]→[/cyan] {parts[0]}")
        console.print()
    except:
        pass

    iface  = Prompt.ask("  Enter interface name (e.g. eth0, wlan0)")
    mode   = Prompt.ask("  Mode", choices=["random", "custom"], default="random")

    if mode == "custom":
        new_mac = Prompt.ask("  Enter new MAC address (format: XX:XX:XX:XX:XX:XX)")
    else:
        import random
        new_mac = "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))
        console.print(f"  [dim]Generated MAC: [cyan]{new_mac}[/cyan][/dim]")

    console.print()

    try:
        subprocess.run(["ip", "link", "set", iface, "down"],  check=True)
        subprocess.run(["ip", "link", "set", iface, "address", new_mac], check=True)
        subprocess.run(["ip", "link", "set", iface, "up"],    check=True)
        console.print(f"  [green]✓ MAC address changed to [cyan]{new_mac}[/cyan][/green]")
        console.print(f"  [dim]Interface [cyan]{iface}[/cyan] is back up.[/dim]")
    except subprocess.CalledProcessError as e:
        console.print(f"  [red]Failed to change MAC: {e}[/red]")
    except Exception as e:
        console.print(f"  [red]Error: {e}[/red]")

    back()

# ─── Main Loop ────────────────────────────────────────────

def main():
    while True:
        clear()
        console.print(BANNER)
        console.print(MENU)

        choice = Prompt.ask("  [cyan]nethawk[/cyan] → ", default="0")

        if choice == "1":
            network_scanner()
        elif choice == "2":
            port_scanner()
        elif choice == "3":
            ip_info()
        elif choice == "4":
            my_network_info()
        elif choice == "5":
            mac_changer()
        elif choice == "0":
            clear()
            console.print("\n  [cyan]Goodbye. Stay curious. Stay ethical.[/cyan]\n")
            sys.exit(0)
        else:
            console.print("  [red]Invalid option. Try again.[/red]")
            time.sleep(1)

if __name__ == "__main__":
    main()
