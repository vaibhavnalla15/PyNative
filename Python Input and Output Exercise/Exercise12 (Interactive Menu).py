""" Interactive Menu """
# Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”.
# Based on the user’s input, perform the corresponding action
# Hints:-
# Use a while loop to keep the menu running until the user chooses to exit.
# Use input() to get the user’s choice and if-elif-else statements to perform the corresponding action.

# Simple Code:-
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Calculate Square")
    print("3. Exit")

    choice = input("Enter your choice (1-3):- ")
    if choice == "1":
        print("Hello Vaibhav!!!")
        break

    elif choice == "2":
        print("Calculating Square")
        number = int(input("Enter your number:- "))
        square = number ** 2
        print(f"The square of {number} is {square}")
        break

    elif choice == "3":
        print("Exiting...Bye!!!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

# Using Error Handling:-
while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Calculate Square")
    print("3. Exit")

    choice = input("Enter your choice (1-3):- ")
    if choice == "1":
        print("Hello Vaibhav!!!")
        break

    elif choice == "2":
        try:
            print("Calculating Square")
            number = int(input("Enter your number:- "))
            square = number ** 2
            print(f"The square of {number} is {square}")
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    elif choice == "3":
        print("Exiting...Bye!!!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
