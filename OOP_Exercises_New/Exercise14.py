""" Polymorphism with a Function: Create a function describe_pet that takes an object of Animal and calls its speak method, demonstrating polymorphism. """

class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Parrot(Animal):
    def speak(self):
        print("Squawk!")

def describe_pet(animal):
    animal.speak()

dog = Dog()
cat = Cat()
parrot = Parrot()

describe_pet(dog)
describe_pet(cat)
describe_pet(parrot)


        