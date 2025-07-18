""" Print the value of key ‘history’ from nested dict """
# Hints:- It is a nested dict. Use the correct chaining of keys to locate the specified key-value pair.

sampleDict = {
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

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

history_value = sampleDict["class"]["student"]["marks"]["history"]
print("Marks Obtained in History:-", history_value)
# or

print(sampleDict["class"]["student"]["marks"]["history"])