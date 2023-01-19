from flask import Blueprint, render_template

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home.route("/")
def get():
    return render_template("home.html")


