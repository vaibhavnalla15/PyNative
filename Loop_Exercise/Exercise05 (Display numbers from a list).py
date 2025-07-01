""" Display numbers from a list using a loop """

# Write a Python program to display only those numbers from a list that satisfy the following conditions
# 1. The number must be divisible by five
# 2. If the number is greater than 150, then skip it and move to the following number
# 3. If the number is greater than 500, then stop the loop

# Hints:-
# 1. Use a for loop to iterate through each item in the list.
# 2. Use a break statement to exit the loop if the current number is greater than 500.
# 3. Use the continue statement to skip the current number and move to the next if the current number is greater than 150.
# 4. Use the condition number % 5 == 0 to check if the number is divisible by 5.

numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n > 500:
        break
    if n > 150:
        continue
    if n % 5 == 0:
        print(n)
