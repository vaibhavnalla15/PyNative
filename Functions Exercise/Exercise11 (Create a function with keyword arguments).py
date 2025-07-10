""" Create a function with keyword arguments """
# The exercise requires you to create a function that can accept any number of keyword arguments. A keyword argument is where you specify
# the name of the argument along with its value (e.g., name="Alice", age=30). Inside the function, you need to access these arguments and print them
# in a key-value format.

# Create a function print_info(**kwargs) that accepts keyword arguments and prints the key-value pairs. Call it with different keyword arguments
# Hints:-
# 1. Inside, iterate through the kwargs dictionary with a for loop and .items(), printing each key and value.
# 2. Call the function a few times with different key=value pairs.

def print_info(**kwargs):
    if kwargs:
        print("\n ---- Information ----")
        for key, value in kwargs.items():
            print(f"{key}:{value}")


# Example calls to the function
print_info(name="Alice", age=30, city="New York")
print_info(job="Engineer", salary=75000)
print_info(country="USA", state="California", zip_code="90210")

