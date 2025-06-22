""" Printing The Pattern """
# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# Notice that each row contains the same number repeated, and the number of repetitions increases with the row number.

# 1. You’ll need an outer loop to control the row number (from 1 to 5).
# 2. Inside this loop, you’ll need an inner loop to print the current row’s number the correct number of times.
#    The current row number will also determine how many times the inner loop runs.

for i in range(1, 6): # It runs 5 times: i = 1, 2, 3, 4, 5
    for j in range(1, i + 1):
        print(j, end=' ')
    print()