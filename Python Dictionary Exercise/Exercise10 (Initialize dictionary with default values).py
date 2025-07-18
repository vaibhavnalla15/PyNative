""" Initialize dictionary with default values """
# In Python, we can initialize the keys with the same values.
# Hints:- Use the fromkeys() method of dict.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict = dict.fromkeys(employees, defaults)
print(new_dict)

# Individual data
print(new_dict["Kelly"])

