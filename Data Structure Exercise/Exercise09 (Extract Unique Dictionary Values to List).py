""" Extract Unique Dictionary Values to List """
# Write a code to get all values from the dictionary and add them to a list but don’t add duplicates.

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

print("Dictionary's values:-", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    if val not in speed_list:
        speed_list.append(val)

print("Unique list:-", speed_list)
