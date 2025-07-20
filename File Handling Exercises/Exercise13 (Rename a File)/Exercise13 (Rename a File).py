""" Rename a File """
# Write a program that takes an old filename and a new filename as input and renames the file. Handle potential errors if the old file doesn’t exist.
# Hints:-
# 1. The os module provides a function specifically designed for renaming files. You’ll need to provide both the old and the new filenames to this function.
# 2. The os.rename(old_filename, new_filename) renames the file from old_filename to new_filename.

import os

def rename_file(old_filename, new_filename):
    if not os.path.exists(old_filename):
        return f"Error: File '{old_filename}' not found"
    try:
        os.rename(old_filename, new_filename)
        return f"Successfully renamed '{old_filename}' to '{new_filename}'."
    except Exception as e:
        return f"An error occurred while renaming: {e}"

# Example Usage:-
old_file = "sample.txt"
new_name = "demo.txt"

print(rename_file(old_file, new_name))

