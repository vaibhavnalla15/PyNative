""" Merge two Python dictionaries into one """
# Write a code to merge two dictionaries into a new dictionary and print it.

# Hints:-
# There are three ways:-
# Using the update() method.
# Using the dictionary unpacking operator (** for Python 3.5+)
# Simple concatenation with | (Python 3.9+).

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

# Using the Union Operator
new_dict = dict1 | dict2
print(new_dict)

# Using the update() Method
dict1.update(dict2)
print(dict1)

# Using the Unpacking Operator (**)
merged_dict = {**dict1, **dict2}
print(merged_dict)