#!usr/bin/python
# -*- coding: utf-8 -*-

from app import app

# from app.controllers import (test)
# from flask import Flask
# app = Flask(__name__, static_folder='www')


# @app.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    if not app.config.get('LIVE'):
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run()
