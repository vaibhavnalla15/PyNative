""" Calculate Multiplication """
# Write a code to calculate multiplication of two random float numbers.
# Note:
# First random float number must be between 0.1 and 1
# Second random float number must be between 9.5 and 99.5

import random

# Generate a random float between 0.1 and 1
first_random_float_num = random.uniform(0.1, 1)
print("First random float number is:", round(first_random_float_num, 2))

# Generate a random float between 9.5 and 99.5
second_random_float_num = random.uniform(9.5, 99.5)
print("Second random float number is:", round(second_random_float_num, 2))

# Multiply the two floats
calculate_multiplication = first_random_float_num * second_random_float_num
print(f"Multiplication of {round(first_random_float_num, 2)} & {round(second_random_float_num, 2)} is {round(calculate_multiplication, 2)}")
