#!/usr/bin/python3
"""Start a web application.
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """return hello hbnb.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Return hbnb.
    """
    return "HBNB"


@app.route('/c/<ctext>')
def cisfun(ctext):
    """Return input string.
    """
    return 'C %s' % ctext.replace("_", " ")
