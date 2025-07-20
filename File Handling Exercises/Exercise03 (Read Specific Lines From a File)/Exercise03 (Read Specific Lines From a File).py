""" Exercise03 (Read Specific Lines From a File)"""
# Write a Python program to read only the first 5 lines of “sample.txt”.
# Hints:-
# 1. Use for loop with range() function as a counter to keep track of the number of lines read. Once you’ve reached the desired number of lines,
#    you can stop the reading process.
# 2. In each iteration of a loop use a readline() function to read single line from file

try:
    with open("sample.txt", encoding="utf-8") as file:
        for i in range(5):
            print(file.readline().strip())
except:
    if FileNotFoundError:
        print("Error: 'sample.txt' not found.")
    if UnicodeError:
        print("Unicode Error")

