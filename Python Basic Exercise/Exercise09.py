""" Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward.
For example, 545 is a palindrome number. """

# Approach 1:
#
# 1. Take the input number.
# 2. Convert the number to a string.
# 3. Reverse the string.
# 4. Compare the original string with the reversed string. R
# 5. Return True if they are the same, False otherwise.

# Approach 2:Reverse the given number using while loop and save it in a different variable.
# Use the if condition to check if the original and reverse numbers are identical. If yes, return True.

# Approach 1:
def palindrome():
    num = input(str("Enter a number:- "))
    reversed_num = (num[::-1])

    if num == reversed_num:
        print("The number is Palindrome")
    else:
        print("The number is not Palindrome")

palindrome()

# Approach 2
def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)


