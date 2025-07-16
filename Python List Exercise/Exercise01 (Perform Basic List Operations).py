""" Perform Basic List Operations """
# Perform following operations on given list:-
# Access Elements: Print the third element.
# List Length: Print the number of elements in the list
# Check if Empty: Write a code to check is list empty.

# Hints:-
# 1. Remember that list indices start from 0. So, the third element will be at index 2. Use indexing to get a specific element.
# 2. Use the len() function to get the number of elements.
# 3. An empty list has a length of 0.

my_list = [10, 20, 30, 40, 50]
print("Initial List:-", my_list)

third_item = my_list[2]
print("Third item:-", third_item)

length_of_list = len(my_list)
print("Length of the List:-", length_of_list)

# list empty
if length_of_list == 0:
    print("List is Empty")
else:
    print("List is not Empty")


