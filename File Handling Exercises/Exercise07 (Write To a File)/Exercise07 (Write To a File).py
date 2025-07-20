""" Write to a file. """
# Write a Python program to create a new file named “output.txt” and write the string “Hello, PYnative!” into it.
# Hints:- Open a new file in write mode ('w') and use the write method.

filename = "output.txt"
text_to_write = "Hello, PYnative!"
try:
    with open(filename, "w") as file:
        file.write(text_to_write)
    print(f"Successfully wrote '{text_to_write}' to '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Explanation:-
# with open(filename, 'w') as file: opens the file in write mode. If “output.txt” doesn’t exist, it will be created. If it does exist,
# its contents will be overwritten.
# The with statement ensures the file is automatically closed. file.write(text_to_write) writes the specified string to the file.