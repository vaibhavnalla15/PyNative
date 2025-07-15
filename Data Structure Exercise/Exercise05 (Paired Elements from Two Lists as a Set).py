""" Paired Elements from Two Lists as a Set """
# Write a code to create a Python set such that it shows the element from both lists in a pair.
# Hints:- Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list,second_list)
result_set = set(result)
print(result_set)

# As for now we can convert this result to any (like list, dict, tuple)
# result_list = list(result)
# print(result_set) & so on ....


