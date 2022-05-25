# declare environment
export ENV=development
export FLASK_APP=app
export FLASK_ENV=$ENV

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
apt install -y python3-pip python3-dev
apt install -y build-essential libssl-dev libffi-dev python3-setuptools libpcre3 libpcre3-dev

# install nginx
apt update
apt install -y nginx

# copy/decrypt configs
env_file=env_$ENV.sh
mkdir /root/scripts
mkdir /etc/systemd/system/nginx.service.d

cp $VAGRANT_HOME/scripts/$env_file /root/scripts

# copy the setup scripts and make them executable
for file in "copy_configs.sh"; do
    cp $VAGRANT_HOME/scripts/$file /root/scripts
    chmod -R 700 /root/scripts/$file
    /root/scripts/$file
done

# create soft links for nginx
ln -s /etc/nginx/sites-available/$APP_NAME.conf /etc/nginx/sites-enabled/$APP_NAME.conf

# create a soft link for the flask service
ln -s /lib/systemd/system/$APP_NAME.service /etc/systemd/system/$APP_NAME.service

# install a virtual environment to run Flask in
apt install -y python3-venv
cd $VAGRANT_HOME
python3 -m venv $APP_NAME-venv
source ./$APP_NAME-venv/bin/activate

# install python libraries
pip3 install -r $VAGRANT_HOME/$APP_NAME/requirements.txt
pip3 install uwsgi

deactivate

# set up the firewall
ufw allow ssh
ufw allow http
ufw allow 5000 # Flask
ufw --force enable

# This script sets up the directory structure and permissions for the app
#   - Runs on reboot via app_setup.service
bash $VAGRANT_HOME/scripts/app_setup.sh

# start services
systemctl daemon-reload

# enable the reboot setup service
systemctl enable app_setup

# start the app
sudo systemctl start $APP_NAME
sudo systemctl enable $APP_NAME

# start nginx
systemctl start nginx
systemctl enable nginx

# clean up
