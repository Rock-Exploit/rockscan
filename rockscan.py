import os
print('''
██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗░█████╗░░█████╗░███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔══██╗████╗░██║
██████╔╝██║░░██║██║░░╚═╝█████═╝░╚█████╗░██║░░╚═╝███████║██╔██╗██║
██╔══██╗██║░░██║██║░░██╗██╔═██╗░░╚═══██╗██║░░██╗██╔══██║██║╚████║
██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗██████╔╝╚█████╔╝██║░░██║██║░╚███║
╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝
''')
print("1-webinfo")
print("2-ipscan")
nm=int(input("Enter number:"))
if nm ==1:
      domin=input("Enter domin:")
      os.system("dmitry -w -s -e " + domin)
elif nm == 2:
    print("1-network scan")
    print("2-port scan")
    print("3-system scan")
scan=int(input("Enter number:"))
ip=input("Enter your ip :")
if scan ==1:
      os.system("nmap -sn " + ip)
elif scan ==2:
        os.system("nmap -sV -Pn " + ip)
elif scan ==3:
        os.system("sudo nmap -sS -sV -Pn --script vuln " + ip)
