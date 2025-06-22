""" Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list
and even numbers from the second list. """

# 1. Create an empty list to store the result.
# 2. Iterate through the first list using a for loop; if a number is odd (check using num % 2 != 0 formula), append it to the new list.
# 3. Next, iterate through the second list; if a number is even (remainder when divided by 2 is 0), append it to the new list.
# Finally, return the newly created list.

new_list = []
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

for i in list1:
    if i % 2 != 0:
        new_list.append(i)

for j in list2:
    if j % 2 == 0:
        new_list.append(j)

print(new_list)

# Using Function:-

def merge_list(list1, list2):
    result_list = []
    for num in list1:
        if num % 2 != 0:    # check if current number is odd
            result_list.append(num)     # add odd number to result list

    for num in list2:
        if num % 2 == 0:    # check if current number is even
            result_list.append(num)     # add even number to result list
    return result_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print("Result list is:- ", merge_list(list1,list2))

