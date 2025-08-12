""" Design a Rectangle class with default attributes for length and width set to 1. Include methods to set these attributes and calculate the area. """

class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    def set_dimension(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rect = Rectangle()
print("Default area:", rect.area())

rect.set_dimension(4,5)
print("Updated area:",rect.area())        

        
        