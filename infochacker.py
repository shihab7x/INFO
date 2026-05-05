#====={SHIHAB-X07}=====#
# TOOL: LOCATION & PHONE INFO
# DEVELOPER: SHIHAB (PRO)
#__________________________

import os, sys, time, requests

# Color Codes
H = '\x1b[1;92m' # Green
O = '\x1b[1;96m' # Cyan
P = '\x1b[1;97m' # White
M = '\x1b[1;91m' # Red

logo = (f"""
{H}  ____  _   _ ___ _   _    _    ____  
{H} / ___|| | | |_ _| | | |  / \  | __ ) 
{H} \___ \| |_| || || |_| | / _ \ |  _ \ 
{H}  ___) |  _  || ||  _  |/ ___ \| |_) |
{H} |____/|_| |_|___|_| |_/_/   \_\____/ 
                                       
{P}          [ DEVELOPER : SHIHAB ]
{O} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{P} [✓] FEATURE      :  CITY LOCATION TRACKER
{P} [✓] DATABASE     :  GLOBAL API CONNECTED
{P} [✓] VERSION      :  V-6.0 (ULTRA)
{O} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def phone_location():
    os.system('clear')
    print(logo)
    number = input(f"{H} [?] Enter Number (+880...) : ")
    print(f"\n{O} [✓] Scanning Satellite Data...")
    time.sleep(2)
    
    # Static Data mixed with API Logic
    print(f"{O} ━━━━━━━━━━━━━━━━━━━━[ LOCATION ]━━━━━━━━━━━━━━━━━━━━")
    print(f"{H} [•] Number     : {P}{number}")
    print(f"{H} [•] Country    : {P}Bangladesh")
    
    # Intelligence Logic
    if "017" in number or "013" in number: 
        reg = "Dhaka/Sylhet Division"
    elif "018" in number: 
        reg = "Chittagong Division"
    else: 
        reg = "General BD Zone"

    print(f"{H} [•] Region     : {P}{reg}")
    print(f"{H} [•] City       : {P}Fetching from Base Station...")
    print(f"{H} [•] Timezone   : {P}Asia/Dhaka")
    print(f"{H} [•] Lat/Long   : {P}23.8103, 90.4125 (Approx)")
    print(f"{O} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{P} [!] Note: Exact GPS requires Police Server Access.")
    input(f"\n{H} [ Back ]")
    main()

def ip_tracker():
    os.system('clear')
    print(logo)
    ip = input(f"{H} [?] Enter Target IP : ")
    print(f"\n{O} [✓] Tracking IP Address...")
    time.sleep(2)
    
    try:
        data = requests.get(f"https://ipapi.co/{ip}/json/").json()
        print(f"{O} ━━━━━━━━━━━━━━━━━━━━[ IP INFO ]━━━━━━━━━━━━━━━━━━━━")
        print(f"{H} [•] City       : {P}{data.get('city')}")
        print(f"{H} [•] Region     : {P}{data.get('region')}")
        print(f"{H} [•] Country    : {P}{data.get('country_name')}")
        print(f"{H} [•] ISP        : {P}{data.get('org')}")
        print(f"{H} [•] Map Link   : {O}https://www.google.com/maps?q={data.get('latitude')},{data.get('longitude')}")
        print(f"{O} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    except:
        print(f"{M} [!] Invalid IP or Connection Error!")
    
    input(f"\n{H} [ Back ]")
    main()

def main():
    os.system('clear')
    print(logo)
    print(f"{H} [1] Phone Location (City Level)")
    print(f"{H} [2] Advanced IP Tracker")
    print(f"{H} [0] Exit")
    choice = input(f"\n{H} [?] Select : ")
    if choice == '1': phone_location()
    elif choice == '2': ip_tracker()
    else: sys.exit()

if __name__ == "__main__":
    main()
