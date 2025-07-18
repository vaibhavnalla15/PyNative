""" Rename key of a dictionary """
# Write a program to rename a key city to a location in the following dictionary.
# Hints:-
# 1. Remove the city from a given dictionary
# 2. Add a new key (location) into a dictionary with the same value

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)
