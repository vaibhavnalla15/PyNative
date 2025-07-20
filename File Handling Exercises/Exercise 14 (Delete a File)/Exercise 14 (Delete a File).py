""" Delete a File """
# Write a program that takes a filename as input and deletes the file. Handle potential errors if the file doesn’t exist.
# Hints:-
# The os module also has a function for removing files. It’s good practice to check if file exists to prevent errors before deleting it.
# The os.remove(filename) deletes the specified file.

import os

def file_to_remove(filename):
    if not os.path.exists(filename):
        return f"Error: File '{filename}' not found."
    try:
        os.remove(filename)
        return f"Successfully deleted {filename}"
    except Exception as e:
        return f"An error occurred while deleting: {e}"

# Example Usage:-
file_to_delete = "sample.txt"

# Create a dummy file to test deletion
with open(file_to_delete, 'w') as f:
    f.write("This file will be deleted.")

result = file_to_remove(file_to_delete)
print(result)