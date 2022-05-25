#!usr/bin/python
# -*- coding: utf-8 -*-

from app import app


if __name__ == "__main__":
    if not app.config.get('LIVE'):
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        app.run()
