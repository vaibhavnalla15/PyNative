""" Generate Random Password """
# Write a code to generate a random password which meets the following conditions.
# Password length must be 10 characters long.
# It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string


def generate_password():
    length = 10

    # Required character types
    uppercase_letters = random.choices(string.ascii_uppercase, k=2)
    digits = random.choices(string.digits, k=1)
    special_chars = random.choices("!@#$%^&*()-_+=<>?/|", k=1)

    # Remaining characters (10 - 4 = 6)
    remaining_length = length - (2 + 1 + 1)
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=<>?/|"
    remaining_chars = random.choices(all_chars, k=remaining_length)

    # Combine and shuffle
    password_list = uppercase_letters + digits + special_chars + remaining_chars
    random.shuffle(password_list)

    # Join as string
    password = ''.join(password_list)
    return password


# Generate and print
print("🔐 Your secure password is:", generate_password())



