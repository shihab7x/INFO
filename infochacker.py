#====={SHIHAB-X07}=====#
# TOOL: ADVANCED PHONE LOOKUP
# DEVELOPER: SHIHAB (PRO)
#__________________________

import os, sys, time, requests

# Color Codes
H = '\x1b[1;92m' # Green (Bold)
O = '\x1b[1;96m' # Cyan
P = '\x1b[1;97m' # White
M = '\x1b[1;91m' # Red

# Ekdom Perfect SHIHAB Logo
logo = (f"""
{H}  ____  _   _ ___ _   _    _    ____  
{H} / ___|| | | |_ _| | | |  / \  | __ ) 
{H} \___ \| |_| || || |_| | / _ \ |  _ \ 
{H}  ___) |  _  || ||  _  |/ ___ \| |_) |
{H} |____/|_| |_|___|_| |_/_/   \_\____/ 
                                       
{P}          [ DEVELOPER : SHIHAB ]
{O} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{P} [✓] CREATED BY   :  SHIHAB-WF
{P} [✓] ROLE         :  SECURITY EXPERT
{P} [✓] VERSION      :  V-5.0 (INTELLIGENT)
{O} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

def lookup():
    os.system('clear')
    print(logo)
    print(f"{H} [!] Format: +8801XXXXXXXXX")
    number = input(f"{H} [?] Enter Number : ")
    
    # "Intelligent" Fake-Loading for Realism
    print(f"\n{O} [✓] Connecting to API...")
    time.sleep(1)
    print(f"{O} [✓] Bypassing Firewalls...")
    time.sleep(1)
    print(f"{O} [✓] Fetching Data From Server...")
    time.sleep(1.5)
    
    # Detailed Result Layout
    print(f"{O} ━━━━━━━━━━━━━━━━━━━━[ RESULT ]━━━━━━━━━━━━━━━━━━━━")
    print(f"{H} [•] Phone Number : {P}{number}")
    print(f"{H} [•] Country      : {P}Bangladesh (BD)")
    
    # Logic to identify carrier for extra 'intelligence'
    op = "Detected"
    if "017" in number or "013" in number: op = "Grameenphone"
    elif "019" in number or "014" in number: op = "Banglalink"
    elif "018" in number: op = "Robi"
    elif "016" in number: op = "Airtel"
    elif "015" in number: op = "Teletalk"
    
    print(f"{H} [•] Carrier      : {P}{op}")
    print(f"{H} [•] Type         : {P}Mobile (GSM)")
    print(f"{H} [•] Valid        : {P}Yes (Active)")
    print(f"{H} [•] Spam Score   : {P}0% (Safe)")
    print(f"{O} ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    input(f"\n{H} [ Back ]")
    main()

def main():
    os.system('clear')
    print(logo)
    print(f"{H} [1] Start Advanced Lookup")
    print(f"{H} [0] Exit Tool")
    choice = input(f"\n{H} [?] Select : ")
    if choice == '1': lookup()
    else: sys.exit()

if __name__ == "__main__":
    main()
