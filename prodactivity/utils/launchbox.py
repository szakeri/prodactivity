#! /usr/bin/env python

import datetime
import subprocess
import sys

from prodactivity.utils import dockerlib

dtn = datetime.datetime.now()



registry = "docker-registry.pdbld.f5net.com"
namespace = "sandbox"
date = "{}{}{}".format(dtn.year, dtn.month, dtn.day)
print(date)
img_name = "bbot-master"
img = "_".join([registry, namespace, img_name])
nfs_uid = 10007
bbot_ui_port = 8010
bbot_pb_port = 9989
gitlab_host = "bldr-git.int.lineratesystems.com"
gitlab_ssh_port = 22


build_string = 'docker build -t $(img):$(date) '+\
               '--build-arg NFS_UID=$(nfs_uid) '+\
               '--build-arg BBOT_UI_PORT=$(bbot_ui_port) '+\
               '--build-arg BBOT_PB_PORT=$(bbot_pb_port) '+\
               '--build-arg GITLAB_HOST=$(gitlab_host) '+\
               '--build-arg GITLAB_SSH_PORT=$(gitlab_ssh_port) '+\
               '.'

publish_string = 'docker tag $(img):$(date) $(img):latest && '+\
                 'docker push $(img)'
def main():
    if sys.argv[1] == 'master-publish':
        print(build_string)
