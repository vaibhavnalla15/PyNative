""" Check if All Values are Unique """
# Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.
# Hints:-
# sets are excellent for checking uniqueness. You can extract all the values from the dictionary and then see if the number of values is the
# same as the number of unique values (i.e., the size of a set created from those values).

def are_all_values_unique(input_dict):
    # Get all values from the dictionary
    all_values = list(input_dict.values())

    # Convert the list of values to a set to get only unique values
    unique_values_set = set(all_values)

    # If the length of the original values list is equal to the length of the unique values set,
    # it means all values were unique.
    return len(all_values) == len(unique_values_set)

# Test cases
dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
dict3 = {} # Empty dictionary (all values are vacuously unique)

print(f"Dictionary: {dict1} -> All values unique? {are_all_values_unique(dict1)}")
print(f"Dictionary: {dict2} -> All values unique? {are_all_values_unique(dict2)}")
print(f"Dictionary: {dict3} -> All values unique? {are_all_values_unique(dict3)}")
