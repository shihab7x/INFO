#====={SHIHAB-X07}=====#
# TOOL: PRO GPS TRACKER & INFO
# DEVELOPER: SHIHAB (PRO)
#__________________________

import os, sys, time, requests

# Color Codes
G = '\x1b[1;92m' # Green
Y = '\x1b[1;93m' # Yellow
P = '\x1b[1;95m' # Pink
C = '\x1b[1;96m' # Cyan
W = '\x1b[1;97m' # White
R = '\x1b[1;91m' # Red

logo = (f"""
{P}  ██████  ██░ ██  ██▓ ██░ ██  ▄▄▄       ▄▄▄▄   
{P}▒██    ▒ ▓██░ ██▒▓██▒▓██░ ██▒▒████▄    ▓█████▄ 
{P}░ ▓██▄   ▒██▀▀██░▒██▒▒██▀▀██░▒██  ▀█▄  ▒██▒ ▄██
{P}  ▒   ██▒░▓█ ░██ ░██░░▓█ ░██ ░██▄▄▄▄██ ▒██░█▀  
{P}▒██████▒▒░▓█▒ ░██▒░██░░▓█▒ ░██▒ ▓█   ▓██▒░▓█  ▀█ 
{C} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W} [•] {Y}SYSTEM  : {W}ADVANCED GPS GRABBER
{W} [•] {Y}DEV     : {W}SHIHAB-X07
{C} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def gps_grabber():
    os.system('clear')
    print(logo)
    print(f"{Y} [!] Target-er kache pathanor jonno link toiri hochche...")
    time.sleep(2)
    print(f"\n{G} [✓] Step 1: {W}Go to 'https://iplogger.org'")
    print(f"{G} [✓] Step 2: {W}Select 'Invisible Image' or 'URL Shortener'")
    print(f"{G} [✓] Step 3: {W}Enable 'Collect GPS Data' button in settings")
    print(f"\n{P} [!] Target jokhon click korbe, browser permission chaibe.")
    print(f"{P} [!] Shey 'Allow' korle apni exact Map Link paben.")
    print(f"{C} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    input(f"{W} [ENTER TO BACK]")
    main()

def phone_tracker():
    os.system('clear')
    print(logo)
    num = input(f"{W} [?] Enter Number : {G}")
    # Carrier Logic
    op = "Unknown"
    if "017" in num or "013" in num: op = "Grameenphone"
    elif "018" in num: op = "Robi"
    elif "019" in num or "014" in num: op = "Banglalink"
    elif "016" in num: op = "Airtel"
    elif "015" in num: op = "Teletalk"
    
    print(f"\n{G} [•] Operator : {W}{op}")
    print(f"{G} [•] Location : {W}Bangladesh (Approx)")
    print(f"{C} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    input(f"{W} [ENTER TO BACK]")
    main()

def ip_tracker():
    os.system('clear')
    print(logo)
    ip = input(f"{W} [?] Enter IP : {G}")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"\n{G} [•] City   : {W}{data.get('city')}")
        print(f"{G} [•] ISP    : {W}{data.get('isp')}")
        print(f"{G} [•] Map    : {C}https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
    except: print(f"{R} [!] Error!")
    input(f"{W} [ENTER TO BACK]")
    main()

def main():
    os.system('clear')
    print(logo)
    print(f"{W} [01] {G}Phone Info (Operator)")
    print(f"{W} [02] {G}IP Tracker (City Level)")
    print(f"{W} [03] {G}GPS Grabber (Exact Location)")
    print(f"{W} [00] {R}Exit")
    print(f"{C} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(f"{W} [?] Option : {G}")
    if opt == '1' or opt == '01': phone_tracker()
    elif opt == '2' or opt == '02': ip_tracker()
    elif opt == '3' or opt == '03': gps_grabber()
    else: sys.exit()

if __name__ == "__main__":
    main()
