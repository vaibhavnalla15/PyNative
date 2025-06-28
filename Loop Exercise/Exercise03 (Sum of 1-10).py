""" Calculate sum of all numbers from 1 to a given number """
# Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10, the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# Approach 1: Use for loop and range() function:-
# 1. Create a variable s and initialize it to 0 to store the sum of all numbers.
# 2. Use Python 3’s built-in input() function to take input from the user.
# 3. Convert the user’s input to an integer type using the int() constructor and save it to a variable n.
# 4. Run loop n times using for loop and range() function
# 5. In each iteration of the loop, add the current number (i) to the variable s.
# 6. Use the print() function to display the value of the variable s on the screen.
#
# Approach 2: Use the built-in function sum(). The sum() function calculates the addition of all numbers from 1 to a given number.

# Approach 1:-
# s: store sum of all numbers
s = 0
n = int(input("Enter a number:- "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("Sum is:- ", s)

# Approach 2:-
n = int(input("Enter a number:- "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print("Sum is:- ", x)