from flask import Blueprint, render_template, session, request, redirect, url_for

from ..auth.auth import login_required, get_user
from ...models.user import User
from ...models.car import Car
from ...models.auction import Auction
from ...models.images import Images

import base64

profile = Blueprint("profile", __name__, static_folder="static", template_folder="templates")

@profile.route("/")
@login_required
def get():
    user = get_user()
    cars = Car.query.filter_by(owner_id=user.id).all()

    for car in cars:
        auction = Auction.query.filter_by(car_id=car.id).filter_by(status="closed").first()

        image = Images.query.filter_by(car_id=car.id).first()
        if image:
            car.image = base64.b64encode(image.image).decode('ascii')
            
        if auction:
            car.price = auction.price
        else:
            car.price = 0

    return render_template("profile.html", user=user, cars=cars, cars_owned=len(cars))