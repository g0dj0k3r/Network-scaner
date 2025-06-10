import nmap
import osdiscovery
import getip
import pingscan
from pyfiglet import Figlet
from colorama import Fore, Style

scanner=nmap.PortScanner()
f=Figlet()



def live_hosts():
    try:
        print(Fore.LIGHTBLUE_EX+f.renderText("LIVE HOST DISCOVER"))
        print("TARGET SPECIFICATION: \n1:192.168.0.0-255 \n2:192.168.0.0/24")   
        targ=input('ENTER YOUR TARGET:')
        print(Fore.RESET)
        print(Fore.GREEN+"scanning for live hosts..."+Fore.RESET)
        scanner.scan(targ,arguments='-sn')
        live_found=False
        for host in scanner.all_hosts():
            if scanner[host].state()=='up':
                print(Fore.GREEN+'LIVE HOSTS :',host,scanner[host].hostname())
                print(Fore.RESET)
                live_found=True
        if not live_found:
            print(Fore.RED+"0 HOST ALIVE"+Fore.RESET)
            
    except Exception as e:
        print(Fore.RED+f"error occurred during discovery: {e}"+Style.RESET_ALL)
        
        
        
        
def syn_scan():
    try:
        print(Fore.LIGHTCYAN_EX+f.renderText("SYN SCAN"))
        targ=input('ENTER YOUR TARGET:')
        print(Fore.RESET)
        print(Fore.GREEN+"SYN ACK scanning for open ports..."+Fore.RESET)
        scanner.scan(targ,arguments='-sS -p 1-1023')
        print(Fore.GREEN+"scan info:",scanner.scaninfo())
        print(Fore.RESET)
        
        
        for host in scanner.all_hosts():
            print(Fore.GREEN+"HOST :",(host,scanner[host].hostname()))
            print(Fore.GREEN+"STATE:",scanner[host].state())
            print(Fore.RESET)
            
            for proto in scanner[host].all_protocols():
                print(Fore.GREEN+"<------------------------>")
                print("protocol :",proto)
                print(Fore.RESET)
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    print(Fore.GREEN+"port :",port,"state:",scanner[host][proto][port]['state'])
                    print(Fore.RESET)
    except Exception as e:
        print(Fore.RED+f"error occurred during SYN scan: {e}"+Style.RESET_ALL) 
        
              
            
def udp_scan():
    try:
        print(Fore.LIGHTYELLOW_EX+f.renderText("UDP SCAN"))
        targ=input('ENTER YOUR TARGET:')
        print(Fore.RESET)
        scanner.scan(targ,arguments='-sU -p 1-1023')
        print(Fore.GREEN+"scan info:",scanner.scaninfo())
        print("scanning for open UDP ports..."+Fore.RESET)
        
        for host in scanner.all_hosts():
            print(Fore.GREEN+"HOST :",(host,scanner[host].hostname()))
            print("STATE:",scanner[host].state())
            print(Fore.RESET)
            
            for proto in scanner[host].all_protocols():
                print(Fore.GREEN+"<------------------------>")
                print("protocol :",proto)
                print(Fore.RESET)
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    print(Fore.GREEN+"port :",port,"state:",scanner[host][proto][port]['state'])
                    print(Fore.RESET)
    except Exception as e:
        print(Fore.RED+f"error occurred during UDP scan: {e}"+Style.RESET_ALL)
        

def version_scan():
    try:
        print(Fore.LIGHTWHITE_EX+f.renderText("VERSION SCAN"))
        targ=input('ENTER YOUR TARGET:')
        print(Fore.RESET)
        print(Fore.GREEN+"scanning for service versions..."+Fore.RESET)
        scanner.scan(targ,arguments='-sV -p 1-1023')
        print(Fore.GREEN+"scaninfo:",scanner.scaninfo())
        print(Fore.RESET)
        
        
        for host in scanner.all_hosts():
            print(Fore.GREEN+"HOST :",(host,scanner[host].hostname()))
            print("STATE:",scanner[host].state())
            print(Fore.RESET)
            
            for proto in scanner[host].all_protocols():
                print(Fore.GREEN+"<------------------------>")
                print("protocol :",proto)
                print(Fore.RESET)
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    service=scanner[host][proto][port]['name']
                    version=scanner[host][proto][port]['version']
                    status=scanner[host][proto][port]['state']
                    reason=scanner[host][proto][port]['reason']
               
                    print(Fore.GREEN+"port :",port,',','status :',status,',',"reason :",reason,',',"service :",service,",","version :",version)
                    print(Fore.RESET)
    except Exception as e:
        print(Fore.RED+f"error occurred during version scan: {e}"+Style.RESET_ALL)    
              
               
def agressive():
    
    try:
        print(Fore.MAGENTA+f.renderText("AGRESSIVE SCAN"))
        targ=input('ENTER YOUR TARGET:')
        print(Fore.RESET)
        print(Fore.GREEN+"performing agressive scan..."+Fore.RESET)
        scanner.scan(targ,arguments='-A -T4 -sV -vv -p 1-1023')
        print(Fore.GREEN+"scaninfo:",scanner.scaninfo())
        print(Fore.RESET)
        
        
        for host in scanner.all_hosts():
            print(Fore.GREEN+"HOST :",(host,scanner[host].hostname()))
            print("STATE:",scanner[host].state())
            print(Fore.RESET)
            
            
            for proto in scanner[host].all_protocols():
                print(Fore.GREEN+"<------------------------>")
                print("protocol :",proto)
                print(Fore.RESET)
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    service=scanner[host][proto][port]['name']
                    version=scanner[host][proto][port]['version']
                    status=scanner[host][proto][port]['state']
                    reason=scanner[host][proto][port]['reason']
               
                    print(Fore.GREEN+"port :",port,',','status :',status,',',"reason :",reason,',',"service :",service,",","version :",version)
                    print(Fore.RESET)
               
    except Exception as e:  
        print(Fore.RED+f"error occurred during agressive scan: {e}"+Style.RESET_ALL)          
