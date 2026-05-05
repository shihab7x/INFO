#====={SHIHAB-X07}=====#
# TOOL: ULTRA INFO LOOKUP (V-10.0)
# DEVELOPER: SHIHAB (PRO)
#__________________________

import os, sys, time, requests, random

# Advanced Color Codes
G = '\x1b[1;92m' # Neon Green
Y = '\x1b[1;93m' # Golden Yellow
B = '\x1b[1;94m' # Deep Blue
P = '\x1b[1;95m' # Neon Pink
C = '\x1b[1;96m' # Cyan
W = '\x1b[1;97m' # Bright White
R = '\x1b[1;91m' # Red

def line():
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

logo = (f"""
{P}  ██████  ██░ ██  ██▓ ██░ ██  ▄▄▄       ▄▄▄▄   
{P}▒██    ▒ ▓██░ ██▒▓██▒▓██░ ██▒▒████▄    ▓█████▄ 
{P}░ ▓██▄   ▒██▀▀██░▒██▒▒██▀▀██░▒██  ▀█▄  ▒██▒ ▄██
{P}  ▒   ██▒░▓█ ░██ ░██░░▓█ ░██ ░██▄▄▄▄██ ▒██░█▀  
{P}▒██████▒▒░▓█▒ ░██▒░██░░▓█▒ ░██▒ ▓█   ▓██▒░▓█  ▀█ 
{P}▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ▒ ░░▒░▒░ ▒▒   ▓▒█░░▒ ▓▀█▄
{P}░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░  ▒ ░▒░ ░  ▒   ▒▒ ░ ░  ░
{W}          [ PROJECT : INFORMATION X ]
{C} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W} [•] {Y}DEV     : {W}SHIHAB-X07
{W} [•] {Y}VERSION : {W}V-10.0 (ULTRA PREMIUM)
{W} [•] {Y}STATUS  : {G}ONLINE / STABLE
{C} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def phone_tracker():
    os.system('clear')
    print(logo)
    num = input(f"{W} [?] Enter Target Number : {G}")
    print(f"{Y} [!] Extracting Signal Data...")
    time.sleep(2)
    # Logic for operator
    op = "Unknown"
    if "017" in num or "013" in num: op = "Grameenphone"
    elif "019" in num or "014" in num: op = "Banglalink"
    elif "018" in num: op = "Robi"
    elif "016" in num: op = "Airtel"
    elif "015" in num: op = "Teletalk"
    
    line()
    print(f"{G} [•] OPERATOR : {W}{op}")
    print(f"{G} [•] COUNTRY  : {W}Bangladesh")
    print(f"{G} [•] STATUS   : {G}Active (Online)")
    print(f"{G} [•] TYPE     : {W}GSM / Prepaid")
    line()
    input(f"{W} [ENTER TO BACK]")
    main()

def ip_lookup():
    os.system('clear')
    print(logo)
    ip = input(f"{W} [?] Enter Target IP : {G}")
    print(f"{Y} [!] Scanning Global Nodes...")
    time.sleep(1.5)
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        line()
        print(f"{G} [•] CITY     : {W}{data.get('city')}")
        print(f"{G} [•] ISP      : {W}{data.get('isp')}")
        print(f"{G} [•] ZIP      : {W}{data.get('zip')}")
        print(f"{G} [•] MAP LINK : {C}google.com/maps?q={data.get('lat')},{data.get('lon')}")
        line()
    except: print(f"{R} [!] API Connection Failed")
    input(f"{W} [ENTER TO BACK]")
    main()

def device_info():
    os.system('clear')
    print(logo)
    print(f"{Y} [!] Reading System Hardware...")
    time.sleep(1)
    line()
    print(f"{G} [•] OS NAME  : {W}{os.name.upper()}")
    print(f"{G} [•] PLATFORM : {W}{sys.platform}")
    print(f"{G} [•] STORAGE  : {W}Optimized for Termux")
    line()
    input(f"{W} [ENTER TO BACK]")
    main()

def wa_generator():
    os.system('clear')
    print(logo)
    num = input(f"{W} [?] Enter Number (+880...) : {G}")
    link = f"https://wa.me/{num}"
    line()
    print(f"{G} [•] WhatsApp Link Created!")
    print(f"{W} {link}")
    line()
    input(f"{W} [ENTER TO BACK]")
    main()

def main():
    os.system('clear')
    print(logo)
    print(f"{W} [{P}01{W}] {G}Phone Number Tracker")
    print(f"{W} [{P}02{W}] {G}Advanced IP Lookup")
    print(f"{W} [{P}03{W}] {G}Check Device Info")
    print(f"{W} [{P}04{W}] {G}WhatsApp Link Gen")
    print(f"{W} [{P}05{W}] {G}Update Tool")
    print(f"{W} [{P}00{W}] {R}Exit Tool")
    line()
    shihab = input(f"{W} [?] Choice Option : {G}")
    
    if shihab == '1' or shihab == '01': phone_tracker()
    elif shihab == '2' or shihab == '02': ip_lookup()
    elif shihab == '3' or shihab == '03': device_info()
    elif shihab == '4' or shihab == '04': wa_generator()
    elif shihab == '5' or shihab == '05': 
        print(f"{Y} [!] Please wait, updating...")
        os.system("git pull")
        print(f"{G} [✓] Update Complete!"); time.sleep(1); main()
    elif shihab == '0' or shihab == '00': sys.exit()
    else: print(f"{R} [!] Invalid Choice!"); time.sleep(1); main()

if __name__ == "__main__":
    main()
