""" Sort Dictionary by Values """
# Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
# Hints:-
# Use sorted() on the dictionary’s items, you’ll need to provide a key argument to sorted() to tell it to sort based on the second element
# of each (key, value) tuple (which is the value). You can use lambda function for this.

from collections import OrderedDict
my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print("Original Dict:-", my_dict)

# Method 1: Create an OrderedDict sorted by values
print("\nSorted by values (as OrderedDict):")
sorted_by_value_ordered_dict = OrderedDict(my_dict)
print(sorted_by_value_ordered_dict)

# Method 2: Convert to a list of (key, value) tuples, sorted by value
print("\nSorted by values (as list of tuples):")
print(my_dict)