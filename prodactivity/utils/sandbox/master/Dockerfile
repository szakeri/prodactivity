FROM ubuntu:16.04

# - declare build args
ARG NFS_UID
ARG BBOT_UI_PORT
ARG BBOT_PB_PORT
ARG GITLAB_HOST
ARG GITLAB_SSH_PORT

# - first, install OS package dependencies (and clean up)
# - then create the buildbot user
RUN apt-get update \
    && apt-get install -y \
        curl \
        git \
        python-dev \
        python-pip \
        sqlite3 libsqlite3-dev \
        vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && useradd --uid $NFS_UID buildbot

# - set working dir
WORKDIR /home/buildbot

# - create output directories
RUN mkdir ./bbot-config \
    && mkdir ./bbot-master

# - upload config files
COPY requirements.txt ./
COPY setup_master.sh ./
COPY master.cfg ./

# - install testlab private key for buildbot user and root user
COPY id_rsa_testlab ./.ssh/id_rsa
COPY id_rsa_testlab /root/.ssh/id_rsa

RUN chmod 600 ./.ssh/id_rsa \
    && ssh-keyscan -p $GITLAB_SSH_PORT $GITLAB_HOST >> ./.ssh/known_hosts \
    && chown -R buildbot:buildbot ./ \
    && chmod 600 /root/.ssh/id_rsa \
    && ssh-keyscan -p $GITLAB_SSH_PORT $GITLAB_HOST >> /root/.ssh/known_hosts \
    && pip install -U pip \
    && pip install -r requirements.txt

# - set default user
USER buildbot

# - expose ports
EXPOSE $BBOT_UI_PORT $BBOT_PB_PORT

# - set default "on start" command
CMD ["/home/buildbot/setup_master.sh"]
