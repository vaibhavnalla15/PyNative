""" Read and Write Binary """
# Write a program to read data from a binary file (“input.bin”) and write it to another binary file (“output.bin”).
# Hints:-
# 1. You need to open them in binary modes ('rb' for read binary and 'wb' for write binary).
# 2. Reading from a binary file will give you bytes objects, and you should write bytes objects to a binary file.
# 3. You can read the entire content of the source binary file and then write that directly to the destination binary file.

def copy_binary_file(source_filename, destination_filename):
    try:
        with open(source_filename, "rb") as source_file:
            binary_content = source_file.read()
        with open(destination_filename, "wb") as destination_file:
            destination_file.write(binary_content)
        print(f"Successfully copied binary file '{source_filename}' to '{destination_filename}'.")
    except FileNotFoundError:
        print(f"Error: Source binary file '{source_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_binary_file = "input.bin" # Make sure this binary file exists
destination_binary_file = "output.bin"
copy_binary_file(source_binary_file, destination_binary_file)