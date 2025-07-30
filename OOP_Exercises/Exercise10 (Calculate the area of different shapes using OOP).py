""" Calculate the area of different shapes using OOP """

# You have given a Shape class and subclasses Circle  and Square. The parent class (Shape) has a area() method.
# Now, Write a OOP code to calculate the area of each shapes (each subclass must write its own implementation of area() method to calculates its area).

# Hints:-
# Use Method Overloading.
# The core idea is that the same method name can have different implementations depending on the class of the object.
# Polymorphism lets you treat objects of different classes in a uniform way. Imagine you have a Shape class, and then you have subclasses like Circle, Square, and Triangle. Each of these shapes has an area() method, but the way you calculate the area is different for each shape.

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):         # Overriding the area method
        return 3.14159 * self.radius**2         # Area of Circle = A=πr² (π = 3.14159)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):         # Overriding the area method
        return self.side * self.side           # Area of Square = A=a²

# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())  # Output: 78.53975, 49, 28.27431