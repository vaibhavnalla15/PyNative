""" Count the total number of digits in a number """
# Write a Python program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

# Hints :-
# 1. Set counter = 0
# 2. Run while loop till number != 0
# 3. In each iteration of a loop
# 4. Reduce the last digit from the number using floor division ( number = number // 10)
# 5. Increment counter by 1
# 6. print counter after loop execution is completed

count = 0
number = int(input("Enter numbers:- "))
while number != 0:
     # floor division to reduce the last digit from number
     number = number // 10
     count += 1             # or (count = count + 1) both are same
print("Total digits are:- ", count)






