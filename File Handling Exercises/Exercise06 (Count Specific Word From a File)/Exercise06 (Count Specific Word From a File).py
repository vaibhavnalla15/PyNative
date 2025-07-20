""" Count Specific Word From a File """
# Write a program to count the occurrences of a specific word (e.g., “hello”) in a given file.
# Hints:-
# Open the file, read its content, To count a specific word, you should probably convert the entire text to a consistent case
# (either lowercase or uppercase) to avoid missing matches due to capitalization. Then, split the text into individual words and iterate
# through them to check for your target word.

import re

word_to_count = "hello"

with open("sample.txt", "r") as file:
    text = file.read().lower()
    # \bhello\b matches only the word "hello" as a whole word
    matches = re.findall(rf'\b{word_to_count}\b', text)

print(f"The word '{word_to_count}' occurred {len(matches)} times.")

# Explanation:-
# Using regular expressions (re) with \b to match whole words only, ignoring commas, dots, or exclamations.