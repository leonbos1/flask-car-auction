from ..extensions import db

class Auction(db.Model):
    __tablename__ = "auction"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, unique=True, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    end_date = db.Column(db.String, unique=False, nullable=False)
    location = db.Column(db.String, unique=False, nullable=False)
    longitute = db.Column(db.Float, unique=False, nullable=False)
    latitude = db.Column(db.Float, unique=False, nullable=False)
    bidder = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)