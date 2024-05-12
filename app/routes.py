from flask import render_template
from flask import flash
from flask import redirect
from app import obj

from app.models import Ticket, Route, Flight
from app import db


@obj.route("/")
def home_page():
    return render_template("home.html")

@obj.route("/flights")
def flights_page():
    return render_template("flights.html")
