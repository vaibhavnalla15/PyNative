""" Check if a value exists in a dictionary """
# While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.
# Write a Python program to check if the value 200 is present in the provided dictionary.

# Hints:-
# Get all values of a dict in a list using the values() method.
# Next, use the if condition to check if 200 is present in the given list

sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print("200 Present in Given Dict")