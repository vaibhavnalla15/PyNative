""" Display Fibonacci series up to 10 terms """
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the
# two numbers before it. The first two numbers are 0 and 1.

# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.

# Hints:-
# 1. Set num1 = 0 and num2 = 1 (first two numbers of the sequence)
# 2. Run the loop 10 times
# 3. In each iteration
# 4. print num1 as the current number of the sequence
# 5. Add the last two numbers to get the following number result = num1 + num2
# 6. update values of num1 and num2. Set num1 = num2 and num2 = result

num1 = 0
num2 = 1
for i in range(10):
    # print next number of a series
    print(num1,  end= " ")
    # add last two numbers to get next number
    result = num1 + num2
    # update values
    num1 = num2
    num2 = result