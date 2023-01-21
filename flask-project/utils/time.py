from datetime import datetime, timedelta

def get_remaining_time(end_date, end_time):
    
    #date format = 2023-01-28 
    #time format = 12:00
    end_date = end_date.split("-")
    end_time = end_time.split(":")
    end_date = datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]), int(end_time[0]), int(end_time[1]))
    remaining_time = end_date - datetime.now()

    remaining_time = str(remaining_time).split(".")[0]

    if remaining_time == "0:00:00":
        remaining_time = "Auction has ended"

    return remaining_time

def date_is_future(date):
    """checks if the date is in the future
    """
    date = date.split("-")
    date = datetime(int(date[0]), int(date[1]), int(date[2]))
    if date <= datetime.now():
        return False
    return True

def get_future_date():
    """returns a date that is 1 day after today
    """
    date = datetime.now()
    date = date + timedelta(days=1)
    date = str(date).split(" ")[0]
  
    return date