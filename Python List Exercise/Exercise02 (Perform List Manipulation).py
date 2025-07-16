""" Perform List Manipulation """
# Perform following list manipulation operations on given list:-
# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.

# Hints:-
# 1. You can modify an element by assigning a new value to its index.
# 2. Use the append() method to add an item to the end.
# 3. Use the insert() method to add an item at a specific position.
# 4. Use the remove() method to delete an item by its value.
# 5. Use the pop() method or del statement to delete an item by its index.

my_list = [10, 20, 30, 40, 50]
print("Initial List:-", my_list)

# Change the second element (at index 1) to 200
my_list[1] = 200
print("After changing second element:", my_list)

# Add 600 to the end of the list
my_list.append(600)
print("List after appending 600:", my_list)

# Insert 300 at index 2
my_list.insert(2,300)
print("List after inserting 300 at index 2:", my_list)

# Remove 600 from the list (by value)
my_list.remove(600)
print("List after removing 600 (by value):", my_list)

# Remove the element at index 0 (using del)
del my_list[0]
print("List after removing element at index 0:", my_list)