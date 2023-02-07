from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify

from ...queries.auction import get_auctions 

from datetime import datetime
import base64

auctions = Blueprint("auctions", __name__,
                     static_folder="static", template_folder="templates")


@auctions.route("/", methods=["GET"])
def get():
    page = request.args.get("page", 1, type=int)

    next = request.args.get("next", None, type=str)
    previous = request.args.get("previous", None, type=str)

    auctions = get_auctions(page, next, previous)

    return render_template("auctions.html", auctions=auctions, page=page, total_pages=auctions.pages)
