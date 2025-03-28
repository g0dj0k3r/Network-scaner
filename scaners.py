import nmap
import osdiscovery
import getip
import pingscan
from pyfiglet import *
from colorama import *

scanner=nmap.PortScanner()
f=Figlet()



def live_hosts():
    print(Fore.LIGHTBLUE_EX+f.renderText("LIVE HOST DISCOVER"))
    print(Fore.LIGHTBLUE_EX+"TARGET SPECIFICATION: \n1:192.168.0.0-255 \n2:192.168.0.0/24")   
    targ=input('ENTER YOUR TARGET:')
    scanner.scan(targ,arguments='-sn')

    for host in scanner.all_hosts():
        if scanner[host].state()=='up':
            print('LIVE HOSTS :',host,scanner[host].hostname())
            
        else:
            print("0 HOST ALIVE")

def syn_scan():
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
                
            
            
def udp_scan():
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
    

def version_scan():
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
               
               
              
               
def agressive():
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
               
               
               
