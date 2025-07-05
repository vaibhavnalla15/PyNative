""" Accept any three string from one input() call """
# Write a program to take three names as input from the user in a single call to the input() function.
# Hints :-
# 1. Ask the user to enter three names separated by space
# 2. Split input string on whitespace using the split() function to get three individual names

str1, str2, str3 = input("Enter your three names:- ").split()
print("Name 1:- ", str1)
print("Name 2:- ", str2)
print("Name 3:- ", str3)


