""" Find all occurrences of a substring in a given string by ignoring the case """
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
# Hints :- Use the string function count()

str1 = "Welcome to USA. usa awesome, isn't it?"
count_str = "USA"

# convert string to lowercase
lower_case = str1.lower()

# use count function
count = lower_case.count(count_str.lower())
print("The count of USA:-", count)
