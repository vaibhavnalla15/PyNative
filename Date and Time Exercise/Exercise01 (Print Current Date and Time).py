""" Print Current Date and Time """
# Hints:- The datetime module has a class named datetime. This class has a static method now().

# Using datetime module
import datetime

# Print date and time
print("Today's Date & Current Time:-", datetime.datetime.now())

# only time
print("Printing only Current Time:-", datetime.datetime.now().time())

# Solution 2 using time.strftime()
from time import gmtime, strftime
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))