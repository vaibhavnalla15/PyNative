""" Calculating Student Results: Develop a class to accept a student's name and marks in three subjects, then calculate and display the total and average marks. """

class Students:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def total(self):
        return sum(self.marks)
    
    def average(self):
        return self.total() / len(self.marks)
    
    def display(self):
        print(f"Student: {self.name}")
        print(f"Total Marks: {self.total()}")
        print(f"Average Marks: {self.average()}")

student1 = Students("John", [65,64,84])
student1.display()
        
        
        
        