""" Inheritance - Animal Kingdom: Create a base class Animal with a method speak(). Derive two classes Dog and Cat from Animal and override the speak method to reflect their sounds. """

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")


dog = Dog()
cat = Cat()
dog.speak()
cat.speak()
        