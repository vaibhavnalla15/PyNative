""" Using Property Decorators: Implement a class Circle with a private attribute radius and use property decorators to get and set its value with checks. """

# Defining a class named Circle
class Circle:
    # Constructor to initialize the private attribute __radius
    def __init__(self, radius):
        self.__radius = radius  # Private attribute (cannot be accessed directly outside the class)

    # Getter method for radius using @property decorator
    @property
    def radius(self):
        return self.__radius  # Returns the current value of radius
    
    # Setter method for radius using @radius.setter decorator
    @radius.setter
    def radius(self, value):
        if value >= 0:  # Check if the radius value is non-negative
            self.__radius = value  # Update radius if the value is valid
        else:
            print("Radius cannot be negative")  # Display message for invalid value
    
    # Method to calculate and return the area of the circle
    def area(self):
        return 3.14159 * self.__radius ** 2  # Formula: π * r²

# Creating an object of Circle class with initial radius = 5
circle = Circle(5)

# Printing the area of the circle
print("Area:", circle.area())

# Trying to set a negative radius (will be rejected by setter)
circle.radius = -10

# Getting and printing the radius (will still be the old value)
print("Radius:", circle.radius)
