#!/bin/bash

# declare environment to build for
export ENV=development

# Set server timezone
timedatectl set-timezone America/New_York
# Set the server locale
localectl set-locale LANG=en_US.UTF-8

# ensure apt is up to date
apt update
apt -y upgrade

# declare variables
VAGRANT_HOME=/vagrant
APP_NAME=recipe_app

# install pip and python dependencies
apt update
apt install -y python3-pip python3-dev python3-setuptools
apt install -y build-essential libssl-dev libffi-dev libpcre3 libpcre3-dev

# install nginx
echo '##### Install nginx'
apt update
apt install -y nginx

# remove the symlink for the default nginx configuration
rm /etc/nginx/sites-enabled/default

# copy/decrypt configs
echo '##### Copy configs'
env_file=env_$ENV.sh
mkdir /root/scripts
mkdir /etc/systemd/system/nginx.service.d

cp $VAGRANT_HOME/scripts/$env_file /root/scripts

# copy the setup scripts and make them executable
for file in "copy_configs.sh"; do
    cp $VAGRANT_HOME/scripts/$file /root/scripts/
    chmod -R 700 /root/scripts/$file
done
/root/scripts/copy_configs.sh

# set up the firewall
echo '##### Enable firewall'
ufw allow ssh
ufw allow http
ufw allow 5000 # Flask
ufw --force enable

# create folders for logs
echo '##### Create log folders'
for log_target in "flask" "uwsgi" "react"; do
    mkdir /var/log/$log_target
    chown vagrant:vagrant /var/log/$log_target
done

echo "Server build complete: $(date)"
