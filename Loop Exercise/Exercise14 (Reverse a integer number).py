""" Reverse a integer number """
# Hints:-
# 1. Initialize a variable to store the reversed number (set it to 0 initially).
# 2. Use a while loop that continues as long as the original number is greater than 0.
# 3. Inside the loop:
# 4. Extract the last digit of the original number using the modulo operator (% 10).
# 5. Update the reversed number: multiply it by 10 and then add the extracted last digit.
# 6. Update the original number by integer division (// 10) to remove the last digit.
# 7. After the loop finishes, the reversed number variable will hold the reversed integer.

num = 76542
reverse_number = 0
print("Given Number ", num)

while num > 0:
    reminder = num % 10                                 # Extract the last digit of the original number using the modulo operator (% 10)
    reverse_number = reverse_number * 10 + reminder
    num = num // 10
print("Revere Number ", reverse_number)
