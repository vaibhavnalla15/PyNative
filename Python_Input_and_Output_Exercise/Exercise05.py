""" Accept a list of 5 float numbers as an input from the user """
# Hints:-
# 1. Create a list variable named numbers.
# 2. Run a loop five times. In each iteration of the loop, use the input() function to get input from the user.
# 3. Convert the user’s input to a floating-point number using the float() constructor.
# 4. Add the floating-point number to the numbers list using the append() function.

numbers = []
for num in range(5):
    new_num = float(input("Enter the number:- "))
    numbers.append(new_num)
print(numbers)
