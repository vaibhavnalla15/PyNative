""" Generate 3 Random Integers """
# Write a code to generate 3 random integers between 100 and 999 which is divisible by 5

import random
for num in range(3):
    print(random.randrange(100,999,5), end=" ") # Step= 5 is used to take multiples of 5 like 105, 110, 115...
