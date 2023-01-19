from flask import Blueprint, render_template

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User

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

def get_remaining_time(end_date, end_time):
    
    #date format = 19-1-2023 
    #time format = 12:00
    end_date = end_date.split("-")
    end_time = end_time.split(":")
    end_date = datetime(int(end_date[2]), int(end_date[1]), int(end_date[0]), int(end_time[0]), int(end_time[1]))
    remaining_time = end_date - datetime.now()

    remaining_time = str(remaining_time).split(".")[0]

    remaining_time = remaining_time.replace(",", "")

    return remaining_time
