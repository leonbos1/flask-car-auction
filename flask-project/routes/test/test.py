from flask import Blueprint, render_template, session, request, redirect, url_for

from ...extensions import db

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User

test = Blueprint("test", __name__, static_folder="static", template_folder="templates")

@test.route("/add_data", methods=["GET"])
def add_some_data():
    user1 = User(username="GeertWilders01",
                 email="wilders@pvv.nl", password="drag4wqt5")
    user2 = User(username="MarkRutte01",
                 email="rutte@vvd.nl", password="45t2g234hyg")
    user3 = User(username="leon", email="leon", password="leon")
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    car1 = Car(brand="BMW", model="M3", year=2008,
               condition="Good", mileage=150000, owner_id=1)
    car2 = Car(brand="Audi", model="A4", year=2010,
               condition="Good", mileage=100000, owner_id=2)
    car3 = Car(brand="Mercedes", model="C200", year=2015,
               condition="Good", mileage=50000, owner_id=2)
    car4 = Car(brand="Audi", model="A3", year=2012,
               condition="Good", mileage=80000, owner_id=1)
    car5 = Car(brand="BMW", model="M5", year=2018,
               condition="Good", mileage=20000, owner_id=3)
    car6 = Car(brand="Ferrari", model="LaFerrari", year=2018,
               condition="Good", mileage=3000, owner_id=3)
    car7 = Car(brand="Alfa Romeo", model="Guilia", year=2020,
               condition="Good", mileage=30000, owner_id=3)
    car8 = Car(brand="Suzuki", model="Swift", year=2006,
               condition="Good", mileage=250000, owner_id=3)
    db.session.add(car1)
    db.session.add(car2)
    db.session.add(car3)
    db.session.add(car4)
    db.session.add(car5)
    db.session.add(car6)
    db.session.add(car7)
    db.session.add(car8)
    db.session.commit()

    auction1 = Auction(price=10000, car_id=1, end_date="20-1-2023", end_time="23:59",
                       location="Amsterdam", longitute=4.895168, latitude=52.370216)
    auction2 = Auction(price=20000, car_id=2, end_date="20-1-2023", end_time="23:59",
                       location="Rotterdam", longitute=4.47917, latitude=51.9225)
    auction3 = Auction(price=30000, car_id=3, end_date="20-1-2023", end_time="23:59",
                       location="Utrecht", longitute=5.12142, latitude=52.09083)
    auction4 = Auction(price=40000, car_id=4, end_date="20-1-2023", end_time="23:59",
                       location="Den Haag", longitute=4.3007, latitude=52.0705)
    db.session.add(auction1)
    db.session.add(auction2)
    db.session.add(auction3)
    db.session.add(auction4)
    db.session.commit()

    return redirect(url_for("auctions.get"))