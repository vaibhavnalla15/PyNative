""" Create a copy of a list """
# Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
# Hints:-
# Simple assignment (new_list = original_list) does not create a true copy; it just creates another reference to the same list.
# For a “shallow copy, you need to use method such as slicing, list() constructor, or the copy() method.

original_list = [10, 20, 30]
print("Original list initially:", original_list)

# Create a copy using slicing
# This is a common and concise way to create a shallow copy
copied_list = original_list[:]

# Modify the copied list
copied_list.append(40)
copied_list.insert(0,0)
print("First copied list:-",copied_list)

# Demonstration using list() constructor
another_copy = list(original_list)
another_copy.append(50)
print("\nOriginal list after another_copy modification:", original_list)
print("Another copied list:-", another_copy)

# Demonstration using .copy() method (Python 3+)
third_copy = original_list.copy()
third_copy.append(60)
print("\nOriginal list after third_copy modification:", original_list)
print("Third copied list:-", third_copy)