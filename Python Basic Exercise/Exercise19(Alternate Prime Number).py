"""Print Alternate Prime Numbers till 20"""

# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11)
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

# Hints :-
# 1. First, identify all the prime numbers within the given range (1 to 20).
# 2. Use this hint to identify prime number: Check divisibility from 2 up to the square root of the number.
# If divisible by any number in this range, it’s not prime. Handle cases for numbers less than or equal to 1 and the number 2 separately.
# 3. Now, once you have the list of prime numbers, you need to pick every other prime number from that list,
# starting with the first one using with a specific step.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Set N
n = 20
primes = []  # List to store all prime numbers
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)

# Printing all prime numbers
print(f'All prime numbers from 1 to {n}: {primes}')

# Printing alternate prime numbers from the list
print(f'Alternate prime numbers from 1 to {n}:')
for i in range(0, len(primes), 2):  # Step by 2 to get alternate primes
    print(primes[i], end=" ")

