from time import sleep
import sqlite3

from datetime import datetime

def check_expired_auctions():
    conn = sqlite3.connect('../../instance/auctions.db')
    c = conn.cursor()
    print("Starting auction service...")

    while True:
        print("Checking for expired auctions...")

        c.execute("SELECT * FROM auction WHERE status = 'active'")

        expired_auctions = c.fetchall()

        for auction in expired_auctions:
            is_expired = False
            auction_end_time = auction[4]
            auction_end_date = auction[3]

            #convert to datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M")

    #         current_date = datetime.strptime(current_date, "%Y-%m-%d")
    #         auction_end_date = datetime.strptime(auction_end_date, "%Y-%m-%d")

    #         current_time = datetime.strptime(current_time, "%H:%M")
    #         auction_end_time = datetime.strptime(auction_end_time, "%H:%M")

    #         print(auction_end_date < current_date)

            if auction_end_date < current_date:
                is_expired = True

            elif auction_end_date == current_date:
                if auction_end_time < current_time:
                    is_expired = True
            
            if is_expired:
                print("Closing auction: ", auction)
                
                c.execute("UPDATE auction SET status = 'closed' WHERE id = ?", (auction[0],))

                if auction[9] is not None:
                    c.execute("UPDATE car SET owner_id = ? WHERE id = ?", (auction[9], auction[2]))

            conn.commit()

        sleep(5)

def main():
    check_expired_auctions()

if __name__ == "__main__":
    main()