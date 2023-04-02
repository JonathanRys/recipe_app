#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from pytz import timezone

app = Flask(__name__)


# TO DO
# Connect SQLite
# Connect ElasticSearch


# set app timezone
app.timezone = timezone('US/Eastern')


### LOGGING
handler_options = {
    'development': {
        'maxBytes': 2048,
        'backupCount': 5
    },
    'production': {
        'maxBytes': 2048,
        'backupCount': 5
    }
}

if app.debug:
    logging_options = handler_options['development']
else:
    logging_options = handler_options['production']

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if app.debug else logging.WARNING )

handler = RotatingFileHandler('/var/log/flask/flask.log', **logging_options)

# create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to console_handler
console_handler.setFormatter(formatter)

# add console_handler to logger
logger.addHandler(console_handler)


### IMPORTS RELYING ON app
# make sure your editor doesn't move this
from app.controllers import (home)
