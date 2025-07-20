""" File Existence Check """
# Write a function that takes a filename as input and returns True if the file exists and False otherwise.
# Hints:-
# 1. You need to use a os module that provides functions for interacting with the operating system.
# 2. This module has a function to check if a file path points to an existing file.
# 3. The os.path.exists(filename) checks if the file specified by filename exists. It returns True if the file or directory exists, and False otherwise.

import os

def check_file_exists(filename):
    return os.path.exists(filename)

# Example usage:
# Use case 1
filename1 = "../Exercise01 (Read a File)/sample.txt"  # Returns True because it exists in other directory.
exists = check_file_exists(filename1)
print(f"Does '{filename1}' exist? {exists}")

# Use case 2
filename2 = "sample.txt"                              # Returns False because it doesn't exist in this folder
exists = check_file_exists(filename2)
print(f"Does '{filename2}' exist? {exists}")
