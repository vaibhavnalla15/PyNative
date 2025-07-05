""" Display Right-Aligned Output """
# Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.
# Hints:- Use f-strings with the > alignment specifier and a width for the word. Then, simply print the number after it.

word = input("Enter a word:- ")
num = int(input("Enter a number:- "))

print(f"{word:>20}{num}") # :> is used to width or to align right.
