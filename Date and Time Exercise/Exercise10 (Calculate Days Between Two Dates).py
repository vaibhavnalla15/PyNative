""" Calculate Days Between Two Dates """
# Write a code to calculate the days between two dates.
# Hints:- Subtract one datetime object from another, the result is a timedelta object.
# The timedelta object has days attribute that gives you the number of days.

from datetime import datetime,timedelta

# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")
