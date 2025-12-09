from datetime import datetime
import pytz

def get_time():
    now = datetime.now(pytz.timezone("Asia/Kolkata"))
    return now.strftime("It's %I:%M %p")

def get_date():
    today = datetime.now()
    return today.strftime("Today's date is %B %d, %Y")

#if __name__ == "__main__":
   # print(get_time())
  #  print(get_date())