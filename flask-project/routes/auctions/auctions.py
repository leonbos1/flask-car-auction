from flask import Blueprint, render_template

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User
from ...utils.time import get_remaining_time

from datetime import datetime

auctions = Blueprint("auctions", __name__, static_folder="static", template_folder="templates")

@auctions.route("/", methods=["GET"])
def get():
    auctions = Auction.query.all()

    for auction in auctions:
        car = Car.query.filter_by(id=auction.car_id).first()
        user = User.query.filter_by(id=car.owner_id).first()
        auction.car = car
        auction.car.owner = user
        auction.remaining_time = get_remaining_time(auction.end_date, auction.end_time)

    return render_template("auctions.html", auctions=auctions)