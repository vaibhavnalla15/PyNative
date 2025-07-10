""" Use a lambda with the sorted() function to sort a list of tuples based on the second element """
# Hints:-
# The sorted() function can take a key argument, which is a function that will be called on each element of the list prior to making comparisons.
# A lambda function can be used here to specify that the sorting should be based on the element at index 1 of each tuple.

data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
sorted_data = sorted(data, key=lambda item: item[1])
print(f"The sorted list of tuples based on the second element is: {sorted_data}")
