""" Count Total Number of Characters in File """
# Write a function that takes a filename as input and returns the total number of characters in that file (including spaces and newlines).
# Hints:-
# Write a function that takes a filename as input and returns the total number of characters in that file (including spaces and newlines).

# Explanation:
#
# The count_characters function takes the filename as input.
# It opens the file in read mode. content = file.read() reads the entire content of the file as a single string.
# return len(content) returns the length of the content string, which represents the total number of characters (including spaces and newline characters).

# Solution:
def count_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
char_count = count_characters("sample.txt")
print(f"Total characters in 'sample.txt': {char_count}")