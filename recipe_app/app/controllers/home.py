#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, url_for
from .. import app


@app.route("/")
def hello():
    return "<h1 style='color:blue; margin:10px'>Hello There!</h1>"


@app.route("/test")
def test_page():

    sample_data = {
        "bundle": url_for('static', filename='bundle.js'),
        "page": {
            "title": "Test Page"
        }
    }

    return render_template('index.html', **sample_data)




@app.route('/hello')
def say_hello():
    """
    A simple page that says hello
    """
    return '<p>Hello, World!</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
