FROM docker-registry.pdbld.f5net.com/prodactivity/base:latest

ARG USER_ID
ENV USER_ID=$USER_ID
ARG USER
ENV USER=$USER
COPY entrypoint.sh /tmp/entrypoint.sh
RUN useradd $USER -u $USER_ID -G sudo,docker &&\
    echo $USER' ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers &&\
    chmod 700 /tmp/entrypoint.sh && chown $USER /tmp/entrypoint.sh
WORKDIR /home/$USER
ENTRYPOINT ["/tmp/entrypoint.sh"]
