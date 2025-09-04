sudo dnf install python3-pip -y

pip3 install paramiko

ansible-playbook playbook_cfgsave.yml \
  --extra-vars "brocade_ip=192.168.1.100 brocade_user=admin brocade_pass=passw0rd"

