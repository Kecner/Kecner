
#!/usr/bin/env python3
import socket
import sys
import datetime

if len(sys.argv)!= 2: 
    print("Usage: python3 kecner.py <target>")
    print("Example: python3 kecner.py scanme.nmap.org")
    sys.exit()

hedef = sys.argv[1]
portlar = [21, 22, 23, 80, 443, 3306, 5432, 8080, 8443]
acik_portlar = []

print(f"""
  _ __ 
 | |/ /__ ___ _ __ ___ _ __
 | ' // _ \\/ __| '_ \\ / _ \\ '__|
 |. \\ __/ (__| | | | __/ | 
 |_|\\_\\___|\\___|_| |_|\\___|_| 
                               
    Kecner v1.1 - Fast Port Scanner
    github.com/kral/kecner
""")
print(f"[+] Target: {hedef}")
print(f"[+] Started: {datetime.datetime.now().strftime('%H:%M:%S')}")
print(f"[+] Scanning...\n")

for port in portlar:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    sonuc = s.connect_ex((hedef, port))
    
    if sonuc == 0:
        print(f"[+] {port}/tcp OPEN")
        acik_portlar.append(port)
    s.close()

print(f"\n[+] Finished: {datetime.datetime.now().strftime('%H:%M:%S')}")
print(f"[+] {len(acik_portlar)} open ports found: {acik_portlar}")
print(f"[+] Scan completed - Kecner v1.1")

