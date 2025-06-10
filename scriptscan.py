import nmap
from colorama import Fore
from pyfiglet import Figlet
scanner=nmap.PortScanner()

f=Figlet()

def script_scan():
    print(Fore.LIGHTGREEN_EX+f.renderText("SCRIPT SCAN"))
    print(Fore.LIGHTGREEN_EX+"This scan uses Nmap's scripting engine to run scripts against the target.")
    target=input("Enter the target IP or hostname: ")
    script=input("Enter the script to run (e.g., http-enum, smb-os-discovery): ")
    print(Fore.RESET)
    
    
    try:
        print(Fore.GREEN+f"Running script '{script}' on target '{target}'...")
        print(Fore.RESET)
        
        
        scanner.scan(target,arguments=f"-sV --script {script} -d")
    
    
        for host in scanner.all_hosts():
            print(Fore.GREEN+"Host:",scanner[host].hostname())
            print("State:",scanner[host].state())
            print(Fore.RESET)
            
            for proto in scanner[host].all_protocols():
                print(Fore.GREEN+"<------------------------>")
                print("protocol :",proto)
                print(Fore.RESET)
                lport = scanner[host][proto].keys()
            
                for port in lport:
                    print(Fore.GREEN+"port :",port,"state:",scanner[host][proto][port]['state'])
                    print("name:",scanner[host][proto][port]['name'])   
                    print("product:",scanner[host][proto][port]['product'])
                    print("version:",scanner[host][proto][port]['version'])
                    print(Fore.RESET)
                    
                    try:
                        print(Fore.GREEN+"extrainfo:",scanner[host][proto][port].get('extrainfo', 'N/A'))
                        print("\n\n\n")
                        print(Fore.RESET)
                        script_res = scanner[host][proto][port].get('script', None)
                        
                        if script_res:
                            print(Fore.LIGHTYELLOW_EX+"Script result:")
                            print(Fore.RESET)
                            
                            
                            for script_name, output in script_res.items():
                                print(Fore.GREEN+f"{script_name}: {output}\n")
                                print(Fore.RESET)
                                
                                
                        else:
                            print(Fore.RED+"No script results found for this port.")
                            print("<------------------------>"+Fore.RESET)
                            
                        print(Fore.LIGHTRED_EX+"Script scan completed."+Fore.RESET)
                        
                    except Exception as e:
                        print(Fore.RED+f"An error occurred while retrieving script results: {e}")
                        print("<------------------------>"+Fore.RESET)
                    
                    
    except nmap.PortScannerError as e:
        print(Fore.RED+f"PortScannerError: {e}"+Fore.RESET)
        
    
    except Exception as e:
        print(Fore.RED+f"An error occurred: {e}"+Fore.RESET)
        
    
    
    except KeyboardInterrupt:
        print(Fore.RED + "Script scan interrupted by user." + Fore.RESET)