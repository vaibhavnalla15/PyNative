""" Static and Class Methods Demonstrate the use of static and class methods in a class Calculator with methods to add and multiply numbers. """

# Define a class Calculator
class Calculator:
    # Static method - does not depend on class or object data
    @staticmethod
    def add(a, b):
        # Returns the sum of two numbers
        return a + b
    
    # Class method - takes the class itself (cls) as the first argument
    @classmethod
    def multiply(cls, a, b):
        # Returns the product of two numbers
        return a * b

# Call the static method directly from the class
print("Addition:", Calculator.add(5, 3))  # Output: Addition: 8

# Call the class method directly from the class
print("Multiplication:", Calculator.multiply(4, 5))  # Output: Multiplication: 20

        
