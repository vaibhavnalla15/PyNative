""" Person Class with __str__ Method: Create a Person class with first and last name attributes and override the __str__ method to return the full name. """

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
person = Person("John","Wick")        
print(person)