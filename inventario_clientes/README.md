# Inventário
Migração do projeto [inventario_clientes](https://github.com/andrejesusdasilva/Python/tree/master/paramiko_proxycomand) para ansible.

# Pré Requisito

Instalar as dependencias com o comando:
* pip3 install -r requirements.txt
# Modo de usar

* Rode a classe main em python e dois arquivos serão gerados localmente, ansible_inventory.conf e config.conf. Vão ser gerados pares
de arquivos para cada clente existente no .csv

* O Conteúdo do arquivo config.conf precisa ser adicionado no arquivo ~/.ssh/config do diretório do host.

* Copie o arquivo ansible_inventory.conf para o diretório /etc/ansible/ ou algum outro diretório de sua preferência

* Rode o comando "ansible-playbook -i <caminho_arquivo_inventorio> <caminho_playbook.yaml>

* No exemplo do arquivo playbook.yml, a receita de comandos irá rodar somente para o host tomcat