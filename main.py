from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auctions.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

class Car(db.Model):
    __tablename__ = "car"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Auction(db.Model):
    __tablename__ = "auction"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=True, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/auctions", methods=["GET"])
def auctions():
    auctions = Auction.query.all()

    for auction in auctions:
        car = Car.query.filter_by(id=auction.car_id).first()
        user = User.query.filter_by(id=car.owner_id).first()
        auction.car = car
        auction.car.owner = user

    return render_template("auctions.html", auctions=auctions)

@app.route("/auction/<int:id>", methods=["GET"])
def auction(id):
    auction = Auction.query.filter_by(id=id).first()
    car = Car.query.filter_by(id=auction.car_id).first()
    user = User.query.filter_by(id=car.owner_id).first()
    auction.car = car
    auction.car.owner = user

    return render_template("auction.html", auction=auction)
    
def add_some_data():
    user1 = User(username="GeertWilders01", email="wilders@pvv.nl", password="drag4wqt5")
    user2 = User(username="MarkRutte01", email="rutte@vvd.nl", password="45t2g234hyg")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    car1 = Car(brand="BMW", model="M3", year=2019, owner_id=user1.id)
    car2 = Car(brand="Audi", model="A4", year=2018, owner_id=user2.id)
    db.session.add(car1)
    db.session.add(car2)
    db.session.commit()

    auction1 = Auction(price=10000, car_id=car1.id)
    auction2 = Auction(price=20000, car_id=car2.id)
    db.session.add(auction1)
    db.session.add(auction2)
    
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)