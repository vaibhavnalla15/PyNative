""" Determine if School_bus is also an instance of the Vehicle class """ 
# Hints:- Use isinstance() function

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

class Bike:                                     # This class does not belongs to any object we use.
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))          # This class Vehicle returns True, also we can use Bus class also.

print(isinstance(School_bus, Bike))             # This class Bike returns False, because School bus object does not belong to Bike class.
