from flask import Blueprint, render_template
import base64

from ...extensions import db
from ...models.auction import Auction
from ...models.car import Car
from ...models.images import Images

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home.route("/")
def get():
    auctions = db.session.query(Auction, Car).join(Car, Auction.car_id == Car.id).order_by(Auction.amount_of_bids.desc()).limit(5).all()

    for auction in auctions:
        image = Images.query.filter_by(car_id=auction.Car.id).first().image
        auction.Car.image = base64.b64encode(image).decode('ascii')

    return render_template("home.html", auctions=auctions)


