""" Calculate the date 4 months from the current date """
# Hints:-
# For exact month arithmetic, the dateutil library (specifically dateutil.relativedelta) is the standard Python solution,
# as timedelta only works with fixed durations (days, seconds, etc.).
# We need to use the Python dateutil module’s relativedelta. We can add 4 months into the given date using a relativedelta.
# The relativedelta is useful when we want to deal months with day 29, 30 31, It will properly adjust the days.

from datetime import datetime
from dateutil.relativedelta import relativedelta

# 2020-02-25
given_date = datetime(2020, 2, 25).date()

months_to_add = 4
new_date = given_date + relativedelta(months=+ months_to_add)
print(new_date)

