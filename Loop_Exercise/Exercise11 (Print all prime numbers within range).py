""" Print all prime numbers within a range """
# Note: A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11)
# A Prime Number is a natural number greater than 1 that cannot be made by multiplying other whole numbers.
# Examples:-
# 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply to make it.

# Hints:-
# 1. Iterate through each number in the given range.
# 2. For each number, assume it’s prime initially.
# 3. Check for divisibility from 2 up to the square root of the number.
# 4. If divisible by any number in this range, it’s not prime.
# 5. If the inner loop completes without finding a divisor and the number is greater than 1, then it’s prime.
# 6. Print the numbers identified as prime.
# 7. Remember to handle numbers less than or equal to 1.

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
