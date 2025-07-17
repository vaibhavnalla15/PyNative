""" Dictionary from Lists """
# Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements
# from the second list become values.

# Hints:-
# 1. Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.
# 2. Or, Iterate the list using a for loop and range() function. In each iteration, add a new key-value pair to a dict using the update() method

# Solution 1: The zip() function and a dict() constructor
# Use the zip(keys, values) to aggregate two lists.
# Wrap the result of a zip() function into a dict() constructor.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict(zip(keys, values))
print(result_dict)

# Solution 2: Using a loop and update() method of a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = dict()
for i in range(len(keys)):
    result_dict.update({keys[i]:values[i]})
print(result_dict)