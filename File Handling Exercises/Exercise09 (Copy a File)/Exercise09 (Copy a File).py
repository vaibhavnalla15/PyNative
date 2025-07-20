""" Copy a File """
# Write a program that takes two filenames as input (source and destination) and copies the content of the source file to the destination file.
# Hints:-
# Open the source file in read mode, read its content, then open the destination file in write mode and write the content.

def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, "r") as source_file:
            content = source_file.read()
        with open(destination_filename, "w") as destination_file:
            destination_file.write(content)
        print(f"Successfully copied '{source_filename}' to '{destination_filename}'.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Use Case:-
source_file = "../Exercise04 (Count Words From a File)/sample.txt"
destination_file = "copied_sample.txt"
copy_file(source_file,destination_file)