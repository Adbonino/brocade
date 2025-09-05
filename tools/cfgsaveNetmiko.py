from netmiko import ConnectHandler

device = {
    'device_type': 'brocade_fastiron',  # Para switches Brocade FC
    'host': '10.82.1.90',
    'username': 'admin',
    'password': 'passw0rd',
}

net_connect = ConnectHandler(**device)

# Enviar comando para guardar configuración
output = net_connect.send_command('cfgsave', expect_string=r'Do you want to save')
print(output)

# Confirmar guardado (asumiendo que el prompt pide 'y')
output += net_connect.send_command('y', expect_string=r'#')  
print(output)

net_connect.disconnect()
