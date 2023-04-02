#!/bin/bash

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
