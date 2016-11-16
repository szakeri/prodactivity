#!/usr/bin/env bash
set -ex

curdir=$(cd $(dirname $0) && pwd)

if [[ "$1" == "" ]] || [[ "$1" == "-h" ]]; then
    prog=$(basename $0)
    echo "$prog <img>"
    exit 1
else
    img="$1"
fi

source $curdir/bbot_config.sh

#mkdir -p $NFS_BASEDIR
#mkdir -p $NFS_BASEDIR/config
#mkdir -p $NFS_BASEDIR/bbot-master
#mkdir -p $NFS_BASEDIR/bbot-worker
#sudo cp $curdir/bbot_config.sh $NFS_BASEDIR/config/
#sudo cp $curdir/bbot_openrc.sh $NFS_BASEDIR/config/
#sudo chown -R $NFS_UID:$NFS_UID $NFS_BASEDIR

#mkdir -p $RESULTS_BASEDIR
#sudo chown -R $NFS_UID:$NFS_UID $RESULTS_BASEDIR

echo "* starting $img ..."
docker run --rm -it \
    --name bbot-master \
    -p $BBOT_UI_PORT:$BBOT_UI_PORT \
    -p $BBOT_PB_PORT:$BBOT_PB_PORT \
    -p 9090:9090 \
    -v /etc/localtime:/etc/localtime:ro \
    -v $NFS_BASEDIR/bbot-master:/home/buildbot/bbot-master \
    -v $NFS_BASEDIR/config:/home/buildbot/bbot-config \
    $img $2
