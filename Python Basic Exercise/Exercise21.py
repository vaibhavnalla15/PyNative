""" Capitalize the first letter of each word in a string """
# Hints:-
# Separate the individual words in the string based on whitespace using string split() method.
# Once you have a list of words, you can iterate through this list and capitalize the first letter of each word using built-in string method
# After capitalizing each word, join them back together into a single string, likely with spaces in between.

def capitalize_words(text):
    words = text.split()                                        # Split the string into a list of words
    capitalized_words = [words.capitalize() for word in words]  # Capitalize each word
    return " ".join(capitalized_words)                          # Join the capitalized words back into a string

# Get input from the user
str1 = "pynative.com is for python lovers"

capitalized_string = capitalize_words(str1)
print("Capitalized string:", capitalized_string)

