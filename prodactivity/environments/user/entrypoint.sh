#!/bin/bash
eval `ssh-agent -s`
for k in ~/ssh_keys/*; do
  [ -f $k ] && ssh-add $k
done
. ${HOME}/.prodactivity/openrc.sh
if [ ${#@} == 0 ]; then
  exec bash
else
  exec "$@"
fi
