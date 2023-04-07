#!usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
from pytz import timezone
from elasticsearch_dsl import connections
from elasticsearch_dsl import serializer
from . import config


app = Flask(__name__)

# TO DO
# Connect SQLite

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

app.logger = logger
app.es = {
    'client': 'default',
    'toJSON': serializer.serializer.loads,
    'fromJSON': serializer.serializer.dumps
}

try:
     # Define a default Elasticsearch client
    connections.create_connection(alias=app.es.get('client'), hosts=[config.ES_HOST])
    print(connections.get_connection().cluster.health())
    # @todo Add some preliminary tests here
except Exception as e:

    logger.warning('Cannot connect to Elasticsearch:', e)


### IMPORTS RELYING ON app
# maybe move to it's own
# make sure your editor doesn't move this
from app.controllers import (home)
