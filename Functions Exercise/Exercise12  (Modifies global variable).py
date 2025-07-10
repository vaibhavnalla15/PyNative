""" Modifies global variable """
# Define a global variable global_var = 10. Write a function that modifies a global variable value.
# Hints:- Use global keyword to create and modify the global variable value

global_var = 10

def modify_global_var():
   global global_var
   global_var = 20
   print("Inside function:-", global_var)

modify_global_var()
print("Outside Function:-", global_var)
