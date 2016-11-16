#! /usr/bin/env python

import datetime
from docker import Client
import sys

from prodactivity.utils import dockerlib

dtn = datetime.datetime.now()



REGISTRY = "docker-registry.pdbld.f5net.com"
NAMESPACE = "sandbox"
DATE = "{}{}{}".format(dtn.year, dtn.month, dtn.day)
IMG_NAME = "bbot-master"
TAG = "_".join([REGISTRY, NAMESPACE, IMG_NAME])
buildargs = {'NFS_UID': '10007',
             'BBOT_UI_PORT': '8010',
             'BBOT_PB_PORT': '9989',
             'GITLAB_HOST': 'bldr-git.int.lineratesystems.com',
             'GITLAB_SSH_PORT': '22'}


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
    cli = Client(base_url='unix://var/run/docker.sock')
    if sys.argv[1] == 'publish_bb_master':
        build_image = \
            cli.build(buildargs=buildargs, tag='zartesttag',path=sys.argv[2])
        for o in build_image:
            print(o) 
        
