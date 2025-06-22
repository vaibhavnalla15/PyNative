""" The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10. """
# Hints
# Use nested loop, where one loop is placed inside another.
# 1. The outer loop iterates through the rows (numbers 1 to 10).
# 2. The inner loop iterates through the columns (numbers 1 to 10) to calculate and display the product of the numbers.

# Multiplication table for a specific number
num = int(input("Enter a number:- "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Full multiplication table from 1 to 10
for i in range(1, 11):
    print("Multiplication table of:", i)
    for j in range(1, 11):
        print(f"{i * j}", end = " ")
    print()
    print()

# Create multiplication table using List Comprehension
multiplication_table = [[i * j for j in range(1, 11)]for i in range(1, 11)]
for row in multiplication_table:
    print(" ".join(map(str, row)))

# Using Functions
def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Call the function
num = int(input("Enter a number: "))
print('Multiplication table of', num)
print_multiplication_table(num)

# Using String Formatting for Better Alignment
print('Full multiplication table with alignment:- ')
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:5}", end="") # :5 = format the result in 5 spaces width, right-aligned
    print()