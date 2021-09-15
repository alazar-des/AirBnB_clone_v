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


if __name__ == "__main__":
    app.run()
