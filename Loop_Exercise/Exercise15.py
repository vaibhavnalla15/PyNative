""" Print elements from a given list present at odd index positions """
# Hints:-
# 1. Use list slicing.
# 2. List slicing in Python is a powerful way to extract a portion (a sublist) of a list based on a specified range of indices.
# 3. It allows you to create new lists containing elements from a specific starting point up to (but not including) a specific ending point
#    in the original list.

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")