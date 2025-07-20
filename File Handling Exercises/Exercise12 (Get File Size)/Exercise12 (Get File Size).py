""" Get File Size """
# Write a program to get the size of a file (in bytes).
# Hints:-
# Similar to checking for existence, you’ll need to use the os module.
# There’s a function to get file-related information, and within that information, you can find the size of the file.
# os.path.getsize('file_path'): Return the file size in bytes.
# The os.rename(old_filename, new_filename) renames the file from old_filename to new_filename.

import os

def get_file_size(filename):
    try:
        size_in_bytes = os.path.getsize(filename)
        return size_in_bytes
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example Usage:-

filename0 = "../Exercise01 (Read a File)/sample.txt"
size = get_file_size(filename0)
print(f"The size of '{filename0}' is: {size} bytes.")

filename1 = "../Exercise02 (Read File Line by Line)/sample.txt"
size = get_file_size(filename1)
print(f"The size of '{filename1}' is: {size} bytes.")
