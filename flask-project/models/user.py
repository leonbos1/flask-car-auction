from ..extensions import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    wallet = db.Column(db.Integer)

    def check_password(self, password):
        if self.password == password:
            return True

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True