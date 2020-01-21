#!/usr/bin/python3

''' script that starts a Flask web application
'''
from flask import Flask, render_template

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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """print python(text)"""
    replace_ptext = text.replace("_", " ")
    return 'Python {}'.format(replace_ptext)


@app.route('/number/<int:n>')
def numbers(n):
    """print a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_whole(n):
    """return html if is number entero"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd(n):
    """return html if is number entero"""
    if (n % 2 == 0):
        text = "is even"
        return render_template("6-number_odd_or_even.html", n=n, text=text)
    else:
        text = "is odd"
        return render_template("6-number_odd_or_even.html", n=n, text=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
