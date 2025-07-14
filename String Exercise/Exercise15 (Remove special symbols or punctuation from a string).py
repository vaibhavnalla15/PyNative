""" Remove special symbols / punctuation from a string """


# GIVEN = "/*Jon is @developer & musician" , Output = "Jon is developer musician"
# Hints:-
# 1. Use string functions translate() and maketrans()
# 2. Use the translate() function to get a new string where specified characters are replaced with the character described in a dictionary or a mapping table.
# 3. Use the maketrans() function to create a mapping table.
# 4. Or Use the regex in Python.

# Solution 1: Use string functions translate() and maketrans().
# The string.punctuation constant contain all special symbols.
import string
str1 = "/*John is @developer & musician"

new_str = str1.translate(str.maketrans("","", string.punctuation))
print("New string is:-", new_str)

# Solution 2: Using regex replace pattern in a string
import re
# replace special symbols with ''
result = re.sub(r'[^\w\s]', '', str1)
print("New string is:-", result)