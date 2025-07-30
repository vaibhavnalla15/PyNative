""" Check object is a subclass of a particular class """

# Write a code to check the following
# Dog is a subclass of Animal? –> True
# Animal is a subclass of Dog? –> False
# Cat is a subclass of Animal? –> False
# Puppy is a subclass of Animal –> True

# Use the issubclass() function. The issubclass(potential_subclass, potential_superclass) returns True if the first argument is a subclass (or the same class) of the second argument, and False otherwise.

class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print(issubclass(Dog, Animal))      # returns True
print(issubclass(Animal, Dog))      # returns False
print(issubclass(Cat, Animal))      # returns False
print(issubclass(Puppy, Animal))    # returns True

