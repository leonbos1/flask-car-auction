from flask import Blueprint, render_template, session, request, redirect, url_for

from ...extensions import db

from ...models.auction import Auction
from ...models.car import Car
from ...models.user import User
from ...models.images import Images

test = Blueprint("test", __name__, static_folder="static",
                 template_folder="templates")


@test.route("/add_data", methods=["GET"])
def add_some_data():
    add_users()
    add_cars()

    directory = "./flask-project/images/"

    image1 = Images(car_id=1, image=open(directory + "m3.1.png", "rb").read())
    image2 = Images(car_id=1, image=open(directory + "m3.2.png", "rb").read())
    image3 = Images(car_id=1, image=open(directory + "m3.3.png", "rb").read())
    image4 = Images(car_id=1, image=open(directory + "m3.4.png", "rb").read())
    image5 = Images(car_id=1, image=open(directory + "m3.5.png", "rb").read())
    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.add(image4)
    db.session.add(image5)
    db.session.commit()

    image6 = Images(car_id=2, image=open(directory + "a4.1.png", "rb").read())
    image7 = Images(car_id=2, image=open(directory + "a4.2.png", "rb").read())
    image8 = Images(car_id=2, image=open(directory + "a4.3.png", "rb").read())
    image9 = Images(car_id=2, image=open(directory + "a4.4.png", "rb").read())
    image10 = Images(car_id=2, image=open(directory + "a4.5.png", "rb").read())
    db.session.add(image6)
    db.session.add(image7)
    db.session.add(image8)
    db.session.add(image9)
    db.session.add(image10)
    db.session.commit()

    image11 = Images(car_id=6, image=open(
        directory + "laferrari.1.png", "rb").read())
    image12 = Images(car_id=6, image=open(
        directory + "laferrari.2.png", "rb").read())
    image13 = Images(car_id=6, image=open(
        directory + "laferrari.3.png", "rb").read())
    image14 = Images(car_id=6, image=open(
        directory + "laferrari.4.png", "rb").read())
    image15 = Images(car_id=6, image=open(
        directory + "laferrari.5.png", "rb").read())
    db.session.add(image11)
    db.session.add(image12)
    db.session.add(image13)
    db.session.add(image14)
    db.session.add(image15)
    db.session.commit()

    image16 = Images(car_id=4, image=open(directory + "a3.1.png", "rb").read())
    image17 = Images(car_id=4, image=open(directory + "a3.2.png", "rb").read())
    image18 = Images(car_id=4, image=open(directory + "a3.3.png", "rb").read())
    image19 = Images(car_id=4, image=open(directory + "a3.4.png", "rb").read())
    image20 = Images(car_id=4, image=open(directory + "a3.5.png", "rb").read())
    image21 = Images(car_id=4, image=open(directory + "a3.6.png", "rb").read())
    image22 = Images(car_id=4, image=open(directory + "a3.7.png", "rb").read())
    image23 = Images(car_id=4, image=open(directory + "a3.8.png", "rb").read())
    db.session.add(image16)
    db.session.add(image17)
    db.session.add(image18)
    db.session.add(image19)
    db.session.add(image20)
    db.session.add(image21)
    db.session.add(image22)
    db.session.add(image23)
    db.session.commit()

    image24 = Images(car_id=3, image=open(
        directory + "c200.1.png", "rb").read())
    image25 = Images(car_id=3, image=open(
        directory + "c200.2.png", "rb").read())
    image26 = Images(car_id=3, image=open(
        directory + "c200.3.png", "rb").read())
    image27 = Images(car_id=3, image=open(
        directory + "c200.4.png", "rb").read())
    image28 = Images(car_id=3, image=open(
        directory + "c200.5.png", "rb").read())
    image29 = Images(car_id=3, image=open(
        directory + "c200.6.png", "rb").read())
    image30 = Images(car_id=3, image=open(
        directory + "c200.7.png", "rb").read())
    image31 = Images(car_id=3, image=open(
        directory + "c200.8.png", "rb").read())
    db.session.add(image24)
    db.session.add(image25)
    db.session.add(image26)
    db.session.add(image27)
    db.session.add(image28)
    db.session.add(image29)
    db.session.add(image30)
    db.session.add(image31)
    db.session.commit()

    image32 = Images(car_id=5, image=open(directory + "m5.1.png", "rb").read())
    image33 = Images(car_id=5, image=open(directory + "m5.2.png", "rb").read())
    image34 = Images(car_id=5, image=open(directory + "m5.3.png", "rb").read())
    image35 = Images(car_id=5, image=open(directory + "m5.4.png", "rb").read())
    image36 = Images(car_id=5, image=open(directory + "m5.5.png", "rb").read())
    image37 = Images(car_id=5, image=open(directory + "m5.6.png", "rb").read())
    image38 = Images(car_id=5, image=open(directory + "m5.7.png", "rb").read())
    image39 = Images(car_id=5, image=open(directory + "m5.8.png", "rb").read())
    db.session.add(image32)
    db.session.add(image33)
    db.session.add(image34)
    db.session.add(image35)
    db.session.add(image36)
    db.session.add(image37)
    db.session.add(image38)
    db.session.add(image39)
    db.session.commit()

    return redirect(url_for("auctions.get"))


def add_users():
    user1 = User(username="geert",
                 email="geert", password="geert", wallet=100000)
    user2 = User(username="test",
                 email="test", password="test", wallet=10000000)
    user3 = User(username="leon", email="leon",
                 password="leon", wallet=1000000)
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()


def add_cars():
    car1 = Car(brand="BMW", model="M3", year=2017,
               condition="Good", mileage=150000, owner_id=1)
    car2 = Car(brand="Audi", model="A4", year=2010,
               condition="Good", mileage=100000, owner_id=2)
    car3 = Car(brand="Mercedes", model="C200", year=2015,
               condition="Good", mileage=50000, owner_id=2)
    car4 = Car(brand="Audi", model="A3", year=2012,
               condition="Good", mileage=80000, owner_id=1)
    car5 = Car(brand="BMW", model="M5 Competition", year=2018,
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
