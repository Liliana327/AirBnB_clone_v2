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


@app.route('/hbnb')
def hbnb_display():
    """
    display a HTML page.
    """
    data = storage.all('State')
    amenity = storage.all('Amenity')
    place = storage.all('Place')
    return render_template('100-hbnb.html', states=data, amenities=amenity,
                           places=place)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
