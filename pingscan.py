import nmap
from pyfiglet import Figlet
from colorama import Fore, Style


scanner=nmap.PortScanner()
f=Figlet()
def ping_scan():
    try:
        print(Fore.LIGHTGREEN_EX+f.renderText("PING SCAN"))
    
        target=input("ENTER YOUR TARGET IP:")


        if not target:
            print(Fore.RED+f"Error: Please enter a valid IP address"+Style.RESET_ALL)
            return
        print(Fore.GREEN+f"scanning target: {target}",Style.RESET_ALL)
        scanner.scan(target,arguments='-sn')
        if not scanner.all_hosts():
            print(Fore.RED+f"Error: Target unreachable or no hosts found"+Style.RESET_ALL)
            return
        for host in scanner.all_hosts():
            print(Fore.GREEN+"<--------------------------------->"+Style.RESET_ALL)
            print(Fore.GREEN+f"host name: {scanner[host].hostname() or 'Unknown'}"+Style.RESET_ALL)
            print(Fore.GREEN+f"TARGET STATUS : {scanner[host].state()}"+Style.RESET_ALL)
            
    except nmap.PortScannerError as e:
        print(Fore.RED+f"Error: {e}"+Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED+f"An error occurred: {e}"+Style.RESET_ALL)
        
        
    