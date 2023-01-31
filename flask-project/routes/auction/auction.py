from flask import Blueprint, render_template, session, request, redirect, url_for

from ...extensions import db
from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User
from ...models.images import Images
from ...utils.time import get_remaining_time, date_is_future, get_future_date
from ...utils.location import get_latitude_longitude

from ..auth.auth import login_required, get_user

import base64

auction = Blueprint("auction", __name__, static_folder="static", template_folder="templates")

@auction.route("/<int:id>", methods=["GET"])
def get(id):
    auction = Auction.query.filter_by(id=id).first()
    car = Car.query.filter_by(id=auction.car_id).first()
    user = get_user()
    auction.bidder_name = User.query.filter_by(id=auction.bidder).first()
    auction.car = car
    auction.car.owner = user

    auction.remaining_time = get_remaining_time(auction.end_date, auction.end_time)

    if session.get("user_id"):
        user_id = session["user_id"]
        user = User.query.filter_by(id=user_id).first()

    images = Images.query.filter_by(car_id=car.id).all()
    for image in images:
        image.data = base64.b64encode(image.image).decode('ascii')

    return render_template("auction.html", auction=auction, current_user=user, images=images)

@login_required
@auction.route("/<int:id>/bid", methods=["GET"])
def bid(id):
    new_price = int(request.args.get("amount"))

    auction = Auction.query.filter_by(id=id).first()
    car = Car.query.filter_by(id=auction.car_id).first()
    current_user = get_user() 

    if new_price > current_user.wallet or new_price <= auction.price:
        return redirect(url_for("auction.get", id=id))

    auction.car = car
    auction.car.owner = current_user
    
    if auction.bidder:
        previous_bidder = User.query.filter_by(id=auction.bidder).first()
        previous_bidder.wallet += auction.price
        
    
    current_user.wallet -= new_price
    auction.price = new_price
    auction.bidder = current_user.id

    auction.amount_of_bids += 1
        
    db.session.commit()

    return redirect(url_for("auction.get", id=id))


@login_required
@auction.route("/sell", methods=["GET"])
def sell():
    user = get_user()

    if not user:
        return redirect(url_for("auth.login"))

    cars = Car.query.filter_by(owner_id=user.id).all()

    cars = [car for car in cars if not Auction.query.filter_by(
        car_id=car.id).filter_by(status="active").first()]

    return render_template("sell.html", cars=cars)

@login_required
@auction.route("/sell", methods=["POST"])
def sell_car():
    car_id = request.form.get("car")
    price = request.form.get("price")
    end_date = request.form.get("end_date")
    end_time = request.form.get("end_time")
    location = request.form.get("location")
    images = request.files.getlist("images")

    for image in images:
        img = Images(car_id=car_id, image=image.read())
        db.session.add(img)
        db.session.commit()

    if not date_is_future(end_date):
        end_date = get_future_date()
    
    latitude, longitute = get_latitude_longitude(location)

    already_auctioned = Auction.query.filter_by(car_id=car_id).first()

    if already_auctioned:
        if (already_auctioned.status == "active"):
            return redirect(url_for("auctions.get"))
        else:
            already_auctioned.status = "active"
            already_auctioned.price = price
            already_auctioned.end_date = end_date
            already_auctioned.end_time = end_time
            already_auctioned.location = location
            already_auctioned.latitude = latitude
            already_auctioned.longitute = longitute
            db.session.commit()
            return redirect(url_for("auctions.get"))

    auction = Auction(price=price, car_id=car_id, end_date=end_date, end_time=end_time,
                      location=location, longitute=longitute, latitude=latitude, status="active", amount_of_bids=0)
    db.session.add(auction)
    db.session.commit()

    return redirect(url_for("auctions.get"))