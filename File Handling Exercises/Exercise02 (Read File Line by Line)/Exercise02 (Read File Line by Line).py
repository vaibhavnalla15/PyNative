""" Exercise02 (Read File Line by Line)"""
# Write a Python program to read the text file named “sample.txt” line by line and print each line.
# Hints:-
# 1. Don’t load the entire file into memory at once.
# 2. Use loop to iterate through file object in Python.
# 3. In each iteration of the loop you can print single line from the file

try:
    with open("sample.txt","r") as file:
        for line in file:
            print(line, end=' ')  # The 'end=''' prevents extra newline characters
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")
