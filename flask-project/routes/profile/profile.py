from flask import Blueprint, render_template, session, request, redirect, url_for

from ..auth.auth import login_required
from ...models.auction import User

profile = Blueprint("profile", __name__, static_folder="static", template_folder="templates")

@profile.route("/")
@login_required
def profile():
    user = User.query.filter_by(id=session["user_id"]).first()
    return render_template("profile.html", user=user)