""" A palindrome number is a number that remains the same when its digits are reversed. 
In simpler terms, it reads the same forwards and backward """ # Example 121 = 121

# simple code
num = input(str("Enter your number:- "))
reversed_num = num[::-1]
if num == reversed_num:
    print("The number is A palindrome number")
else:
    print("The number is Not A palindrome number")

# Using while loop:-
# 1. Initialize a variable to store the reversed number (set it to 0 initially).
# 2. Use a while loop that continues as long as the original number is greater than 0.
# 3. Inside the loop:
    # 4. Extract the last digit of the original number using the modulo operator (% 10).
    # 5. Update the reversed number: multiply it by 10 and then add the extracted last digit.
    # 6. Update the original number by integer division (// 10) to remove the last digit.
# 7. After the loop finishes, the reversed number variable will hold the reversed integer.
# 8. Now, check if it is same as original number

def is_palindrome_while_loop(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number //= 10
    return original_number == reversed_number

print(is_palindrome_while_loop(121))
print(is_palindrome_while_loop(123))