""" Dynamic Attribute Addition Demonstrate dynamic attribute addition where a class Vehicle starts without defined attributes and properties are added later. """

# Define an empty class named Vehicle
class Vehicle:
    pass  # 'pass' is a placeholder that does nothing (used to define an empty class or function)

# Create an object 'car' from the Vehicle class
car = Vehicle()

# Dynamically add attributes to the 'car' object
# Normally, attributes are defined in __init__, but here we are adding them directly
car.make = "Toyota"  # type: ignore → Ignores type checker warnings
car.model = "Camry"  # type: ignore → Ignores type checker warnings

# Print the attributes in a formatted string
print(f"Car: {car.make} {car.model}")  # type: ignore
