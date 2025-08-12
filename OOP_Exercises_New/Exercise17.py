"""  Multiple Inheritance - Battery and GPS Tracker: Create classes Battery and GPS with respective methods charge and location. Derive a SmartPhone class that inherits both functionalities. """

# Define a class named Battery
class Battery:
    # Method to simulate charging the battery
    def charge(self):
        print("Charging the Battery")

# Define a class named GPS
class GPS:
    # Method to simulate getting the current location
    def location(self):
        print("Current location is 123, 456")

# Define a class named SmartPhone that inherits from BOTH Battery and GPS
# This is an example of Multiple Inheritance
class SmartPhone(Battery, GPS):
    pass  # No extra methods or attributes, but inherits from both parent classes

# Create an object (instance) of the SmartPhone class
phone = SmartPhone()

# Call the 'charge' method inherited from Battery class
phone.charge()

# Call the 'location' method inherited from GPS class
phone.location()
