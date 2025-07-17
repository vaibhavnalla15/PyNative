""" Iterate both lists simultaneously """
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order
# and items from list2 in reverse order.
# Hints:-
# Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# In straight order:-
for x, y in zip(list1, list2):
    print(x, y)

print()

# In reverse order:-
for x, y in zip(list1, list2[::-1]):
    print(x, y)


