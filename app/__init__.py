# import flask
# this would require use to run flask.Flask(...)

# from library flask import the class Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

pathname = os.path.abspath(os.path.dirname(__file__))

obj = Flask(__name__)

obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # where the database file will be stored
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(pathname, 'app.db')

)

db = SQLAlchemy(obj)

with obj.app_context():
    from app.models import Ticket, Route, Flight, Airport
    db.create_all()

    from app.fake_db import add_routes, add_flights, add_airports
    add_routes()
    add_flights()
    add_airports()

from app import routes
