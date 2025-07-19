""" Add Week to Given Date """
# Write a code to add a week (7 days) and 12 hours to a given date.
# Hints:-
# 1. Use the timedelta class.
# 2. Create a timedelta object that combines days and hours.
# 3. Use the + operator to add this timedelta to your datetime object.

from datetime import timedelta, datetime
# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)
print("Given Date:-", given_date)

days_to_add = 7
result = given_date + timedelta(days=days_to_add, hours=12)
print("New Date:-", result)
