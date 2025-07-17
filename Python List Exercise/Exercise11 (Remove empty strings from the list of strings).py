""" Remove empty strings from the list of strings """
# Hints:- Use a filter() function to remove the None / empty type from the list

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# remove None from list1 and convert result into list
result = list(filter(None, list1))
print(result)

