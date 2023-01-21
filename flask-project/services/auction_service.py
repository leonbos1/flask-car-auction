from time import sleep
from threading import Thread

from ..models.auction import Auction
from ..extensions import db
from datetime import datetime

def check_expired_auctions():
    while True:
        print("Checking for expired auctions...")
        auctions = Auction.query.all()
        for auction in auctions:
            if auction.end_date < datetime.now().date():
                auction.expired = True
                db.session.commit()

        sleep(5)