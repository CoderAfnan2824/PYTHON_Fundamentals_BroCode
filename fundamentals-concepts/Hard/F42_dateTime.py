import datetime

date = datetime.date(2025, 12, 24)    # Store time in ccyy-mm-dd format

today = datetime.date.today()         # Current date
now = datetime.datetime.now()         # Current Time

print(f"Today's Date: {today}")
print(f"Today's time: {now}")

print(date)
now = now.strftime("%H %M %S %m-%d-%Y")  
# see strftime method for more details (H: hour, M: Mins, S: secs, m: month, d: day, Y: year)
print(now)

target_date = datetime.datetime(2020, 12, 1, 12, 30, 00)
current_date = datetime.datetime.now()

if(current_date > target_date):
    print("Date has passed")
else:
    print("Date did not pass")