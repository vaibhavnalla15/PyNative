""" Abstract Classes - Polygon Calculator: Define an abstract base class Polygon with an abstract method area. Implement this in derived classes Rectangle and Triangle. """

# Importing ABC (Abstract Base Class) and abstractmethod from the abc module
# These are used to create abstract classes in Python
from abc import ABC, abstractmethod

# Creating an abstract class named Polygon
# Abstract classes cannot be instantiated directly.
# They are meant to be inherited by other classes.
class Polygon(ABC):

    # Defining an abstract method named 'area'
    # Abstract methods are declared but have no implementation here.
    @abstractmethod
    def area(self):
        pass  # 'pass' means "do nothing here" — subclasses will define this method


# Creating a class Rectangle that inherits from Polygon
class Rectangle(Polygon):
    
    # Constructor method (__init__) to initialize width and height attributes
    def __init__(self, width, height):
        self.width = width      # Instance attribute for width
        self.height = height    # Instance attribute for height

    # Implementing the abstract method 'area' for Rectangle
    def area(self):
        return self.width * self.height  # Formula for rectangle area: width × height


# Creating a class Triangle that also inherits from Polygon
class Triangle(Polygon):

    # Constructor method (__init__) to initialize base and height attributes
    def __init__(self, base, height):
        self.base = base        # Instance attribute for base
        self.height = height    # Instance attribute for height
    
    # Implementing the abstract method 'area' for Triangle
    def area(self):
        return 0.5 * self.base * self.height  # Formula for triangle area: ½ × base × height


# Creating an object of Rectangle with width=10 and height=20
rect = Rectangle(10, 20)

# Creating an object of Triangle with base=10 and height=10
tri = Triangle(10, 10)

# Printing the area of the rectangle using its area() method
print("Area of Rectangle:", rect.area())

# Printing the area of the triangle using its area() method
print("Area of Triangle:", tri.area())

