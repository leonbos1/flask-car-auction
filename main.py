from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auctions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'EFG#$ty45wg'
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
    brand = db.Column(db.String(80), unique=False, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    condition = db.Column(db.String(120), unique=False, nullable=False)
    mileage = db.Column(db.Integer, unique=False, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Auction(db.Model):
    __tablename__ = "auction"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=True, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    end_date = db.Column(db.String, unique=False, nullable=False)
    location = db.Column(db.String, unique=False, nullable=False)
    longitute = db.Column(db.Float, unique=False, nullable=False)
    latitude = db.Column(db.Float, unique=False, nullable=False)

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

@app.route("/add_data", methods=["GET"])
def add_some_data():
    user1 = User(username="GeertWilders01", email="wilders@pvv.nl", password="drag4wqt5")
    user2 = User(username="MarkRutte01", email="rutte@vvd.nl", password="45t2g234hyg")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    car1 = Car(brand="BMW", model="M3", year=2008, condition="Good", mileage=150000, owner_id=1)
    car2 = Car(brand="Audi", model="A4", year=2010, condition="Good", mileage=100000, owner_id=2)
    car3 = Car(brand="Mercedes", model="C200", year=2015, condition="Good", mileage=50000, owner_id=2)
    car4 = Car(brand="Audi", model="A3", year=2012, condition="Good", mileage=80000, owner_id=1)
    db.session.add(car1)
    db.session.add(car2)
    db.session.add(car3)
    db.session.add(car4)
    db.session.commit()

    auction1 = Auction(price=10000, car_id=1, end_date="2020-12-31", location="Amsterdam", longitute=4.895168, latitude=52.370216)
    auction2 = Auction(price=20000, car_id=2, end_date="2020-12-31", location="Rotterdam", longitute=4.47917, latitude=51.9225)
    auction3 = Auction(price=30000, car_id=3, end_date="2020-12-31", location="Utrecht", longitute=5.12142, latitude=52.09083)
    auction4 = Auction(price=40000, car_id=4, end_date="2020-12-31", location="Den Haag", longitute=4.3007, latitude=52.0705)
    db.session.add(auction1)
    db.session.add(auction2)
    db.session.add(auction3)
    db.session.add(auction4)
    db.session.commit()

    return redirect(url_for("auctions"))


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not password == user.password:
        flash("Please check your login details and try again.")
        return redirect(url_for("login"))

    login_user(user)

    return redirect(url_for("auctions"))

@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_post():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if user:
        flash("Username already exists")
        return redirect(url_for("register"))

    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auctions"))

def login_user(user):
    session.clear()
    session["user_id"] = user.id

def logout_user():
    session.clear()

def is_logged_in():
    return session.get("user_id") is not None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/profile")
@login_required
def profile():
    user = User.query.filter_by(id=session["user_id"]).first()
    return render_template("profile.html", user=user)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)