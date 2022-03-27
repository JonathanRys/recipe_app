#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, url_for
from app import app

# app = create_app()


@app.route("/")
def hello_world():

    sample_data = {
        "bundle": url_for('static', filename='bundle.js'),
        "page": {
            "title": "Test Page"
        }
    }

    return render_template('index.html', **sample_data)

# a simple page that says hello


@app.route('/hello')
def hello():
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
