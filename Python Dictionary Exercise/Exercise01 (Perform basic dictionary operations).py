""" Perform basic dictionary operations """
# 1.  Perform following operations on given dictionary
# 2.  Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
# 3.  Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
# 4.  Access Key: Print the value associated with the city key.

# Hints:-
# 1. You can add a new key-value pair to a dictionary by simply assigning a value to a new key using square bracket notation.
# 2. Same as above you can modify an existing value by assigning a new value to an existing key using square bracket notation.

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print("Original Dictionary:-", my_dict)

# Add a new key-value pair
my_dict["profession"] = "Doctor"
print(f"Updated dictionary after adding 'profession': {my_dict}")

# Modify Value
my_dict["age"] = 40
print(f"Updated dictionary after modification: {my_dict}")

# print key
print("City:-", my_dict["city"])