""" Pattern Printing """
# Write a Python program to print the reverse number pattern using a for loop.
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# Hints:-
# 1. Setting the row value to 5 is crucial, as the pattern we’re working with has five rows.
# 2. Using a for loop and the range() function, create an outer loop that iterates through numbers from 1 to 5.
# 3. The outer loop controls the number of iterations of the inner loop. For each outer loop iteration, the number of inner loop
#    iterations is reduced by i, the outer loop’s current number.
# 4. In each iteration of the inner loop, print the iterator variable of the inner loop (j).

# Note:
# 1. In the first iteration of the outer loop, the inner loop executes five times.
# 2. In the second iteration of the outer loop, the inner loop executes four times.
# 3. In the last iteration of the outer loop, the inner loop will execute only once.

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
