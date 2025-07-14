""" Remove empty strings from a list of strings """
# Hints:-
# Use the built-in function filter() to remove empty strings from a list
# Or use the for loop and if condition to remove the empty strings from a list

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Solution 1: Using the loop and if condition
result_list = []
for s in str_list:
    # check for non empty string
    if s:
        result_list.append(s)
print(result_list)

# Solution 2: Using the built-in function filter()
new_list = list(filter(None, str_list))
print(new_list)