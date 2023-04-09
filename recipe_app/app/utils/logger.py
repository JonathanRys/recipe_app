#!usr/bin/python
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

def make_logger(logging_options):
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

    return logger
