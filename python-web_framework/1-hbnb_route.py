#!/usr/bin/env python3
"""
Starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when accessing root."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB' when accessing /hbnb."""
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
