""" Find largest and smallest digit in a number """
# Hints:-
# 1. Get Number and treat the Number as a Sequence of Digits.
# 2. Handle the sign (maybe take the absolute value).
# 3. Convert the (absolute) number to a string.
# 4. Initialize variables to store the largest and smallest digits (perhaps with the first digit of the string converted to an integer).
# 5. Loop through the remaining characters of the string (starting from the second character).
# Inside the loop:
    # 1. Convert the current character to an integer.
    # 2. Compare it with the current largest and smallest, updating if necessary.
# 6. Return or print the largest and smallest digits.


def find_largest_smallest_digit(number):
    if number == 0:
        print("The number is zero. Largest and smallest digit is 0.")
        return 0, 0

    str_number = str(abs(number)) # Convert to string and handle negative numbers
    largest_digit = int(str_number[0])
    smallest_digit = int(str_number[0])

    for digit in str_number[1: ]:
        digit_int = int(digit)
        if digit_int > largest_digit:
            largest_digit = digit_int
        if digit_int < smallest_digit:
           smallest_digit = digit_int

    return largest_digit, smallest_digit

# Example usage:

num1 = 9876543210
largest1, smallest1 = find_largest_smallest_digit(num1)
if largest1 is not None:
  print(f"Largest digit in {num1}: {largest1}")
  print(f"Smallest digit in {num1}: {smallest1}")
print()

num2 = -5082
largest2, smallest2 = find_largest_smallest_digit(num2)
if largest2 is not None:
  print(f"Largest digit in {num2}: {largest2}")
  print(f"Smallest digit in {num2}: {smallest2}")
