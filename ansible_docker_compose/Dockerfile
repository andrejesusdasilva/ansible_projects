FROM ubuntu:latest

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    openssh-server \
    python \
    sudo \
    curl \
    vim \
    net-tools \
    wget \
    && mkdir -p /var/run/sshd \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' ansible \
  &&  echo "ansible:ansible" | chpasswd \
  &&  adduser ansible sudo \
  &&  echo '%ansible ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
  && mkdir -p /home/ansible/.ssh

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
