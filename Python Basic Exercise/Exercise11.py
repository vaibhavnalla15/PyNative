# """ Get each digit from a number in the reverse order. """
# # For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

num = input("Enter a Number:- ")

new_num = num[::-1]
print(' '.join(str(new_num)))

# or

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10     # 7536 % 10 = 6 ✅ (last digit)
    # remove the last digit and repeat the loop
    number = number // 10   # This removes the last digit of the number.
    print(digit, end=" ")

