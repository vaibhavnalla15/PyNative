""" Car Class: Create a Car class with attributes make, model, and year. Include a method to display the details of the car. """

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

my_car = Car("Toyota", "Corolla", 2021)
my_car.display()
        
