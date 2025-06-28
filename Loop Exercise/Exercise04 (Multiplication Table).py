""" Print multiplication table of a given number """
# Hints:-
# You can use a simple for loop to generate the multiplication table for a specific number.
# 1. Set n = 2.
# 2. Use for loop to iterate the first 10 natural numbers (From 1 to 10)
# 3. In each iteration, multiply the current number by 2 ( p = n*i). Now print p

n = int(input("Enter a number for to create a Table:- "))
for i in range(1,11):
    p = n * i
    print(p)

