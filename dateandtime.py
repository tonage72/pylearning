from datetime import datetime, timedelta

today = datetime.now()
first_of_the_year = datetime(2021, 1, 1)
how_many_days = first_of_the_year - today
day_increment = timedelta(days=1, seconds=300)
tomorrow = today + day_increment

print(tomorrow)
print(how_many_days)