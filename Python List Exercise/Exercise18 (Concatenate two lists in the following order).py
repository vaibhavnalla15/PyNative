""" Concatenate two lists in the following order """
# Given :-
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir
# Expected Output:- ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# Hints:- Use a list comprehension to iterate two lists using a for loop and concatenate the current item of each list.

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]
print(result)