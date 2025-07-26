""" Define a property that must have the same value for every class instance (object) """
# Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.
# Hints:- Define a color as a class variable in a Vehicle class

# Expected Output:-
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:

    # class Attribute
    color = "White"

    def __init__(self, name, max_speed, mileage, color="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240 , 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

# Variables created in __init__() are called instance variables. An instance variable’s value is specific to a particular instance of the class.
# For example, in the solution, all Vehicle objects have a name and a max_speed,
# but the values of the name and max_speed variables will vary depending on the Vehicle instance.
# On the other hand, a class variable is shared between all class instances. You can define a class attribute by assigning a value to a variable name
# outside of __init__().
