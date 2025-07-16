""" Sum and average of all numbers in a list """
# Calculate and print the sum and average of all numbers in a list.
# Hints:-
# Python has built-in functions sum() to easily calculate the sum of numbers in a list and to determine the number of elements (length) in a list.

my_list = [10, 20, 30, 40, 50]

total_sum = sum(my_list)
print("Sum:-", total_sum)

# The average is the sum divided by the number of elements
average = total_sum / len(my_list)
print("Average:-", average)