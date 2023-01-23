from flask import Blueprint, render_template

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User
from ...models.images import Images
from ...utils.time import get_remaining_time

from ...extensions import db

from datetime import datetime
import base64

auctions = Blueprint("auctions", __name__, static_folder="static", template_folder="templates")

@auctions.route("/", methods=["GET"])
def get():
    auctions = db.session.query(Auction, Car).join(Car, Auction.car_id == Car.id).all()

    for auction in auctions:
        auction.Auction.remaining_time = get_remaining_time(auction.Auction.end_date, auction.Auction.end_time)
        image = Images.query.filter_by(car_id=auction.Auction.car_id).first()
        auction.Auction.image = base64.b64encode(image.image).decode('ascii')

    return render_template("auctions.html", auctions=auctions)