""" Turn every item of a list into its square """
# Given a list of numbers. write a program to turn every item of a list into its square.
# Hints:-  Iterate numbers from a list one by one using a for loop and calculate the square of the current number

numbers = [1, 2, 3, 4, 5, 6, 7]
squared_numbers = []
for n in numbers:
    squared_numbers.append(n ** 2)
print(squared_numbers)

# Using List Comprehension:-
numbers = [1, 2, 3, 4, 5, 6, 7]
result = [n * n for n in numbers]
print(result)

