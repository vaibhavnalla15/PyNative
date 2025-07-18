""" Invert Dictionary """
# Write a code to swap keys and values in a dictionary. Assume all values are unique
# Hints:-
# 1. Remember that list indices start from 0. So, the third element will be at index 2. Use indexing to get a specific element.
# 2. Use the len() function to get the number of elements.
# 3. An empty list has a length of 0.

original_dict1 = {'a': 1, 'b': 2, 'c': 3}


def invert_dictionary(input_dict):
  inverted_dict = {}
  # iterates through each key-value pair in the input_dict
  for key, value in input_dict.items():
    inverted_dict[value] = key
  return inverted_dict

print("Original Dictionary is:-", original_dict1)
print(f"Inverted Dictionary is:- {invert_dictionary(original_dict1)}")