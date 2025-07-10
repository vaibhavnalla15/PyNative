""" Create a lambda function that squares a given number """
# A lambda function in Python is a small anonymous function defined using the lambda keyword.
# The syntax is lambda arguments: expression.  The expression is evaluated and returned.

square = lambda x: x ** 2

number = 5
squared_number = square(number)
print(f"The square of {number} is {squared_number}")
