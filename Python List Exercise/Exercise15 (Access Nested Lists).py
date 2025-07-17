""" Access Nested Lists """
# Given a nested list, print the element '55'.
# Hints:-
# To access elements in a nested list, you need to use multiple sets of square brackets, one for each level of nesting, specifying the index at each level.

nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print("Nested List:-", nested_list)

# To access 55:
# 1. The list [44, 55, 66] is at index 1 of the main nested_list.
# 2. Within [44, 55, 66], the element 55 is at index 1.
element_55 = nested_list[1][1]
print(f"The element '55' is: {element_55}")

