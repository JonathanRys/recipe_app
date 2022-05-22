#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

#make sure your editor doesn't move this
from app.controllers import (test)
