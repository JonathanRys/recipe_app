#!/bin/bash

# create soft links for nginx
ln -s /etc/nginx/sites-available/$APP_NAME.conf /etc/nginx/sites-enabled/$APP_NAME.conf

# create a soft link for the flask service
ln -s /lib/systemd/system/$APP_NAME.service /etc/systemd/system/$APP_NAME.service

# start services
systemctl daemon-reload

# start the app
sudo systemctl start $APP_NAME
sudo systemctl enable $APP_NAME

# start nginx
systemctl enable nginx
systemctl reload nginx

# start the NPM build service
sudo systemctl start build_watch
sudo systemctl enable build_watch
