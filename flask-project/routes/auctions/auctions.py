from flask import Blueprint, render_template

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User

auctions = Blueprint("auctions", __name__, static_folder="static", template_folder="templates")

@auctions.route("/", methods=["GET"])
def get():
    auctions = Auction.query.all()

    for auction in auctions:
        car = Car.query.filter_by(id=auction.car_id).first()
        user = User.query.filter_by(id=car.owner_id).first()
        auction.car = car
        auction.car.owner = user

    return render_template("auctions.html", auctions=auctions)