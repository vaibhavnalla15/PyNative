""" Subtract a Week From a Given Date """
# Write a code to subtract a week (7 days) from a given date.
# Hints:- Use timedelta class

from datetime import timedelta, datetime

given_date = datetime(2020, 2, 25)
print("Given date", given_date)

days_to_subtract = 7
result_date = given_date - timedelta(days_to_subtract)
print("New Date:-", result_date)
