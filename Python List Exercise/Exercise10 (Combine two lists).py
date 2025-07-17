""" Combine two lists """
# Combine given two lists into a single list and print it.
# Hints:- You can combine lists using the + operator, or by using the extend() method, or by unpacking them into a new list.

list_a = [1, 2]
list_b = [3, 4]

# Method 1: Using unpacking (creates a new list - Python 3.5+)
combined_list_unpacking = [*list_a, *list_b]
print("Combined list (using unpacking *):", combined_list_unpacking)

# Method 2
print(list_a + list_b)

# Method 3
new_list = list_a
new_list.extend(list_b)
print(new_list)


