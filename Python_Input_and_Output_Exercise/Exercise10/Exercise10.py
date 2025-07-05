""" Read Line Number 4 from File """
with open("test.txt" , "r") as file:
    lines = file.readlines()
    print(lines[3])