""" Split a string on hyphens """
# Write a program to split a given string on hyphens and display each substring.
# Hints:- Use the string function split()

str1 = "Emma-is-a-data-scientist"
# split string
sub_strings = str1.split("-")

for sub in sub_strings:
    print(sub)