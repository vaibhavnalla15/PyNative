""" Flatten a nested list using loops """
# You need to use nested loop ( a loop inside another loop)
# 1. Write Outer Loop:
    # Iterates over each element in the input nested_list.
# 2. Write Inner Loop:
    # 1. Check If the element is a list, iterate through the sublist and append each item to flat_list.
    # 2. Otherwise, append the element directly to flat_list.
# 3. After processing all elements, return the flattened list.

# Flatten means making nested list as a single list
# Ex . nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]] to flatten_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def flatten_list(nested_list):
    flat_list = []  # Initialize an empty list to store the flattened elements

    # Iterate through each element in the list
    for element in nested_list:
        if isinstance(element, list): # Check if the element is a list
            for item in element: # If so, iterate through the inner list
                flat_list.append(item)
        else:
            flat_list.append(element) # If not a list, add the element directly

    return flat_list

# Example usage
nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)


