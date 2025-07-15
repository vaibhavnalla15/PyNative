""" Find words with both alphabets and numbers """
# Write a program to find words with both alphabets and numbers from an input string.
# Hints:- Use the built-in function any() with the combination of string functions isalpha() and isdigit()

str1 = "Emma25 is Data scientist50 and AI Expert"
result = []
temp = str1.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        result.append(item)

for i in result:
    print(i)
