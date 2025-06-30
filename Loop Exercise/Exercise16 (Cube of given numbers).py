""" Calculate the cube of all numbers from 1 to a given number """
# Hints:-
# 1. Iterate numbers from 1 to n using for loop and range() function
# 2. In each iteration of a loop, calculate the cube of a current number (i) by multiplying itself three times (cube = i * i* i)

input_number = 6
for i in range(1, input_number + 1):
    cube = i * i * i
    print(f"Current number is {i} and the cube is:- {cube}")