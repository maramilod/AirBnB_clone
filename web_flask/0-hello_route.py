#!/usr/bin/python3
""" starts a flask web app
"""
from flask import Flask


app = Flask(__name__)


# Define the route
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays 'Hello HBNB!' """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
