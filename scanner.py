#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    if "." not in target:
        print("Bukan IP")
        sys.exit()
    for sub in target.split("."):
        if len(sub) > 3:
            print("Invalid IP")
            sys.exit()
else:
    print("Salah")
    print("Syntax : python3 scanner.py <IP>")
    sys.exit()

print("-"*50)
print(f"Scanning {target}")
print(f"Time Started {str(datetime.now())}")
print("-"*50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) # Returns error indicator
        if result == 0:
            print(f"Port {port} is open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except socket.error:
    print("Couldnt connect to server")
    sys.exit()