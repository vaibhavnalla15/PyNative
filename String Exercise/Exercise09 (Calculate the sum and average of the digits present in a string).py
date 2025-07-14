""" Calculate the sum and average of the digits present in a string """
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
# Hints:- Iterate each character from a string s1 and check if the current character is digit using the isdigit() function
# 1. Iterate each character from a string s1 using a loop
# 2. In the body of a loop, check if the current character is digit using the isdigit() function
# 3. If it is a digit, then add it to the sum variable
# 4. In the end, calculate the average by dividing the total by the count of digits

str1 = "PYnative29@#8496"
total = 0
cnt = 0
for i in str1:
    if i.isdigit():
        total += int(i)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:-", total, "\nAverage is:-", avg)

# Using Regular Expression:-
import re
input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

# use the built-in function sum
total = sum(digit_list)

# average = sum / count of digits
avg = total / len(digit_list)
print("Sum is:", total, "Average is ", avg)