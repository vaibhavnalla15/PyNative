""" Print the alternate numbers pattern """
# Hints:-
# You need to use two nested loop inside a single loop.
# Think about how the numbers are arranged in each row and how that arrangement changes from one row to the next. Consider these points:
    # 1. Row Number: Notice that the behavior of the numbers in a row depends on whether the row number is odd or even.
    # 2. Number of Elements per Row: The first row has one number, the second has two, the third has three, and so on. The ith row contains i numbers.
    # 3. Odd Rows: In odd-numbered rows (1st, 3rd, 5th, etc.), the numbers are printed in increasing order.
    # 4. Even Rows: In even-numbered rows (2nd, 4th, etc.), the numbers are printed in decreasing order.
    # 5. Starting Number: You need to keep track of the starting number for each row. Observe how the last number of one row relates to the first number
    # of the next row.
# Try to use these observations to build your logic row by row. You’ll likely need a loop that iterates through the rows, and inside that loop,
# you’ll have different logic based on whether the current row is odd or even.

# Print the following Pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def print_alternate_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        if i % 2 != 0: # Odd row: increasing order
            for x in range(num, num + i):
              print(x, end=' ')
            print() # to display next row of number on new line
        else: # Even row: decreasing order
            for y in range(num + i - 1, num - 1, -1):
              print(y, end=' ')
            print() # # to display next row of number on new line
        num += i

# Call the function to print the pattern with a specified number of rows
print_alternate_pattern(5)