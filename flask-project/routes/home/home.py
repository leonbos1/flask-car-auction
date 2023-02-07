from flask import Blueprint, render_template
import base64

from ...extensions import db
from ...models.auction import Auction
from ...models.car import Car
from ...models.images import Images

from ...queries.auction import get_top_5_auctions

home = Blueprint("home", __name__, static_folder="static", template_folder="templates")

@home.route("/")
def get():
    auctions = get_top_5_auctions()

    return render_template("home.html", auctions=auctions)


