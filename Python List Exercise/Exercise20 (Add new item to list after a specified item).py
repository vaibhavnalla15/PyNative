""" Add new item to list after a specified item """
# Write a program to add item 7000 after 6000 in the following Python List
# Hints:-
# The given list is a nested list. Use indexing to locate the specified item, then use the append() method to add a new item after it.

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000

list1[2][2].append(7000)
print(list1)
