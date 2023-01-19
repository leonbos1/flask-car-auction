from flask import Blueprint, render_template, session, request, redirect, url_for

from ...extensions import db
from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User

from ..auth.auth import login_required

auction = Blueprint("auction", __name__, static_folder="static", template_folder="templates")

@auction.route("/<int:id>", methods=["GET"])
def get(id):
    auction = Auction.query.filter_by(id=id).first()
    car = Car.query.filter_by(id=auction.car_id).first()
    user = User.query.filter_by(id=car.owner_id).first()
    auction.bidder_name = User.query.filter_by(id=auction.bidder).first()
    auction.car = car
    auction.car.owner = user

    return render_template("auction.html", auction=auction)


@auction.route("/<int:id>/bid", methods=["GET"])
def bid(id):
    new_price = request.args.get("amount")

    auction = Auction.query.filter_by(id=id).first()
    car = Car.query.filter_by(id=auction.car_id).first()
    user = User.query.filter_by(id=car.owner_id).first()
    auction.car = car
    auction.car.owner = user
    auction.price = new_price

    if session.get("user_id"):
        user_id = session["user_id"]
        user = User.query.filter_by(id=user_id).first()
        auction.bidder = user.id
        db.session.commit()
        return redirect(url_for("auction.get", id=id))
    else:
        return redirect(url_for("auth.login"))


@login_required
@auction.route("/sell", methods=["GET"])
def sell():
    user = User.query.filter_by(id=session["user_id"]).first()
    cars = Car.query.filter_by(owner_id=user.id).all()

    cars = [car for car in cars if not Auction.query.filter_by(
        car_id=car.id).first()]

    return render_template("sell.html", cars=cars)

@login_required
@auction.route("/sell", methods=["POST"])
def sell_car():
    car_id = request.form.get("car")
    price = request.form.get("price")
    end_date = request.form.get("end_date")
    location = request.form.get("location")
    longitute = request.form.get("longitute")
    latitude = request.form.get("latitude")

    auction = Auction(price=price, car_id=car_id, end_date=end_date,
                      location=location, longitute=longitute, latitude=latitude)
    db.session.add(auction)
    db.session.commit()

    return redirect(url_for("auctions.get"))