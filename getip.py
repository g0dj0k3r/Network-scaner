import socket
from pyfiglet import *
from colorama import *
f=Figlet()
def get_ip():
    
    
    print(Fore.LIGHTRED_EX+f.renderText("GET URL IP"))
    
    target=input("ENTER TARGET URL TO GET IP:")
    get_ip=socket.gethostbyname(target)

    print(get_ip)
