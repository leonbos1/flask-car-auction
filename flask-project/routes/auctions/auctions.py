from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User
from ...models.images import Images
from ...utils.time import get_remaining_time

from ...extensions import db

from datetime import datetime
import base64

auctions = Blueprint("auctions", __name__,
                     static_folder="static", template_folder="templates")


@auctions.route("/", methods=["GET"])
def get():
    page = request.args.get("page", 1, type=int)

    next = request.args.get("next", None, type=str)
    previous = request.args.get("previous", None, type=str)

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

    return render_template("auctions.html", auctions=auctions, page=page, total_pages=auctions.pages)
