""" Operator Overloading Create a Vector class that supports addition using the + operator, allowing you to add two vectors. """

# Define a class to represent a mathematical vector
class Vector:
    # Constructor method to initialize x and y coordinates
    def __init__(self, x, y):
        self.x = x  # Store x-coordinate
        self.y = y  # Store y-coordinate

    # Magic method for adding two Vector objects
    def __add__(self, other):
        # Returns a new Vector whose coordinates are the sum of the two vectors
        return Vector(self.x + other.x, self.y + other.y)

    # Magic method to convert Vector object into a readable string
    def __str__(self):
        return f"{self.x}, {self.y}"  # Represent the vector as "x, y"

# Create first vector (2, 4)
v1 = Vector(2, 4)

# Create second vector (1, -1)
v2 = Vector(1, -1)

# Print the result of vector addition
print("Vector Addition:", v1 + v2)  # Output: Vector Addition: 3, 3


        