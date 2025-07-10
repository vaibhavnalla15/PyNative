""" Use a lambda with the map() function to double each element in a list """
# Hints:-
# The map() function applies a given function to each item of an iterable (like a list) and returns an iterator of the results.
# You can use a lambda function to define the operation to be performed on each element concisely.

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f"The doubled numbers are: {doubled_numbers}")
