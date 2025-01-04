import nmap
from pyfiglet import *
from colorama import *


scanner=nmap.PortScanner()
f=Figlet()
def ping_scan():
    
    print(Fore.LIGHTGREEN_EX+f.renderText("PING SCAN"))
    
    target=input("ENTER YOUR TARGET IP:")

    scanner.scan(target,arguments="-sn")

    for host in scanner.all_hosts():
        print("<--------------------------------->")
        print("host name:",scanner[host].hostname())
        print("TARGET STATUS :",scanner[host].state())
        
        
    