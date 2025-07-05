""" Percentage Display"""
# Ask the user for a numerator and a denominator. Calculate the percentage and display it with two decimal places followed by a
# percent sign (e.g., 75.50%).
# Hints:-
# 1. Get the numerator and denominator using input() function and convert them to floating-point numbers using float() function.
# 2. Calculate the percentage. Use an f-string with formatting specifiers to display the result with two decimal places and the percent sign

# Simple code
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

percentage = (numerator / denominator) * 100
print(f"{percentage:.2f} %")

# Using Error Handling:-
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    if denominator == 0:
        print("Error: Denominator cannot be zero.")
    else:
        percentage = (numerator / denominator) * 100
        print(f"The percentage is:- {percentage:.2f} %")
except ValueError:
    print("Invalid Input. Please enter numbers.")
