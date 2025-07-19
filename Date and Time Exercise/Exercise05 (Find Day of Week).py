""" Find Day of Week """
# Write a code to find the day of the week of a given date.
# Hints:-
# 1. Use specific format codes in strftime() method to get name
# 2. Or use calendar module’s day_name() method.

# Solution 1: Using datetime

from datetime import datetime
given_date = datetime(2020, 7, 26)

# to get weekday as integer
print(given_date.today().weekday())

# To get the english name of the weekday
print(given_date.strftime('%A'))
