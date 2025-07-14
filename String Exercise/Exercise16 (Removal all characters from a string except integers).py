""" Removal all characters from a string except integers """
# Hints:- Use the string function isdigit()

str1 = 'I am 25 years and 10 months old'

# Using list comprehension + join() + isdigit()
result = "".join([item for item in str1 if item.isdigit()])

print(result)