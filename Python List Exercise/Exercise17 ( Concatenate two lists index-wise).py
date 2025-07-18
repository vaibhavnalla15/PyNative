"""  Concatenate two lists index-wise """
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item,
# and so on till the last element. any leftover items will get added at the end of the new list.

# Hints:- Use list comprehension with the zip() function
# Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

