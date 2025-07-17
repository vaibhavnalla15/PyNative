"""  Perform dictionary operations """

# Perform following operations on given dictionary
# Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
# Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary

# Hints:-
# 1. Use the del keyword to remove a key-value pair from a dictionary by specifying the key.
# 2. Use dictionary method items(), that returns a view object of all key-value pairs. You can iterate over this view.
# 3. Use the in keyword is to check for the existence of a key in a dictionary

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print("Original Dictionary is:-", my_dict)

# Remove the 'model' key-value pair using del
del my_dict["profession"]
print(f"Updated dictionary after removing 'profession': {my_dict}")

print("Printing all key-value pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

def check_key_exists(dictionary, key_to_check):
    return key_to_check in dictionary

key1 = 'age'
print(f"Does '{key1}' exist? {check_key_exists(my_dict, key1)}")
