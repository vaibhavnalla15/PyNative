""" Managing Private Attributes Create a Person class with private attributes name and age and provide getter and setter methods to manage these attributes safely. """

# Class with encapsulation using @property and @setter
class Person:
    def __init__(self, name, age):
        # Private attributes (cannot be accessed directly outside the class)
        self.__name = name
        self.__age = age

    # Getter for 'name' property
    @property
    def name(self):
        return self.__name

    # Setter for 'name' property with validation
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:  # Check if value is a non-empty string
            self.__name = value
        else:
            print("Invalid name")  # Validation failed

    # Getter for 'age' property
    @property
    def age(self):
        return self.__age

    # Setter for 'age' property with validation
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:  # Check if value is a positive integer
            self.__age = value
        else:
            print("Invalid age")  # Validation failed


# ----------------- Example usage -----------------

# Creating a Person object
person = Person("John Wick", 50)

# Accessing values using the getter
print("Name:", person.name)
print("Age:", person.age)

# Trying to set an invalid name
person.name = ""  # Will print "Invalid name"

# Trying to set an invalid age
person.age = -5   # Will print "Invalid age"
