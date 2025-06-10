import nmap
from pyfiglet import *
from colorama import *

scanner=nmap.PortScanner()
f=Figlet()
def os_discovery():
    
    print(Fore.CYAN+f.renderText("OS DISCOVERY"))
    
    target=input("enter target :")
    print(Fore.RESET)
    scanner.scan(target,arguments='-O')

    for host in scanner.all_hosts():
        
        scanner.scan(host,arguments='-O')
        
        if 'osmatch' in scanner[host]:
            for osmatch in scanner[host]['osmatch']:
                
                osversion=osmatch.get('osgen', 'Unknown version')
                osname=osmatch['name']
                if 'osclass' in osmatch:
                    
                    for osclass in osmatch['osclass']:
                        
                        
                        print(Fore.GREEN+"ip :",host)
                        
                        print("os type :",osclass['type'])
                        
                        print("os name:",osname)
                        
                        print("os family:",osclass['osfamily'])
                        
                        print("VERSION :",osversion)
                        
                        print("<---------------------------------------------------->"+Fore.RESET)
                