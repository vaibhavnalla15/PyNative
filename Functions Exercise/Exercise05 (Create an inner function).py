""" Create an inner function """
# Create a program with nested functions to perform an addition calculation as follows:
# 1. Define an outer function that accepts two parameters, a and b.
# 2. Inside this outer function, define an inner function that calculates the sum of a and b.
# 3. The outer function should then add 5 to this sum.
# 4. Finally, the outer function should return the resulting value.”

# outer function
def outer_fun(a, b):
    pass    # This function does nothing

    # inner function
    def addition(x, y):
        return x + y

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)