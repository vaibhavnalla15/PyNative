""" Return multiple values from a function """
# Write a function calculation() that accepts two variables and calculates both their addition and subtraction.
# The function should then return both the sum and the difference in a single return statement.

# Hints:- In Python, to return multiple values from a function, separate the values with commas in the return statement

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

print(calculation(10,5))

