""" Check File is Empty or Not """
# Hits:- Use os.stat('file_name').st_size() function to get the file size. if it is 0 then the file is empty.
import os

size = os.stat("test.txt").st_size
if size == 0:
    print("File is Empty")
else:
    print("File is not Empty")