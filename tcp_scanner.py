import socket
import sys
from datetime import datetime

# Target to scan (we'll scan localhost 127.0.0.1 safely)
target_host = "127.0.0.1"

# Common ports to check: SSH (22), DNS (53), HTTP (80), CUPS (631), HTTPS (443)
ports_to_scan = [22, 53, 80, 443, 631, 3306, 8080]

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)

try:
    for port in ports_to_scan:
        # 1. Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so the script doesn't hang forever on closed ports (1 second)
        s.settimeout(1.0)
        
        # 2. Try to connect to the target IP and port
        # connect_ex returns 0 if the connection succeeded (port is open)
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: Closed")
            
        # 3. Always close the socket socket descriptor when done
        s.close()

except KeyboardInterrupt:
    print("\nExiting script...")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()

print("-" * 50)
print("Scan complete.")
