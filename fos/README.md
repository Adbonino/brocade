# Brodace.fos


Ejemplo de ejecución (local):

```
ansible-playbook -i localhost, -e "fos_ip_addr=192.0.2.10 fos_user_name=admin fos_password=TuPassword" get_brocade_facts_local.yml
```

Ekemplo de ejecución (httpapi):

NOTA: antes de ejecutarlo cambiar IP, USER y PASSWORD en el archiv de inventairo inventory_httpapi.yml

```
ansible-playbook -i inventory_httpapi.yml get_brocade_facts_httpapi.yml
```
