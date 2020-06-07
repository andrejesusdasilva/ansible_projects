# Objetivo
Migração do projeto [GitHub](https://github.com/andrejesusdasilva/Python/tree/master/paramiko_proxycomand) para o Ansible

# Pré Requisitos

* Instalar o ansible (testado com a versão 2.9.9);
* Copiar o arquivo "hosts_tomcat"  para /etc/ansible. Salvar o arquivo playbook.yaml em algum local;
* Arquivo ~/.ssh/config com as entradas configuradas para que o "Jump" funcione (ainda em teste);


# Modo de usar

* ansible-playbook -i /etc/ansible/hosts_tomcat ~/Desktop/inventario_ansible/playbook.yaml


# Resultado esperado

* Arquivos de log gerado localmente, com o resultado dos comandos executados no servidor.