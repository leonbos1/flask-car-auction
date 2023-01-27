from ..extensions import db

class Car(db.Model):
    __tablename__ = "car"
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(80), unique=True, nullable=False)
    brand = db.Column(db.String(80), unique=False, nullable=False)
    model = db.Column(db.String(120), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=True)
    condition = db.Column(db.String(120), unique=False, nullable=True)
    vehicle_type = db.Column(db.String(120), unique=False, nullable=True)
    mileage = db.Column(db.Integer, unique=False, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)