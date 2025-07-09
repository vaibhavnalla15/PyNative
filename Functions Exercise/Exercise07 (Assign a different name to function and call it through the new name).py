""" Assign a different name to function and call it through the new name """
# Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.
# Hints:-
# Assign a different name to function using the assignment (=) operator. To assign a different name to an existing function and then call it
# using this new name, you can simply assign the function object to a new variable.
# fun_name = new_name

def display_student(name, age):
    print(name, age)

# call using original name
display_student("John", 60)

# assign new name
show_student = display_student
# call using new name
show_student("Wick", 60)


