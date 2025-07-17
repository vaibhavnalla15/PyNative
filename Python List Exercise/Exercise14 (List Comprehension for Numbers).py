""" List Comprehension for Numbers """
# Use list comprehension to create a new list containing only the numbers from a given list.

# Hints:-  List comprehensions provide a concise way to create lists. You need to combine an iteration with a conditional check using isinstance()
# method to filter elements based on their type.

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'John', 6]

numbered_list = [items for items in my_list if isinstance(items, (int, float))]
print(numbered_list)