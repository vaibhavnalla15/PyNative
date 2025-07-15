""" Replace each special symbol with # in the following string """
# Hints:- Use string function replace()
# 1. Use the string.punctuation constant to get the list of all punctuations
# 2. Iterate each symbol from a punctuations
# 3. Use string function replace() to replace the current special symbol in a string with

import string
str1 = '/*Jon is @developer & musician!!'

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)
