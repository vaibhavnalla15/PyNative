""" Composition Over Inheritance: Create a Book class with a Author class included within it, demonstrating composition over inheritance."""

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = Author(author)

    def display(self):
        print(f"Book: {self.title}, Author: {self.author.name}")

book = Book("Think & Grow Rich", "Napoleon Hill") 
book.display()
        
        