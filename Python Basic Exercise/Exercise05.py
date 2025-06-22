""" Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False. """

# Use list indexing.
# Get the first element of the list.
# Get the last element of the list.
# Compare these two elements using the equality operator (==).

def first_last_same(number_list):
    print("Given list: " , number_list)

    first_num = number_list[0]
    last_num = number_list[-1]

    if first_num == last_num :
        return True
    else:
        return False

number_x = [10,20,30,40,10]
print("result is :", first_last_same(number_x))

number_y = [10,20,30,40,50]
print("result is :", first_last_same(number_y))