""" Remove all occurrences of a specific item from a list """
# Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]

# Using while loop
while 20 in list1:
    list1.remove(20)
print(list1)

# List comprehension
# remove specific items and return a new list

def remove_values(sample_list, val):
    return [i for i in sample_list if i != val]

result = remove_values(list1, 20)
print(result)


