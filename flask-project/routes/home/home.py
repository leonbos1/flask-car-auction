from flask import Blueprint, render_template

from ...extensions import db
from ...models.auction import Auction
from ...models.car import Car

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home.route("/")
def get():
    auctions = Auction.query.order_by(Auction.amount_of_bids.desc()).limit(5).all()

    #join the auction table with the car table
    auctions = db.session.query(Auction, Car).join(Car, Auction.car_id == Car.id).all()

    return render_template("home.html", auctions=auctions)


