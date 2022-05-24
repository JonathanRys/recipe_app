# declare environment
export ENV=development
export FLASK_APP=app
export FLASK_ENV=$ENV

# ensure apt is up to date
apt update
apt -y upgrade

# declare variables
NVM_VERSION=0.39.1
VAGRANT_HOME=/vagrant
APP_NAME=recipe_app

# install pip and python dependencies
apt update
apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools


# install node and npm
apt update
apt install -y nodejs

# install a virtual environment to run Flask in
# pip3 install virtualenv
# virtualenv $APP_NAME
# source $APP_NAME/bin/activate

# option 2 for virtual env
apt install -y python3-venv
mkdir ~/$APP_NAME
cd ~/$APP_NAME
python3 -m venv $APP_NAME
source $APP_NAME/bin/activate

# install python libraries
pip3 install -r $VAGRANT_HOME/$APP_NAME/requirements.txt

# install nginx
apt update
apt install -y nginx

# install NVM
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v$NVM_VERSION/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# install node
nvm install 16
# update npm
npm install -g npm@latest

# copy/decrypt configs
env_file=env_$ENV.sh
mkdir /root/scripts
mkdir /etc/systemd/system/nginx.service.d

cp /vagrant/scripts/$env_file /root/scripts

# copy the setup scripts and make them executable
for file in "copy_configs.sh"; do
    cp /vagrant/scripts/$file /root/scripts
    chmod -R 700 /root/scripts/$file
    /root/scripts/$file
done

# create soft links for nginx
ln -s /etc/nginx/sites-available/$APP_NAME.conf /etc/nginx/sites-enabled/$APP_NAME.conf

# create a soft link for the flask service
ln -s /lib/systemd/system/$APP_NAME.service /etc/systemd/system/$APP_NAME.service

# set up the firewall
ufw allow ssh
ufw allow http
ufw allow 5000 # Flask
ufw --force enable

# start services
systemctl enable nginx
systemctl enable $APP_NAME
systemctl daemon-reload

# install dependencies
cd /var/www/app/app/static/recipe_app
npm install

# build the React app
# npm run build
# npx webpack build --config ./webpack.config.js --stats verbose

# start the app
cd /var/www/app
python3 run.py

# clean up
reboot
