""" Class Inheritance """
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Simple Method:-
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    pass

School_Bus =  Bus("School Volvo Bus", 180,12)
seating_capacity = School_Bus.seating_capacity(50)

# print(f"Vehicle Name:-'{School_Bus.name}', its speed is {School_Bus.max_speed} km/h, mileage is {School_Bus.mileage} and {seating_capacity}")
print(f"{seating_capacity}")

# Default Value Method:-
class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())