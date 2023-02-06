from ..extensions import db
from ..models.auction import Auction
from ..models.car import Car
from ..models.images import Images

import base64

def get_top_5_auctions():
    auctions = db.session.query(Auction, Car).filter(Auction.status == "active").join(Car, Auction.car_id == Car.id).order_by(Auction.amount_of_bids.desc()).limit(5).all()

    for auction in auctions:
        image = Images.query.filter_by(car_id=auction.Car.id).first().image
        auction.Car.image = base64.b64encode(image).decode('ascii')