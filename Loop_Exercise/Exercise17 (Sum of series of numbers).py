""" Find the sum of a series of a number up to n terms """
# Write a program to calculate the sum of this series up to n terms.
# For example, if the number is 2 and the number of terms is 5, then the series will be 2+22+222+2222+22222=2469

# Hints:-
# 1. Initialize a variable sum with the base number.
# 2. Initialize a variable current_term with the base number.
# 3. Loop n-1 times (since the first term is already accounted for in the initialization).
# Inside the loop:
    # 1. Update current_term: multiply it by 10 and add the base number.
    # 2. Add the updated current_term to the sum.
# 4. After the loop, the sum variable will hold the result

# number of terms
num = 2
terms = 5
# Expected output: 24690
sum = 0

for i in range(0, terms):
    print(num , end=" + ")
    sum += num
    num = num * 10 + 2
print("\nSum of above series is: ", sum)