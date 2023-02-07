from ..extensions import db
from ..models.auction import Auction
from ..models.car import Car
from ..models.images import Images

from ..utils.time import get_remaining_time

import base64

def get_top_5_auctions():
    auctions = db.session.query(Auction, Car).filter(Auction.status == "active").join(Car, Auction.car_id == Car.id).order_by(Auction.amount_of_bids.desc()).limit(5).all()

    for auction in auctions:
        image = Images.query.filter_by(car_id=auction.Car.id).first().image
        auction.Car.image = base64.b64encode(image).decode('ascii')

    return auctions

def get_auctions(page: int, next: str, previous: str):
    total_pages = db.session.query(Auction).filter(
        Auction.status == "active").paginate(page=page, per_page=10).pages

    if total_pages == 0: total_pages = 1

    if next and page < total_pages:
        page += 1
    elif previous and page > 1:
        page -= 1

    auctions = db.session.query(Auction, Car).join(Car, Auction.car_id == Car.id).filter(
        Auction.status == "active").paginate(page=page, per_page=10)

    for auction in auctions:
        auction.Auction.remaining_time = get_remaining_time(
            auction.Auction.end_date, auction.Auction.end_time)
        image = Images.query.filter_by(car_id=auction.Auction.car_id).first()
        auction.Auction.image = base64.b64encode(image.image).decode('ascii')

    return auctions