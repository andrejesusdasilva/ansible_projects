# Objetivo
Projeto simples para utilizar o ansible em servidores em docker. Isso não é uma recomendação, é simplesmente um lab.

# Pré Requisitos

* Docker, Docker-Compose e Ansible no mesmo host;
* No arquivo (para esta versão) adicionar as suas chaves publicas/authorized_keys para serem levadas para dentro do container;


# Modo de usar

* Buildar a imagem com o comando: docker-compose build --no-cache;
* Escalar os containers: docker-compose scale ubuntu=4;
* Pegar os ips dos container via docker inspect <container_name> | grep IP;

# Configurando o ansible
* Configurar o arquivo de hosts com os ips dos containers;


# Executando o ansible

* export ANSIBLE_HOST_KEY_CHECKING=False
* ansible-playbook -i hosts plabook_hml.yml

# Resultado esperado

* Devem ter outras formas mais práticas de fazer isso, mas eu não gosto de usar o ansible via localhost na minha máquina.
* O ideal é ter várias distribuições em containers para fazer testes