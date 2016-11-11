FROM ubuntu:16.10

RUN DEBIAN_FRONTEND=noninteractive apt-get update &&\
    apt-get install -y\
     ssh make git python python-pip docker.io sudo &&\
    pip install --upgrade pip 
     git+https://github.com/zancas/prodactivity.git &&\
    rm -rf /var/lib/apt/lists/*
