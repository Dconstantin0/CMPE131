from flask import render_template
from flask import flash
from flask import redirect
from app import obj

from app.models import Ticket, Route, Flight, Airport
from app import db


@obj.route("/")
def home_page():
    # Retrieve all airports from the database
    all_airports = Airport.query.all()

    return render_template("home.html", airports=all_airports)

@obj.route("/flights")
def flights_page():
    return render_template("flights.html")
