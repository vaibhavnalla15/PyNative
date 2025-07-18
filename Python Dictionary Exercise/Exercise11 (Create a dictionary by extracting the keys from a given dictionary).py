""" Create a dictionary by extracting the keys from a given dictionary """
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# Hints:-
# 1. Iterate the mentioned keys using a loop
# 2. Next, check if the current key is present in the dictionary, if it is present, add it to the new dictionary

# Solution 1: Dictionary Comprehension
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# Using Dictionary comprehension.
new_dict = {k: sample_dict[k] for k in keys}
print(new_dict)

# Solution 2: Using the update() method and loop
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
result = dict()

for k in keys:
    result.update({k: sample_dict[k]})
print(result)
