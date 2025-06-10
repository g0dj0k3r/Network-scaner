
import osdiscovery
import getip
import pingscan
import scaners
import scriptscan
from pyfiglet import Figlet
from colorama import Fore


f=Figlet()

def main():
    print(Fore.RED+f.renderText("NETWORK SCANER\n"))

    print(Fore.MAGENTA+"\t  \t\t\t\tCREATED BY:GODJOKER\n\n")

    print(Fore.LIGHTBLUE_EX+"well known ports (0-1023)")
    print("registered ports (1024-49151)")
    print("dynamic ports (49152-65535).")
    print("NMAP VERSION:",scaners.scanner.nmap_version(),Fore.RESET)
    
    while True:
        try:
        
            options=['GET WEBSITE IP','DISCOVER LIVE HOSTS','PING SCAN','SYN ACK SCAN',
                    'UDP SCAN','VERSION SCAN','AGRESSIVE SCAN','OS DISCOVERY',
                    'SCRIPT SCAN','EXIT']
        
        
            print(Fore.YELLOW+"""\n\n\nCHOOSE OPTION TO SCAN\n
                    [1] GET WEBSITE IP\n
                    [2] DISCOVER LIVE HOSTS\n
                    [3] PING SCAN\n
                    [4] SYN ACK SCAN\n
                    [5] UDP SCAN\n
                    [6] VERSION SCAN\n
                    [7] AGRESSIVE SCAN\n
                    [8] OS DISCOVERY\n
                    [9] SCRIPT SCAN\n
                    [10] EXIT\n\n\n""")
            option=input("Enter scan option:")
            print(Fore.GREEN+"Scaning:",options[int(option)-1])
            print(Fore.YELLOW+"<------------------------------------------------->")
            print(Fore.RESET)
            if option=='1':
                getip.get_ip()
            
            elif option=='2':
                scaners.live_hosts()
            
            elif option=='3':
                pingscan.ping_scan()
            
            elif option=='4':
                scaners.syn_scan()
            
            elif option=='5':
                scaners.udp_scan()
            
            elif option=='6':
                scaners.version_scan()
            
            elif option=='7':
                scaners.agressive()
            
            elif option=='8':
                osdiscovery.os_discovery()
            
            elif option=='9':
                scriptscan.script_scan()
            
            elif option=='10':
            
                print(Fore.RED+f.renderText('!bye bye!'))
                
                break
        
        
            else:
                print("you entered invalid option")
                
                
                
        except IndexError:
            print(Fore.RED+"Invalid option. Please enter a number between 1 and 10."+Fore.RESET)
        except ValueError:
            print(Fore.RED+"Invalid input. Please enter a valid number."+Fore.RESET)
        except Exception as e:
            print(Fore.RED+"An error occurred:", e, Fore.RESET)
        except KeyboardInterrupt:
            print(Fore.RED+"\nScan interrupted by user. Exiting..."+Fore.RESET)
            break
        
           

