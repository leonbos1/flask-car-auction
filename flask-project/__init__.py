from flask import Flask
from .routes.auctions.auctions import auctions
from .routes.auction.auction import auction
from .routes.auth.auth import auth
from .routes.test.test import test
from .routes.home.home import home

from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auctions.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'EFG#$ty45wg'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(auctions, url_prefix="/auctions")
    app.register_blueprint(auction, url_prefix="/auction")
    app.register_blueprint(auth, url_prefix="")
    app.register_blueprint(test, url_prefix="/test")
    app.register_blueprint(home, url_prefix="")

    return app