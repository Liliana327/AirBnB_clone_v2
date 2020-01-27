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


@app.route('/hbnb_filters')
def deploy_hbnb_filters():
    """
    display a HTML page like 6-index.html, 0x01. AirBnB clone
    """
    data = storage.all('State')
    amenity = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=data, amenities=amenity)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
