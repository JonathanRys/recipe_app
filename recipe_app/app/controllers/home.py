#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, url_for
from .. import app


@app.route("/")
def home():

    sample_data = {
        "bundle": url_for('static', filename='bundle.js'),
        "page": {
            "title": "Recipe App"
        }
    }

    return render_template('index.html', **sample_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
