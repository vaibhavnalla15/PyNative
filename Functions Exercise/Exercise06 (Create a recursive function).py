""" Create a recursive function """
# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself repeatedly.

def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

result = addition(10)
print(result)

