from flask import render_template
from flask import flash
from flask import redirect
from app import obj

from app.models import User, Post
from app import db


@obj.route("/")
@obj.route("/index.html")
def home_page():
    return render_template("home.html")

@obj.route("/flights")
def flights_page():
    return render_template("flights.html")
