""" Reverse a given string """
# Hints:-
# 1. Use negative slicing
# 2. Or use the built-in function reversed().

str1 = "PYnative"

# Solution 1
print(str1[::-1])

# Solution 2
reversed_string = "".join(reversed(str1))
print(reversed_string)
