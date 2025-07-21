""" Generate Random String """
# Write a code to generate random string of length 5.
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.

import random
import string

def get_random_string(length):
    result = "".join(random.choice(string.ascii_letters) for i in range(length))
    print(result)

# string of length 5
get_random_string(5)
get_random_string(5)