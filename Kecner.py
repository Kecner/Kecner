import os
import time
import socket
import requests

# Renk Kodları
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

def banner():
    os.system("clear")
    print(f"""{RED}
             ___
            (o,o)     {WHITE}KECNER v1.0{RED}
           {{{{`"'}}}}     {CYAN}The Raven is Watching...{RED}
           -"-"-
    ╦╔═  ╔═╗  ╔═╗  ╔╗╔  ╔═╗  ╦═╗
    ╠╩╗  ║╣   ║    ║║║  ║╣   ╠╦╝
    ╩ ╩  ╚═╝  ╚═╝  ╝╚╝  ╚═╝  ╩╚═
    {WHITE}[---------------------------------------]
    {GREEN}Geliştirici: Kecner {WHITE}| {GREEN}Güvenlik Modülü
    {WHITE}[---------------------------------------]{RESET}
    """)

def network_menu():
    while True:
        banner()
        print(f"{CYAN}--- Network Tools ---{RESET}\n")
        print(f"{RED}[1]{WHITE} Port Tarayıcı (Hızlı)")
        print(f"{RED}[2]{WHITE} IP Bilgi Toplama")
        print(f"{RED}[99]{WHITE} Geri Dön")
        
        n_choice = input(f"\n{RED}Kecner/Network > {RESET}")
        
        if n_choice == "99":
            break
        elif n_choice == "1":
            banner()
            target = input(f"{WHITE}Hedef IP veya URL: {RESET}")
            print(f"{CYAN}[!] {target} taranıyor...{RESET}\n")
            ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389, 8080]
            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"{GREEN}[+] Port {port} : AÇIK {RESET}")
                s.close()
            input(f"\n{WHITE}Tarama bitti. Enter'a bas...{RESET}")
        elif n_choice == "2":
            banner()
            ip_addr = input(f"{WHITE}Sorgulanacak IP (Boş bırakırsan kendi IP'n): {RESET}")
            print(f"{CYAN}[!] Bilgiler çekiliyor...{RESET}\n")
            try:
                response = requests.get(f"http://ip-api.com/json/{ip_addr}").json()
                if response['status'] == 'success':
                    print(f"{GREEN}[+] Ülke: {WHITE}{response['country']}")
                    print(f"{GREEN}[+] Şehir: {WHITE}{response['city']}")
                    print(f"{GREEN}[+] ISP: {WHITE}{response['isp']}")
                    print(f"{GREEN}[+] IP: {WHITE}{response['query']}")
                else:
                    print(f"{RED}[-] Bilgi bulunamadı.{RESET}")
            except:
                print(f"{RED}[-] Bağlantı hatası!{RESET}")
            input(f"\n{WHITE}Devam etmek için Enter'a bas...{RESET}")

def main_menu():
    while True:
        banner()
        print(f"""
    {RED}[1]{WHITE} Network Tools (Port Scanner, Recon)
    {RED}[2]{WHITE} Exploitation Tools (Sızma)
    {RED}[0]{WHITE} Çıkış
        """)
        choice = input(f"{RED}Kecner > {RESET}")
        if choice == "1":
            network_menu()
        elif choice == "2":
            print(f"\n{CYAN}[!] Sızma Modülleri v1.1 ile eklenecektir.{RESET}")
            time.sleep(2)
        elif choice == "0":
            print(f"{GREEN}Karga yuvaya dönüyor...{RESET}")
            break

if __name__ == "__main__":
    main_menu()
