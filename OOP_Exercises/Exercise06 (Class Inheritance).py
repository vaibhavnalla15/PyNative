""" Class Inheritance """

# Create a Bus child class that inherits from the Vehicle class. The default fare charge for any vehicle is its seating capacity multiplied by 100 (seating capacity * 100).
# If the vehicle is a Bus instance, we need to add an extra 10% to the full fare as a maintenance charge. Therefore, the total fare for a Bus instance will be the final amount, calculated as total fare plus 10% of the total fare. (final amount = total fare + 10% of the total fare.)
# Note: The bus seating capacity is 50, so the final fare amount should be 5500.

# Expected Output :- Total Bus fare is: 5500.0

# Hints:- You need to override the fare() method of the Vehicle class in the Bus class.
# Use super() function within a child class to call methods of a parent (or super) class.
# Method overriding lets a subclass provide its own version of a method that its superclass already has. It allows the subclass to customize or specialize the behavior inherited from the superclass.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 /100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


