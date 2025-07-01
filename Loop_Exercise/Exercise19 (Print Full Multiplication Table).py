""" Print Full Multiplication Table """
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
# Write a code to generates a complete multiplication table for numbers 1 through 10.

# Hints:-
# Use nested loop, where one loop is placed inside another.
    # 1. The outer loop iterates through the rows (numbers 1 to 10).
    # 2. The inner loop iterates through the columns (numbers 1 to 10) to calculate and display the product of the numbers.

for i in range(1, 11):
    print('Multiplication table of:-', i)
    for j in range(1, 11):
        print(f" {i * j}", end="")
    print()
    print()