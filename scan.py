import nmap
import osdiscovery
import getip
import pingscan
import scaners
from pyfiglet import *
from colorama import *

scanner=nmap.PortScanner()
f=Figlet()
def main():
    print(Fore.RED+f.renderText("PYTHON NMAP SCANER\n"))

    print(Fore.MAGENTA+"\t  \t\t\t\tCREATED BY:GODJOKER\n\n")

    print(Fore.WHITE+"well known ports (0-1023)")
    print("registered ports (1024-49151)")
    print("dynamic ports (49152-65535).")
    print("NMAP VERSION:",scanner.nmap_version())
    
    while True:
        print(Fore.YELLOW+"""CHOOSE OPTION TO SCAN
                 [1] GET WEBSITE IP
                 [2] DISCOVER LIVE HOSTS
                 [3] PING SCAN
                 [4] SYN ACK SCAN
                 [5] UDP SCAN
                 [6] VERSION SCAN
                 [7] AGRESSIVE SCAN
                 [8] OS DISCOVERY
                 [9] EXIT""")
        option=input("ENTER YOUR CHOICE:")
        print("you choosed:",option)
        print("<------------------------------------------------->")
        
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
            exit()
        else:
            print("you entered invalid option")
            
main()