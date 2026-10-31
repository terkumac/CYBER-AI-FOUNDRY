# A Python Dictionary mapping standard ports to their actual services
port_database = {
    21: "FTP (File Transfer - Often targeted by brute force)",
    22: "SSH (Secure Shell - Remote Linux Administration)",
    53: "DNS (Domain Name Resolution)",
    80: "HTTP (Unencrypted Web Traffic)",
    443: "HTTPS (Secure Encrypted Web Traffic)",
    4444: "Metasploit Default Listener / Potential Malware C2",
    502: "Modbus ICS Protocol (Critical Infrastructure / Power Grid)"
}

print("--- CYBER-AI FOUNDRY: PORT SERVICE ANALYZER ---")

# Scan list of detected ports on a target server
scanned_ports = [22, 80, 4444, 502]

for port in scanned_ports:
    # Use .get() to look up the port description safely from the dictionary
    service = port_database.get(port, "Unknown / Unassigned Port")
    print(f"Port {port}: {service}")
