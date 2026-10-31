# Python & Data Science Arsenal

## Day 2 — Core Syntax, Functions & Conditional Logic (Kaggle Lessons 1–3)
* `type(x)` — Inspects the data type of a variable (`int`, `float`, `str`, `bool`).
* `//` vs `%` — Floor division (`//` drops the decimal remainder) and Modulo (`%` returns only the remainder, heavily used in cryptography and hashing).
* `help(fn)` — Displays the docstring and arguments of any built-in or custom function.
* `def function_name(arg1, arg2=default):` — Defines a reusable code block; `return` passes the computed output back to the caller.
* `if / elif / else` & Booleans (`and`, `or`, `not`) — Controls execution flow based on security conditions or data thresholds.

## Day 4 — Lists, Loops & Security Filtering
* **Lists (`[]`)** — Ordered sequences used to hold collections of ports, IP addresses, or log entries (e.g., `open_ports = [22, 80, 443, 502]`).
* **Indexing & Slicing** — `list[0]` grabs the first item; `list[-1]` grabs the last item; `list[0:2]` slices a subset.
* **`for` Loops & Membership (`in`)** — Iterates through every item in a collection and checks membership against a threat list (`if port in backdoor_ports:`).
* **List Comprehensions** — Filters a list in a single line: `alerts = [p for p in open_ports if p in backdoor_ports]`.

## Day 5 — Python Libraries & Custom Socket Port Scanner
* **`import socket`** — Python’s native interface to the operating system's networking stack, allowing scripts to build TCP/UDP sockets and resolve DNS.
* **`socket.AF_INET & SOCK_STREAM`** — Flags used to instantiate a standard IPv4 (`AF_INET`) TCP (`SOCK_STREAM`) socket descriptor.
* **`s.connect_ex((host, port))`** — Attempts a TCP connection handshake; returns `0` if successful (port is open) or an error code if closed.
* **`s.settimeout(seconds)`** — Prevents network scripts from hanging indefinitely by setting a hard time limit on socket operations.
