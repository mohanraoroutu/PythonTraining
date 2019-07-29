from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def main():


# DATE OBJECTS
# Get todays date from the simple today()

    today = date.today()
    today = datetime.now()
    t = datetime.time(datetime.now())
    wd = date.weekday(today)
    now = datetime.now()

    print("Date Components:", today.day, today.month, today.year)
    print("Today's Weekday#:", today.weekday())
    print("The current date and time is", today)
    print("The current time is", t)

    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print("Today is day number %d" %wd)
    print("which is a " + days[wd])

    print(now.strftime("%Y"))
    print(now.strftime("%y"))
    print(now.strftime("%a, %d, %B, %y"))
    print(now.strftime("%c"))
    print(now.strftime("%x"))
    print(now.strftime("%X"))
    print(now.strftime("%I:%M%S %p"))
    print(now.strftime("%H:%M"))

    print(timedelta(days=365, hours=8, minutes=15))
    print("today is: " + str(datetime.now()))
    print("one year from now it will be:" + str((datetime.now() + timedelta(days=365))))
    print("in one week and 4days it will be " + str(datetime.now() + timedelta(weeks=1, days=4)))


if __name__ == "__main__":
    main()

today = date.today()
nyd = date(today.year, 1, 1)
if nyd < today:
    print("New Year day is already went by %d days ago" % ((today - nyd).days))
