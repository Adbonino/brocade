import paramiko
import time
import sys

# Recoger argumentos desde Ansible
if len(sys.argv) != 4:
    print("Uso: ejecutar_cfgsave.py <ip> <usuario> <password>")
    sys.exit(1)

host = sys.argv[1]
usuario = sys.argv[2]
clave = sys.argv[3]

# Resto del código igual...
cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cliente.connect(hostname=host, username=usuario, password=clave, look_for_keys=False, allow_agent=False)

shell = cliente.invoke_shell()
time.sleep(1)

if shell.recv_ready():
    shell.recv(1000)

shell.send("cfgsave\n")
time.sleep(2)

output = shell.recv(5000).decode('utf-8')
print(output)

if "Do you want to save" in output:
    shell.send("y\n")
    time.sleep(1)

if "password:" in output.lower():
    shell.send(clave + "\n")
