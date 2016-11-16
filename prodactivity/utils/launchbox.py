#! /usr/bin/env python

import datetime
import subprocess
import sys

from prodactivity.utils import dockerlib

dtn = datetime.datetime.now()



REGISTRY = "docker-registry.pdbld.f5net.com"
NAMESPACE = "sandbox"
DATE = "{}{}{}".format(dtn.year, dtn.month, dtn.day)
IMG_NAME = "bbot-master"
TAG = "_".join([REGISTRY, NAMESPACE, IMG_NAME])
NFS_UID = 10007
BBOT_UI_PORT = 8010
BBOT_PB_PORT = 9989
GITLAB_HOST = "bldr-git.int.lineratesystems.com"
GITLAB_SSH_PORT = 22


build_string = 'docker build -t {tag}:{date} '+\
               '--build-arg NFS_UID={nfs_uid} '+\
               '--build-arg BBOT_UI_PORT={bbot_ui_port} '+\
               '--build-arg BBOT_PB_PORT={bbot_pb_port} '+\
               '--build-arg GITLAB_HOST={gitlab_host} '+\
               '--build-arg GITLAB_SSH_PORT={gitlab_ssh_port} '+\
               '{ctxt}'

publish_string = 'docker tag {tag}:{date} {tag}:latest && '+\
                 'docker push {tag}'
def main():
    if sys.argv[1] == 'master-publish':
        print(build_string.format(tag=TAG, date=DATE, nfs_uid=NFS_UID,
                               bbot_ui_port=BBOT_UI_PORT,
                               bbot_pb_port=BBOT_PB_PORT,
                               gitlab_host=GITLAB_HOST,
                               gitlab_ssh_port=GITLAB_SSH_PORT,
                               ctxt=sys.argv[2]))
