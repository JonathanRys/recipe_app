#!/usr/bin/bash

# create a folder for the uWSGI socket file
mkdir /var/run/uwsgi
chown vagrant:vagrant /var/run/uwsgi