""" Append To a File """
# Modify the previous program to append the string “This is an appended line.” to the end of “output.txt”.
# Hints:-
# You need to open file in a different mode that allows you to add content to the end. Use a mode.

filename = "output.txt"
text_to_append = "This is an appended line."

try:
    with open("../Exercise07 (Write To a File)/output.txt", "a") as file:
        file.write("\n" + text_to_append) # Adding a newline character for better readability
    print(f"Successfully appended '{text_to_append}' to '{filename}'.")
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Explanation:
# with open(filename, 'a') as file: opens the file in append mode ('a'). If “output.txt” doesn’t exist, it will be created.
# If it does exist, new content will be added at the end.
# file.write("\n" + text_to_append) writes the string to the file.
