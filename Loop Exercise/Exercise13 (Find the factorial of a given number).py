""" Find the factorial of a given number """
# Write a Python program to use for loop to find the factorial of a given number.
# The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.
# For example, a factorial of 5! is 5 × 4 × 3 × 2 × 1 = 120

# Hints:-
# 1. Set variable factorial = 1 to store the factorial of a given number
# 2. Iterate numbers starting from 1 to the given number n using for loop and range() function. (here, the loop will run five times because n is 5)
# 3. In each iteration, multiply the factorial by the current number and assign it again to a factorial variable (factorial = factorial *i)
# 4. After the loop completes, print factorial.

factorial = 1
num = 5
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)