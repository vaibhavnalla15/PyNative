""" Modify Nested Dictionary """
# In the below dictionary, change name to ‘Jessa’.
# Hints:- Use chained square bracket notation to reach the specific value you want to modify, then assign a new value to it.

nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


print(f"Nested dictionary: {nested_student_dict}")
nested_student_dict['class']['student']['name'] = 'Jessa'

print(f"Dict after modification: {nested_student_dict}")