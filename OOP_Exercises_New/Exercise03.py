""" Build a class Employee with multiple constructors that can initialize an employee object in different ways. """

class Employee:
    def __init__(self, name, Id=None, department= None):
        self.name = name
        self.id = Id
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        if self.id:
            print(f"ID: {self.id}")
        if self.department:
            print(f"Department: {self.department}")

emp1 = Employee("John")

emp2 = Employee("Jane", 100)

emp3 = Employee("James", 101, "HR")

emp1.display_details()
print("-------------------")
emp2.display_details()
print("-------------------")
emp3.display_details()
