# web_app/routes/home_routes.py
# how to set and run flask - https://github.com/Microsoft/vscode-docs/issues/1881

from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("prediction_form.html")

@home_routes.route("/hello")
def hello(parameter_list):
    print("VISITING THE HOMEPAGE")
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    print("VISITING THE HOMEPAGE")
    return "About me"

