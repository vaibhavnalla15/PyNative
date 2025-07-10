""" Write a recursive function to calculate the factorial """
# Write a recursive function to calculate the factorial of a non-negative integer.
# Hints:-
# 1. Base Case: The function needs a condition to stop calling itself. What is the factorial of 0?
# 2. Recursive Step: If n is not 0, the factorial of n is n times the factorial of what?
# 3. Function Call: The function should call itself with a modified argument.

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0:
        return 1    # Base case: factorial of 0 is 1
    else:
        return n * factorial_recursive(n - 1) # Recursive step  # 5! = 5 * 4 * 3 * 2 * 1 = 120

# Example Usage:
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}")  # 5! = 5 * 4 * 3 * 2 * 1 = 120

