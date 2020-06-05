# web_app/routes/home_routes.py
# how to set and run flask - https://github.com/Microsoft/vscode-docs/issues/1881

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    return "About me"

