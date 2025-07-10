""" Create Higher-Order Function """
# Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, and
# returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).
# The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.
# Hints:-
# The apply_operation function takes a function func as its first argument and then calls this function with the provided numbers x and y. You can
# define the functions to be passed to apply_operation using either regular function definitions (def) or lambda functions for more concise operations.

def apply_operation(func, x, y):
    """
      Applies a given function to two numbers.

      Args:
        func: The function to apply (should take two arguments).
        x: The first number.
        y: The second number.

      Returns:
        The result of calling func(x, y).
      """
    return func(x, y)

# Demonstrate with addition using a regular function
def add(a, b):
  return a + b

result_add = apply_operation(add, 5, 3)
print(f"Result of addition: {result_add}")

# Demonstrate with subtraction using a lambda function
subtract = lambda a, b: a - b
result_subtract = apply_operation(subtract, 10, 4)
print(f"Result of subtraction: {result_subtract}")

# Demonstrate with multiplication using another lambda function
multiply = lambda a, b: a * b
result_multiply = apply_operation(multiply, 2, 6)
print(f"Result of multiplication: {result_multiply}")