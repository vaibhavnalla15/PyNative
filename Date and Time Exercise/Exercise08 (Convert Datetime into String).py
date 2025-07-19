""" Convert Datetime into String """
# Write a code to convert a given datetime object into a string.

from datetime import datetime

given_date = datetime(2020, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)