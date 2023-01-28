from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from functools import wraps

from ...extensions import db
from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User

auth = Blueprint("auth", __name__, static_folder="static",
                 template_folder="templates")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("auth.login", next=request.url))
        else:
            user = User.query.filter_by(id=session["user_id"]).first()
            if user is None:
                return redirect(url_for("auth.login", next=request.url))

        return f(*args, **kwargs)
    return decorated_function


@auth.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not password == user.password:
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))

    login_user(user)

    return redirect(url_for("auctions.get"))


@auth.route("/register", methods=["GET"])
def register():
    error_message = request.args.get("error_message")

    return render_template("register.html", error_message=error_message)


@auth.route("/register", methods=["POST"])
def register_post():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if user:
        error_message = "Username already exists"
        return redirect(url_for("auth.register", error_message=error_message))

    user = User(username=username, email=email, password=password, wallet=0)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auctions.get"))

@auth.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


def login_user(user):
    session.clear()
    session["user_id"] = user.id


def logout_user():
    session.clear()


def is_logged_in():
    return session.get("user_id") is not None
