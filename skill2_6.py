from datetime import datetime,timedelta

current_datetime = datetime.now()

one_year_future = current_datetime+timedelta(days=365)

print(one_year_future)

pastdate = current_datetime-timedelta(days=3)
print(pastdate)

dt = current_datetime.date()
print(dt)

tomorrow = dt + timedelta(days=1)
print(tomorrow)