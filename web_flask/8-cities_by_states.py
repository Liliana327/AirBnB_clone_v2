#!/usr/bin/python3

'''script that starts a Flask web application
'''

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def current_remove(self):
    """
    request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list')
def display_html():
    """
    display a HTML page
    """
    data = storage.all("State")
    return render_template('7-states_list.html', states=data)


@app.route('/cities_by_states')
def displays_html():
    """
    display cities a HTML page
    """
    data = storage.all("State")
    return render_template('8-cities_by_states.html', states=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
