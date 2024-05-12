# import flask
# this would require use to run flask.Flask(...)

# from library flask import the class Flask
from flask import Flask
from flask import render_template

obj = Flask(__name__)

@obj.route("/")
@obj.route("/index.html")
def hello():
    company_name_update = "foober"
    return render_template('home.html', company=company_name_update)

@obj.route("/login")
# tells flask to execute login() when user goes to /login path of the webpage
def login():
    return "Login Page!!"

obj.run(debug=True)
