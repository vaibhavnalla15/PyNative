""" Padding with Zeros """
# Ask the user for a number. Print this number padded with leading zeros to a width of 5.
# For example, if the input is 12, the output should be “00012“
# Hints:-
# 1. Get the number as a string using input().
# 2. Use the zfill() string method to pad it with leading zeros to the desired width.

num = input("Enter a Number:- ")
print("The Padded Number is:- ", num.zfill(5))
