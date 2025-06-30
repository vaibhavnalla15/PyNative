""" Print list in reverse order using a loop """
# Hints:-
# Approach 1: Use the built-in function reversed() to reverse the list
#
# Approach 2: Use for loop and the len() function
# 1. Get the size of a list using the len(list1) function.
# 2. Use a for loop and reversed(range()) to iterate through index numbers in reverse order, starting from length-1 down to 0.
#    In each iteration, i will be reduced by 1.
# 3. In each iteration, print list items using list1[i]. i is the current value of the index.

print("Approach 1:- ")
list1 = [10, 20, 30, 40, 50]
reversed_list = reversed(list1)
for n in reversed_list:
    print(n)
print() # used for space in between

print("Approach 2:- ")
# get list size
# len(list1) -1: because index start with 0
# iterate list in reverse order
# start from last item to first
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])
