""" Generate a Python list of all the even & odd numbers between 4 to 30 """
# Hints:-
# Use the built-in range() function to generate a sequence of numbers from the given start number up to (but not including) the stop number,
# with a step of 2, to obtain even & odd numbers.
# Pass the result of the range() function to the list() constructor to create a list

def even_num():
    print(list(range(4, 31, 2)))    # This prints Even numbers within the Range. Just start Range with Even number. Like 2 or 4
    print(list(range(3, 31, 2)))    # This prints Odd numbers within the Range. Just start Range with Odd number. Like 3 or 5
even_num()