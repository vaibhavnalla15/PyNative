""" Create a string made of the first, middle and last character """
# Write a program to create a new string made of an input string’s first, middle, and last character.
# Hints:-
# 1. String index always starts with 0
# 2. Use string indexing to get the character present at the given index
# 3. Get the index of the middle character by dividing string length by 2
# 4. Use string indexing to get the character present at the given index.
# 5. Use str1[0] to get the first character of a string and add it to the result variable
# 6. Next, get the middle character’s index by dividing string length by 2. x = len(str1) /2. Use str1[x] to get the middle character and add it to
#    the result variable
# 7. Use str1[len(str1)-1] to get the last character of a string and add it to the result variable
# 8. print result variable to display new string

str1 = 'James'
print("Original String is:-", str1)

# Get first character
result = str1[0]

# Get string size
l = len(str1)

# Get middle index number
mi = int(l / 2)

# Get middle character and add it to result
result = result + str1[mi]

# Get last character and add it to result
result = result + str1[l - 1]

print("New String is:-", result)
