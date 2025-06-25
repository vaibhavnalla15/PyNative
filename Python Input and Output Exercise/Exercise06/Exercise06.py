""" Write all content of a file into a new file by skipping line number 5 """
# Hints:-
# 1. Read all lines from the ‘test.txt’ file using the readlines() method.
# 2. This method returns all lines from a file as a list.
# 3. Open a new text file in write mode ('w').
# 4. Set counter = 0. Iterate through each line from the list.
# 5. If the counter is 4, skip that line; otherwise, write that line to the new text file using the write() method.
# 6. Increment counter by 1 in each iteration.

# TODO :- Create a test.txt file and add content to it.
# read test.txt
with open("test.txt", "r") as file:
    # read all lines from a file
    lines = file.readlines()

# open new file in write mode
with open("new_file.txt", "w") as file:
    count = 0
    # open new file in write mode
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            file.write(line)
        # in each iteration reduce the count
        count += 1

