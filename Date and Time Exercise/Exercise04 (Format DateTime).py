""" Format DateTime """
# Write a code to print date in the following format.
# Day_name  Day_number  Month_name  Year
# Hints:- Use specific format codes in strftime() method to achieve the desired output
# (e.g., %A for full weekday name, %d for day of the month, %B for full month name, %Y for year).

from datetime import datetime

given_date = datetime(2020, 2, 25)
new_date = given_date.strftime("%A %d %B %Y")
print(new_date)
