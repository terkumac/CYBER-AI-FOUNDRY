# Linux Command Arsenal

## Day 1 — File System, Redirection & Remote SSH (Bandit 0–5)
* `mkdir -p` — Creates parent and child directories at the same time.
* `touch` — Creates an empty plain-text file (0 bytes).
* `echo "text" > file` — Redirects text output into a file (overwrites).
* `ls -la` — Lists all files in long format, exposing hidden dot-files (.) and permissions.
* `cat ./-` — Reads a file starting with a dash by specifying the current directory (./).
* `cat "./--spaces--"` — Reads files with spaces and leading dashes by wrapping the path in quotes.
* `file ./*` — Inspects the magic bytes of all files in a folder to find human-readable ASCII text.
* `ssh user@host -p 2220` — Connects to a remote server over an encrypted shell on a custom port.

## Day 2 — File Sizing & Line Counting
* `ls -lhA` — Lists all files with human-readable sizes (`-h`) and hidden files (`-A`), hiding `.` and `..`.
* `wc file.md` — Outputs line count, word count, and byte size of a file.

## Day 3 — Network Interfaces, Routing & Socket Auditing
* `ip -br a` — Displays a brief summary of network interfaces, operational state (UP/DOWN), and assigned IP addresses.
* `ip r` — Displays the kernel routing table and default gateway IP.
* `ss -tuln` — Audits all active listening (`-l`) TCP (`-t`) and UDP (`-u`) numeric ports (`-n`) on the local machine.
* `sudo ss -tulnp` — Reveals the exact Process ID (`pid`) and binary name owning each listening TCP/UDP socket (requires `sudo` to inspect root-owned daemons).
* `sudo tcpdump -n -c 4 host 1.1.1.1` — Captures 4 raw network packets (`-c 4`) to/from a target IP without DNS resolution delays (`-n`).
* `ip neigh` — Displays the local ARP (Address Resolution Protocol) cache mapping local IPv4 addresses to physical MAC (`lladdr`) addresses.
* **DHCP (DORA Sequence)** — Discover -> Offer -> Request -> Acknowledge (how a host dynamically leases an IP address on a LAN).
* **ARP Resolution** — Broadcasts a request (`Who has IP?`) across the local subnet to discover the target's Layer-2 MAC address before sending frames.

## Day 4 — Filesystem Hunting, Pipes & Stream Redirection (Bandit 5 -> 10)
* `find . -type f -size 1033c ! -executable` — Searches current directory for regular files (`-type f`) of exact byte size (`1033c`) that are not executable.
* `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null` — Hunts across the entire root filesystem (`/`) by owner/group while redirecting permission errors (`2>`) to `/dev/null`.
* `grep "pattern" file.txt` — Searches a file and prints only the lines matching a specific text string or regular expression.
* `sort data.txt | uniq -u` — Sorts lines alphabetically and pipes (`|`) the output to `uniq -u` to isolate the single unique line in a dataset.
* `strings data.txt | grep "==="` — Extracts human-readable ASCII strings from raw binary data and filters for specific markers.
