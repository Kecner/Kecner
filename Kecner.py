import socket
import threading
from queue import Queue
import sys
from datetime import datetime

# Banner - Temiz ve Ciddi
def print_banner():
    banner = r"""
     _  __                             
    | |/ /___  ___ _ __   ___ _ __ 
    | ' // _ \/ __| '_ \ / _ \ '__|
    | . \  __/ (__| | | |  __/ |   
    |_|\_\___|\___|_| |_|\___|_|   
                                   
    [ Kecner v1.1 - Fast Port Scanner ]
    """
    print(banner)
    print("-" * 55)
    print(f"Target Scan Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 55)

def port_scanner(target, port, q):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            try:
                # Portun hangi servise ait olduğunu bulur (80 -> http vb.)
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f" [+] Port {port:5} [OPEN]  -->  Service: {service}")
        s.close()
    except:
        pass

def threader(target, q):
    while True:
        port = q.get()
        port_scanner(target, port, q)
        q.task_done()

def main():
    # Komut satırından direkt hedefi alır: python3 Kecner.py 1.1.1.1
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("\n [!] Usage: python3 Kecner.py <target>")
        print(" [!] Example: python3 Kecner.py 192.168.1.1\n")
        sys.exit()

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n [!] Error: Could not resolve hostname.")
        sys.exit()

    print_banner()
    print(f"[*] Scanning Target: {target_ip}\n")

    q = Queue()

    # 100 Thread ile yüksek hız
    for x in range(100):
        t = threading.Thread(target=threader, args=(target_ip, q))
        t.daemon = True
        t.start()

    # Standart 1024 portu tarar
    for port in range(1, 1025):
        q.put(port)

    q.join()
    print("\n" + "-" * 55)
    print(" [+] Scan completed successfully. [Kecner v1.1]")
    print("-" * 55)

if __name__ == "__main__":
    main()
