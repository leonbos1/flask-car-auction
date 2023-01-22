from datetime import datetime, timedelta

def get_remaining_time(end_date: str, end_time: str):
    
    end_date = end_date.split("-")
    end_time = end_time.split(":")

    end_date = datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]), int(end_time[0]), int(end_time[1]))
    print(end_date)
    remaining_time = end_date - datetime.now()

    remaining_time = str(remaining_time).split(".")[0]

    #make hours, minutes, seconds 2 digits
    remaining_time = remaining_time.split(":")
    for i in range(len(remaining_time)):
        if "day, 0" in remaining_time[i]:
            remaining_time[i] = remaining_time[i].replace("day, 0", "day, 00")
    
    remaining_time = ":".join(remaining_time)

    if remaining_time == "00:00:00":
        remaining_time = "Auction has ended"

    return remaining_time

def date_is_future(date: str):
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