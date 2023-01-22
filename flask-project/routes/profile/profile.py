from flask import Blueprint, render_template, session, request, redirect, url_for

from ..auth.auth import login_required
from ...models.user import User
from ...models.car import Car
from ...models.auction import Auction

profile = Blueprint("profile", __name__, static_folder="static", template_folder="templates")

@profile.route("/")
@login_required
def get():
    user = User.query.filter_by(id=session["user_id"]).first()
    cars = Car.query.filter_by(owner_id=user.id).all()

    for car in cars:
        auction = Auction.query.filter_by(car_id=car.id).filter_by(status="closed").first()

        print(auction)

        if auction:
            car.price = auction.price
        else:
            car.price = 0

    return render_template("profile.html", user=user, cars=cars)