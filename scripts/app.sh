# declare environment
export ENV=dev
export FLASK_APP=app
export FLASK_ENV=development

# ensure apt is up to date
apt update
apt -y upgrade

# declare variables
NVM_VERSION=0.39.1
VAGRANT_HOME=/vagrant

# install pip
apt update
apt install -y python3-pip

# install a virtual environment to run Flask in
# pip3 install virtualenv
# virtualenv recipe_app
# source recipe_app/bin/activate

# install python libraries
pip3 install -r $VAGRANT_HOME/config/requirements.txt

# install nginx
apt update
apt install -y nginx

# install NVM
apt update
apt install -y build-essential libssl-dev
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v$NVM_VERSION/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# install node
nvm install 16

# copy/decrypt configs
mkdir /root/scripts
env_file=./scripts/env_$ENV.sh
echo ###### Please enter the decryption password:
gpg --decrypt $env_file --pinentry-mode loopback --passphrase-fd 0 > /root/scripts/$env_file
cp /vagrant/scripts/decrypt.sh /root/scripts
chmod +x /root/scripts/decrypt.sh
./

# create soft links for nginx
ln -s /etc/nginx/sites-available/recipe_app.conf /etc/nginx/sites-enabled/recipe_app.conf

# create a soft link for the flask service
sudo ln -s /lib/systemd/system/recipe_app.service /etc/systemd/system/recipe_app.service

# start services
systemctl enable nginx
systemctl enable recipe_app
systemctl daemon-reload

# clean up
