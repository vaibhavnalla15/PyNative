""" Remove Duplicates from list """
# Write a function that takes a list with duplicate elements and returns a new list with only unique elements.
# Hints:- Sets in Python inherently store only unique elements.
# You can convert a list to a set to get unique elements, and then convert it back to a list.

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

new_list = set(list_with_duplicates) # Here "Set" data type is used because "Set" is an unordered collection of unique, immutable elements.
print(list(new_list))