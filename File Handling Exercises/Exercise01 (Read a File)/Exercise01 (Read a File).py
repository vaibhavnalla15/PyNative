""" Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console."""
# Hints:- You’ll need to open the file in read mode ('r') and then use a read() method to read the entire content at once.

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")
