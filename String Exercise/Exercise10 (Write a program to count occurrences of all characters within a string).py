""" Write a program to count occurrences of all characters within a string """
# Hints:- Use the string function count()
# 1. create an empty dictionary to store the result. character is the key, and the count is the value
# 2. Iterate each character from a string s1 using a loop
# 3. In the body of a loop, use the count() function to find how many times a current character appeared in a string
# 4. Add key-value pair in a dictionary

str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)
