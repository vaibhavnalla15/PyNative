""" Access Nested Dictionary """
# Given a nested dictionary {'person': {'name': 'Alice', 'age': 30}}, print Alice’s age.
# Hints:-
# To access values in a nested dictionary, you use multiple sets of square brackets, chaining the key lookups for each level of nesting.

data = {'person': {'name': 'Alice', 'age': 30}}

# Access Alice's age
# 1. Access the 'person' key to get the inner dictionary
# 2. Access the 'age' key within that inner dictionary
alice_age = data['person']['age']
print(f"Alice's age is: {alice_age}")