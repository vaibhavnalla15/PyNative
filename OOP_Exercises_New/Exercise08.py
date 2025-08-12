""" Student Grade Calculator: Implement a Student class with attributes for name and a list of marks. Include a method to calculate the average and determine the grade. """

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        average = self.average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

student = Student("Alice", [92, 88, 91])
print(f"{student.name} Grade: {student.grade()}")
            

        
        
        
        