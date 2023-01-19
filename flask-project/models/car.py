from ..extensions import db

class Car(db.Model):
    __tablename__ = "car"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), unique=False, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    condition = db.Column(db.String(120), unique=False, nullable=False)
    mileage = db.Column(db.Integer, unique=False, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)