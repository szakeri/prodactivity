#!/usr/bin/env bash
set -ex

# - note that $config_dir and $log_dir are volumes that are mounted at runtime
config_dir="/home/buildbot/bbot-config"
log_dir="/home/buildbot/bbot-master"

# - use "-a" to automatically export variable definitions
set -a
source $config_dir/bbot_config.sh
set +a

# - $BBOT_BASEDIR points to an existing buildbot master basedir that we want
#   to reuse
# - if no $BBOT_BASEDIR value is provided, then we create a brand new buildbot
#   master basedir
if [[ -z $BBOT_BASEDIR ]]; then
    # - create time-stamped output dir
    date_dir=$(date +"%Y/%m")
    timestamp=$(date +"%Y%m%d-%H%M%S")
    rel_dir=$date_dir/$timestamp-master
    base_dir=$log_dir/$rel_dir
    mkdir -p $base_dir

    # - create symlink to "latest"
    cd $log_dir
    if [[ -e latest ]]; then
        rm latest
    fi
    ln -s ./$rel_dir latest
else
    base_dir=$log_dir/$BBOT_BASEDIR
    pid_file=$base_dir/twistd.pid
    if [[ -e $pid_file ]]; then
        rm $pid_file
    fi
fi


# - move the master config files into the newly created base_dir
cd $base_dir
mv /home/buildbot/master.cfg ./

# - create the change hook auth file
echo "$BBOT_HOOK_USER:$BBOT_HOOK_PASS" > changehook.passwd

# - we instantiate the master inside an externally mounted directory so
#   that we can access the master logs from outside the container (and
#   persist them after the container is stopped/removed)
if [[ -z $BBOT_BASEDIR ]]; then
    buildbot create-master --log-count=$BBOT_LOG_COUNT --relocatable .
else
    # --force means "reuse existing master directory"
    buildbot create-master --log-count=$BBOT_LOG_COUNT --force .
    buildbot reconfig
fi

# - start tailing the log file (and background that process) *before* we call
#   "exec" so that "docker logs" will return useful data if/when we need to
#   use it
touch twistd.log
tail -F twistd.log &
disown
exec buildbot start --nodaemon
