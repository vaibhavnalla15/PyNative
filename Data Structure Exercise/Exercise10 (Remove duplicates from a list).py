""" Remove duplicates from a list """
# Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Original list:-", sample_list)

sample_list = list(set(sample_list))    # Set data structure is used to extract unique values
print("Unique List:-", sample_list)

t = tuple(sample_list)
print("Tuple:-", t)

print("Maximum number is:-", max(t))
print("Minimum number is:-", min(t))