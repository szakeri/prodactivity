FROM debian:latest

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y\
     docker.io \
     git \
     make \
     python \
     python-pip \
     ssh \
     sudo &&\
    pip install --upgrade pip 
     git+https://github.com/zancas/prodactivity.git &&\
    rm -rf /var/lib/apt/lists/*
