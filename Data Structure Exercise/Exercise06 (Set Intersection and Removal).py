""" Set Intersection(common) and Removal """
# Write a code to find the intersection (common) of two sets and remove those elements from the first set and second set.
# Hints:- Use the intersection() and remove() method of a set
# 1. Get the common items using the first_set.intersection(second_set)
# 2. Next, iterate common items using a for loop
# 3. In each iteration, use the remove() method of on first set and pass the current item to it.

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set:-", first_set)
print("Second Set:-", second_set)

common_items = first_set.intersection(second_set)
print("Common items are:-", common_items)
for item in common_items:
    first_set.remove(item)
    second_set.remove(item)

print("First Set after removing common element:-", first_set)
print("Second Set after removing common element:-", second_set)
