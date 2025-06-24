""" Check if a user-entered string contains any digits using a for loop """

# Hints:-
# Accept input from user.
# Iterate through each character in the input string using a for loop.
# For each character, check if it is a digit. You can compare its value to the range of digit characters (‘0’ to ‘9’).
# If a digit is found, you can immediately conclude that the string contains digits and return True.
# If the loop completes without finding any digits, it means the string does not contain any digits. In this case, return False

def contains_digits(string):
    for char in string:
        if "0" <= char <= "9":
            return True # Found a digit, so return True immediately
    return False # No digits found after checking all characters

user_string = input("Enter a string:- ")

if contains_digits(user_string):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")

