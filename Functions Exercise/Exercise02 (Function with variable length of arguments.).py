""" Create a function with variable length of arguments """
# Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values
# Note: Create this function so that it can receive any number of arguments, process them, and display the value of each individual argument.
#  Hints:-
# 1. To accept a variable number of positional arguments, allowing functions to take any quantity of these arguments, we use *args as a parameter.
# (This involves prefixing a parameter name with an asterisk: *).
# 2. Using *args, you can pass any number of positional arguments to the function.
# Internally, all these passed values are collected and represented as a tuple.

def func1(*args):
    for args in args:
        print(args)

# Example calls to the function with different numbers of arguments:-
func1(10,20,)
func1("hello", 3.14, True)
func1("hello world", 15 , 20)
func1("Hi my Name is Vaibhav Nalla", "DOB:- 15/02/2002")