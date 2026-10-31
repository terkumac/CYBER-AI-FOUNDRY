import re

logs = [
    "Oct 31 22:10:01 sshd[101]: Failed password for root from 197.210.55.12 port 22",
    "Oct 31 22:11:15 sshd[102]: Accepted password for ceetee from 10.85.47.6 port 54321",
    "Oct 31 22:12:40 sshd[103]: Failed password for admin from 45.33.32.156 port 39210",
    "Oct 31 22:14:00 sshd[104]: Disconnected from user ceetee 10.85.47.6 port 54321"
]

for line in logs:
    if "Failed password" in line:
        match = re.search(r'from ([\d\.]+)', line)
        if match:
            attacker_ip = match.group(1)
            print(f"[!] ALERT: Brute-force attempt from {attacker_ip}")
