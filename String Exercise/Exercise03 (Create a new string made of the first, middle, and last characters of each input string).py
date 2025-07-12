""" Create a new string made of the first, middle, and last characters of each input string """
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
# Hints:-
# 1. String index starts with index 0. The first character is present at index 0, and the last character is at the index string’s length -1
# 2. Use built-in function len(s1) to get the string length.
# 3. Next, get the middle index number by dividing string length by 2.
# 4. Get the first character from both strings, concatenate them, and store them in variable x
# 5. Get the middle character from both strings, concatenate them, and store them in variable y
# 6. Get the last character from both strings, concatenate them, and store them in variable z
# 7. In the end, join x, y, and z and save it in the result variable
# 8. print the result

def mix_string(s1, s2):
    print(f"Original string is:- {s1} & {s2}")

    # get first character from both string
    first_char = s1[0] + s2[0]

    # get middle character from both string
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_char + middle_char + last_char
    print("Mixed String is:-", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)
