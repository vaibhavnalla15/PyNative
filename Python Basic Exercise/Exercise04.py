""" Write a Python code to remove characters from a string from 0 to n and return a new string."""

def remove_chars(word, n):
    print("Original string: ", word)
    x = word[n:]
    return x

print("Removing characters from a string")

print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

