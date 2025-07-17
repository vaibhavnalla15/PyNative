""" Flatten Nested List """
# Write a function to flatten a list of lists into a single, non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).

# Hints:- Iterate through the outer list, and for each sublist, iterate through its elements and append them to a new flattened list.
# You can also use list comprehension to make code concise.

# Without list comprehension
def flatten_list(nested_list):
    flattened = []
    for sublist in nested_list:
        for item in sublist:
            flattened.append(item)
    return flattened

# Alternative and often more Pythonic using List comprehension
def flatten_list_comprehension(nested_list):
  return [item for sublist in nested_list for item in sublist]

# Test cases
list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
print(f"Original nested list: {list_of_lists}")

flattened_result = flatten_list(list_of_lists)
print(f"Flattened list (using loops): {flattened_result}")

flattened_result_comp = flatten_list_comprehension(list_of_lists)
print(f"Flattened list (using list comprehension): {flattened_result_comp}")