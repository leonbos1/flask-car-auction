from flask import Blueprint, render_template

parts = Blueprint("parts", __name__, static_folder="static", template_folder="")

def nav_bar():
    return render_template("navbar.html")