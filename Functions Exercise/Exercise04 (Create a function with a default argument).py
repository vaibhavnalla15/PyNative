""" Create a function with a default argument """
# Write a program to create a function show_employee() with the following specifications:
# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000.

# Hints:- Default arguments in Python will assume their default value during a function call if no corresponding argument is explicitly provided.
# You can assign a default value to a function parameter in the function definition using the assignment operator (=).

def show_employee(name, salary=9000):
    print("Name:", name, "Salary:", salary)

show_employee("James", 12000000)
show_employee("Bond")
