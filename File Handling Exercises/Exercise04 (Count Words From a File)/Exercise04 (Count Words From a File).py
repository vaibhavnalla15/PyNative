""" Count Words From a File """
# Create a function that takes a filename as input and returns the total number of words in that file.
# Hints:-
# 1. You’ll need to read the file content, split it into words, and then count the number of resulting elements.
# 2. Remember to handle potential punctuation.

import re

def count_words(filename):
    try:
        with open("sample.txt", "r") as file:
            content = file.read().lower()
            words = re.findall(r'\b\w+\b', content)  # Use regex to find whole words
            return len(words)
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
word_count = count_words("sample.txt")
print(f"Total words in 'sample.txt': {word_count}")

# Code Explanation:-
# 1. We import the re module for regular expression operations.
# 2. The count_words function takes the filename as input. It opens the file in read mode. content = file.read().lower() reads the entire content
#    and converts it to lowercase to ensure consistent word counting.
# 3. words = re.findall(r'\b\w+\b', content) uses a regular expression r'\b\w+\b' to find all whole words. \b matches word boundaries,
#    and \w+ matches one or more word characters (letters, numbers, and underscore).
# 4. return len(words) returns the total number of words found. The try-except block handles the case where the file is not found
