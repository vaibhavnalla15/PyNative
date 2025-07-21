""" Generate Random Date """
# Write a code to generate a random date between given start and end dates.

from datetime import datetime, timedelta
import random


# Function to get a random date between two given dates
def get_random_date(startDate, endDate):
    print("Printing random date between:-", startDate, "and", endDate)
    date_format = '%d/%m/%Y'  # Define the expected date format (day/month/year)

    # Convert start and end date strings to datetime objects
    start = datetime.strptime(startDate, date_format)
    end = datetime.strptime(endDate, date_format)

    # Calculate the difference in days between the start and end dates
    delta = end - start

    # Generate a random number of days to add (between 0 and total days in range)
    random_days = random.randint(0, delta.days)

    # Add the random number of days to the start date
    random_date = start + timedelta(days=random_days)

    # Convert the final datetime object back to a string in the original format
    return random_date.strftime(date_format)


# Call the function and print a random date between 01/01/2001 and 12/12/2012
print("Random Date:-", get_random_date("01/01/2001", "12/12/2012"))

