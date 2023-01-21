from flask import Blueprint, render_template, session, request, redirect, url_for

from ...extensions import db

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User

test = Blueprint("test", __name__, static_folder="static", template_folder="templates")

@test.route("/add_data", methods=["GET"])
def add_some_data():
    user1 = User(username="geert",
                 email="geert", password="geert")
    user2 = User(username="test",
                 email="test", password="test")
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

    return redirect(url_for("auctions.get"))