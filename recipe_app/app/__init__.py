#!usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask
from pytz import timezone
from . import config

from .utils.logger import make_logger
from .utils.elasticsearch import ES

app = Flask(__name__)

# TO DO
# Connect SQLite

# set app timezone
app.timezone = timezone('US/Eastern')
app.config.from_pyfile('config.py')

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

app.logger = make_logger(logging_options)

try:
    app.es = ES(host=app.config['ES_HOST'])
    print(app.es.connection.cluster.health())
    # @todo Add some preliminary tests here
    # Load data

except Exception as e:
    app.logger.warning('Cannot connect to Elasticsearch:', e)


### IMPORTS RELYING ON app
# make sure your editor doesn't move this
from app.controllers import (home)
