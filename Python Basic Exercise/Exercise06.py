""" Write a Python code to display numbers from a list divisible by 5 """
# 1. Iterate through each number in the list using a for loop.
# 2. For each number, use the modulo operator (%) to find the remainder when divided by 5. If the remainder is 0,
# it means the number is divisible by 5. In that case, print the number.

num_list = [10, 20, 33, 46, 55]
print("Given list is :", num_list)
print('Divisible by 5:')
for n in num_list:
    if n % 5 == 0:
        print(n)





