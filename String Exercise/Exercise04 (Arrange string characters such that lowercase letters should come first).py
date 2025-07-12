""" Arrange string characters such that lowercase letters should come first """
# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

# Hints:-
# 1. Iterate each character from a string and check if the current character is the lower or upper case using islower() string function
# 2. Create two lists lower and upper
# 3. Iterate a string using a for loop
# 4. In each loop iteration, check if the current character is the lower or upper case using the islower() string function.
# 5. If a character is the lower case, add it to the lower list, else add it to the upper list
# 6. to join the lower and upper list using a join() function.
# 7. convert list to string
# 8. print the final string

str1 = "PyNaTive"       # Output should be "yaivePNT"
lower = []
upper = []

for n in str1:
    if n.islower():
        lower.append(n)
    else:
        upper.append(n)

sorted_list = "".join(lower + upper)
print("Original string is:-", str1)
print("Result is:-",sorted_list)