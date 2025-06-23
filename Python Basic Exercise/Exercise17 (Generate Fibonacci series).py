"""Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is
found by adding up the two numbers before it. The first two numbers are 0 and 1."""
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
# Hints :-

# Set num1 = 0 and num2 = 1 (first two numbers of the sequence)
# Run the loop 15 times
# In each iteration
    # print num1 as the current number of the sequence
    # Add the last two numbers to get the following number result = num1 + num2
    # update values of num1 and num2. Set num1 = num2 and num2 = result

# Simple Code
num1 , num2 = 0, 1          # first two numbers
for i in range(15):         # run loop 15 times
    print(num1, end=" ")    # print next number of a series
    result = num1 + num2    # add last two numbers to get next number

    num1 = num2             # update values
    num2 = result

# Using a Function :-
def fibonacci_iterative(n):
    if n <= 0:
        return "Please enter a positive number!"  # Handle invalid input
    elif n == 1:
        return [0] # If only one number is needed, return [0]
    elif n == 2:
        return [0, 1] # If two numbers are needed, return [0, 1]

    fib_series = [0, 1] # Start with the first two Fibonacci numbers

    for i in range(2, n): # Start loop from 3rd number (index 2)
        next_number = fib_series[i - 1] + fib_series[i - 2] # Start loop from 3rd number (index 2)
        fib_series.append(next_number)
    return fib_series # Return the full Fibonacci series

print(fibonacci_iterative(15))

