""" Replace list’s item with new value if found """
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200.
# Only update the first occurrence of an item.
# Hints:-
# Use list method index(20) to get the index number of a 20
# Next, update the item present at the location using the index number

list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index
index = list1.index(20)

# update item present at location
list1[index] = 200
print(list1)