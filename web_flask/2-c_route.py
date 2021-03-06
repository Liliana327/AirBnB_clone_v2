#!/usr/bin/python3

''' script that starts a Flask web application
'''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """print hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """print HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def C_text(text):
    """print /c/<text>"""
    replace_text = text.replace("_", " ")
    return 'C {}'.format(replace_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
