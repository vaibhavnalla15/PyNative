"""Write a Python code to accept a string from the user and display characters present at an even index number."""

string = input("Enter your string:- ")
print(f"Original String is {string}")

size = len(string)

print("Printing only even index chars")
for i in range(0, size -1, 2):
    print("index[",i,"]", string[i])

"""==================================================== or ===================================================="""

word = input("Enter your string:- ")
print(f"Original String is {word}")

x = list(word)
for i in x[0::2]:
    print(i)



