""" Use a lambda with the filter() function to get all even numbers from a list """
# Hints:-
# The filter() function takes two arguments: a function and an iterable. It applies the function to each element of the iterable and
# returns an iterator containing only the elements for which the function returns True.
# A lambda function can be used as the first argument to define a filtering condition concisely.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"The even numbers in the list are: {even_numbers}")
