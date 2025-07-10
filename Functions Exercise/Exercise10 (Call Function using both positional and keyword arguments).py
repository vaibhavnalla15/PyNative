""" Call Function using both positional and keyword arguments """
# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function using
# both positional and keyword arguments.

# Hints:-
# Call the function twice: once by just giving the values in order, and once by saying animal_type= and pet_name=

def describe_pet(animal_type, pet_name):
    return animal_type, pet_name

print(describe_pet("Dog", "Puppy"))

print(describe_pet(pet_name="Tom", animal_type="Cat"))