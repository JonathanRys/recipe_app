#!/bin/bash

# Script to install project dependencies and build the app
#   This script should not be run as root

### Python dependencies
# declare variables
export FLASK_APP=app
export FLASK_ENV=$ENV

# install a virtual environment to run Flask in
pip3 install virtualenv --user
cd $VAGRANT_HOME
# the --always-copy flag makes virtualenv copy files instead of symlinking
#   it is required to prevent a bug on Windows:
#   https://github.com/gratipay/gratipay.com/issues/2327
python3 -m virtualenv -p python3 $APP_NAME-venv --always-copy
# activate the virtual environment
source ./$APP_NAME-venv/bin/activate

# install python libraries
pip3 install -r $VAGRANT_HOME/$APP_NAME/requirements.txt
pip3 install uwsgi
deactivate

### React dependencies
sudo apt update

# install NVM
wget -qO- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# install node
nvm install 16.20.0
# update npm
npm install -g npm@latest

# install git
sudo apt install -y nodejs git

# install dependencies
cd /var/www/app/app/static/$APP_NAME
# vagrant cannot create symlinks in shared folders under Windows 10
# @dev
npm install --no-bin-links
# @prod
# npm install

# the build_watch service will build the React app so no need to do it here
