#!usr/bin/python
# -*- coding: utf-8 -*-

from flask import render_template, url_for
from elasticsearch_dsl import Search
from .. import app


@app.route("/")
def home():

    try:
        es_search = Search(using=app.es.client, index='test').query('match_all')
        es_data = es_search.execute()
    except Exception as e:
        app.logger.warning('ElasticSearch cannot be found')

    sample_data = {
        "bundle": url_for('static', filename='bundle.js'),
        "page": {
            "title": "Recipe App",
            "data": es_data[0].data
        }
    }

    return render_template('index.html', **sample_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
