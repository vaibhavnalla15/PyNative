""" Sort a list of numbers """
# Sort a given list of numbers in ascending order and print it.
# Hints:- Python lists have a built-in method sort() to sort elements in-place, and there’s also a built-in function sorted() that returns
# a new sorted list without modifying the original.

numbers = [5, 2, 8, 1, 9]
# Resetting for demonstration of sorted()

print("Original list for sorted() demonstration:", numbers)
# Method 1: Using the sort() method (sorts in-place)
numbers.sort()
print("Sorted list (in-place using .sort()):", numbers)
print()

# Method 2: Using the sorted() function (returns a new sorted list)
numbers = [5, 2, 8, 1, 9]
print("Original List:-", numbers)
print("Sorted List:-", sorted(numbers))
