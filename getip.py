import socket
from pyfiglet import *
from colorama import *
f=Figlet()
def get_ip():
    
    
    print(Fore.LIGHTRED_EX+f.renderText("GET URL IP"))
    
    target=input("ENTER TARGET URL TO GET IP:")
    
    if not target:
        print(Fore.RED+f"Please enter a valid URL"+Style.RESET_ALL)
        return
    try:
        get_ip=socket.gethostbyname(target)
        print(Fore.GREEN+f"IP OF {target} : {get_ip}"+Style.RESET_ALL)
    except socket.gaierror:
        print(Fore.RED+f"Error: Unable to resolve {target}"+Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED+f"An error occurred: {e}"+Style.RESET_ALL)