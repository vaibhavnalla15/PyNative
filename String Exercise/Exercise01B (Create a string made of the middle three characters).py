""" Create a string made of the middle three characters """
# Write a program to create a new string made of the middle three characters of an input string.
# Hints:-
# 1. First, get the middle index number by dividing string length by 2.
# 2. Use string slicing to get the middle three characters starting from the middle index to the next two character

def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    result = str1[mi - 1 : mi + 2]
    print("Middle three characters are:-", result)

get_middle_three_chars("JohnDipPeta")
print()     # Just added to give space between
get_middle_three_chars("JaSonAy")