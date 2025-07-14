""" Find the last position of a given substring """
# Write a program to find the last position of a substring “Emma” in a given string.
# Hints:- Use the string function rfind()

str1 = "Emma is a data scientist who knows Python. Emma works at google."
index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:-", index)