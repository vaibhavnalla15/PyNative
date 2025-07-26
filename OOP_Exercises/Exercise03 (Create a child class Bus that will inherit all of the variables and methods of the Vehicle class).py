""" Create a child class Bus that will inherit all of the variables and methods of the Vehicle class """
# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo Bus", 180,12)
print(f"Vehicle Name:-'{School_Bus.name}', its speed is {School_Bus.max_speed} km/h, mileage is {School_Bus.mileage}.")