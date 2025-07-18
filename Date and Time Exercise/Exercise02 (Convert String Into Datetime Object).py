""" Convert String Into Datetime Object """
# Write a code to convert the given date in string format into a Python DateTime object.
# Hints:-
# 1. The datetime class has a method strptime() specifically designed to parse strings into datetime objects.
# 2. You’ll need to tell this method the exact format of your input string using format codes
#    (e.g., %Y for year, %m for month, %d for day, %H for hour, %M for minute, %S for second).

from datetime import datetime

date_string = "Feb 25 2020 4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)
