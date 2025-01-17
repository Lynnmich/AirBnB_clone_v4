#!/usr/bin/python3
""" Starts a Flash Web Application """
import os
import uuid
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template

app = Flask(__name__)
app.url.map.strict_slashes = False
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

"""If 100-hbnb.html is not present, use 8-hbnb.html"""
template_path = "web_dynamic/0-hbnb.html"
if not os.path.exists(template_path):
    template_path = "web_flask/templates/8-hbnb.html"


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb')
def hbnb():
    """ HBNB is alive! """
    cache_id = str(uuid.uuid4())
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template(template_path,
                           cache_id=cache_id,
                           states=st_ct,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
