#!/bin/bash

# Script to install project dependencies and build the react app
#   This script should not be run as root

# install node, git, and npm
sudo apt update

# install NVM
wget -qO- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# install node
nvm install 16
# update npm
npm install -g npm@latest

sudo apt install -y nodejs git

# install dependencies
cd /var/www/app/app/static/recipe_app
npm install

# build the React app
npm run build
