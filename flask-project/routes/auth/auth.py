from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from functools import wraps
import flask_login

from ...extensions import db
from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User

auth = Blueprint("auth", __name__, static_folder="static",
                 template_folder="templates")

login_manager = flask_login.LoginManager()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not flask_login.current_user.is_authenticated:
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

def get_user():
    return flask_login.current_user

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for("auth.login"))

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))

    flask_login.login_user(user)
    return redirect(url_for("profile.get"))

@auth.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    email = request.form.get("email")
    password = request.form.get("password")
    username = request.form.get("username")

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for("auth.register"))

    new_user = User(email=email, username=username, password=password)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))