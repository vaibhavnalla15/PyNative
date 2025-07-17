""" Count Character Frequencies """
# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
# Hints:-
# 1. First, iterate through each character in the string using for loop.
# 2. For each character, check if it’s already a key in your frequency dictionary using get() method. If it is, increment its count; otherwise,
# add it as a new key with a count of 1.

def count_char_frequencies(input_string):
    frequency_dict = {}
    for char in input_string:
        # Use get() method: if char is in dict, get its value; otherwise, default to 0
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict

string1 = 'Jessa'
print(f"Frequencies for '{string1}': {count_char_frequencies(string1)}")
