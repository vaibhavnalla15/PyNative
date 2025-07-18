""" Sort Dictionary by Keys """
# Sort a dictionary by its keys and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
# Hints:-  You can get the keys, sort them, and then build a new dictionary or list of tuples.

from collections import OrderedDict

my_dict = {'apple': 3, 'zebra': 1, 'banana': 2, 'cat': 4}
print(f"Original Dict:- {my_dict}")

# Method 1: Create an OrderedDict (maintains insertion order, good for sorted views)
# In Python 3.7+, dicts already preserve insertion order, so this might be redundant
# if you just create a new dict from sorted items.
print("\nSorted by keys (as OrderedDict):")

sorted_by_key_order_dict = OrderedDict(sorted(my_dict.items()))
print(sorted_by_key_order_dict)

# Method 2: Convert to a list of (key, value) tuples, sorted by key
print("\nSorted by keys (as list of tuples):")
sorted_list_of_tuples = sorted(my_dict.items())
print(sorted_list_of_tuples)
