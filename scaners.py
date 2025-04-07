import nmap
import osdiscovery
import getip
import pingscan
from pyfiglet import *
from colorama import *

scanner=nmap.PortScanner()
f=Figlet()



def live_hosts():
    try:
        print(Fore.LIGHTBLUE_EX+f.renderText("LIVE HOST DISCOVER"))
        print(Fore.LIGHTBLUE_EX+"TARGET SPECIFICATION: \n1:192.168.0.0-255 \n2:192.168.0.0/24")   
        targ=input('ENTER YOUR TARGET:')
        scanner.scan(targ,arguments='-sn')
        live_found=False
        for host in scanner.all_hosts():
            if scanner[host].state()=='up':
                print('LIVE HOSTS :',host,scanner[host].hostname())
                live_found=True
        if not live_found:
            print("0 HOST ALIVE")
            
    except Exception as e:
        print(Fore.RED+f"error occurred during discovery: {e}"+Style.RESET_ALL)
def syn_scan():
    try:
        print(Fore.RED+f.renderText("SYN SCAN"))
        targ=input('ENTER YOUR TARGET:')
        scanner.scan(targ,arguments='-sS -p 1-1023')
        print("scan info:",scanner.scaninfo())
        for host in scanner.all_hosts():
            print("HOST :",(host,scanner[host].hostname()))
            print("STATE:",scanner[host].state())
            for proto in scanner[host].all_protocols():
                print("<------------------------>")
                print("protocol :",proto)
            
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    print("port :",port,"state:",scanner[host][proto][port]['state'])
                
    except Exception as e:
        print(Fore.RED+f"error occurred during SYN scan: {e}"+Style.RESET_ALL)       
            
def udp_scan():
    try:
        print(Fore.YELLOW+f.renderText("UDP SCAN"))
        targ=input('ENTER YOUR TARGET:')
        scanner.scan(targ,arguments='-sU -p 1-1023')
        print("scan info:",scanner.scaninfo())
        for host in scanner.all_hosts():
            print("HOST :",(host,scanner[host].hostname()))
            print("STATE:",scanner[host].state())
            for proto in scanner[host].all_protocols():
                print("<------------------------>")
                print("protocol :",proto)
            
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    print("port :",port,"state:",scanner[host][proto][port]['state'])
    
    except Exception as e:
        print(Fore.RED+f"error occurred during UDP scan: {e}"+Style.RESET_ALL)

def version_scan():
    try:
        print(Fore.WHITE+f.renderText("VERSION SCAN"))
        targ=input('ENTER YOUR TARGET:')
        scanner.scan(targ,arguments='-sV -p 1-1023')
        print("scaninfo:",scanner.scaninfo())
        for host in scanner.all_hosts():
            print("HOST :",(host,scanner[host].hostname()))
            print("STATE:",scanner[host].state())
            for proto in scanner[host].all_protocols():
                print("<------------------------>")
                print("protocol :",proto)
            
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    service=scanner[host][proto][port]['name']
                    version=scanner[host][proto][port]['version']
                    status=scanner[host][proto][port]['state']
                    reason=scanner[host][proto][port]['reason']
               
                    print("port :",port,',','status :',status,',',"reason :",reason,',',"service :",service,",","version :",version)
               
    except Exception as e:
        print(Fore.RED+f"error occurred during version scan: {e}"+Style.RESET_ALL)    
              
               
def agressive():
    
    try:
        print(Fore.MAGENTA+f.renderText("AGRESSIVE SCAN"))
        targ=input('ENTER YOUR TARGET:')
        scanner.scan(targ,arguments='-A -T4 -sV -vv -p 1-1023')
        print("scaninfo:",scanner.scaninfo())
        for host in scanner.all_hosts():
            print("HOST :",(host,scanner[host].hostname()))
            print("STATE:",scanner[host].state())
            for proto in scanner[host].all_protocols():
                print("<------------------------>")
                print("protocol :",proto)
            
                lport=scanner[host][proto].keys()
            
                for port in lport:
                    service=scanner[host][proto][port]['name']
                    version=scanner[host][proto][port]['version']
                    status=scanner[host][proto][port]['state']
                    reason=scanner[host][proto][port]['reason']
               
                    print("port :",port,',','status :',status,',',"reason :",reason,',',"service :",service,",","version :",version)
               
               
    except Exception as e:  
        print(Fore.RED+f"error occurred during agressive scan: {e}"+Style.RESET_ALL)          
