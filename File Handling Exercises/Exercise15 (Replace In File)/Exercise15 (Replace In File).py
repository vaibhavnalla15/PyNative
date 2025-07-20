""" Replace In File """
# Write a program that reads a text file, replaces all occurrences of a specific word with another word, and writes the modified content to a new file.
# Hints:-
# First, read the entire content of the source file.
# Next, use string replace() method to replace all occurrences of the old word with the new word.
# Finally, open a new file in write mode and write the modified content to it.

def replace_in_file(source_filename, destination_filename, old_word, new_word):
    try:
        with open(source_filename, "r") as source_file:
            content = source_file.read()
        modified_content = content.replace(old_word, new_word)
        with open(destination_filename, "w") as destination_file:
            destination_file.write(modified_content)
        return f"Successfully replaced '{old_word}' with '{new_word}' in '{source_filename}' and saved to '{destination_filename}'."
    except FileNotFoundError:
        return f"Error: Source file '{source_filename}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
source_file = "sample.txt"
destination_file = "replaced_file.txt"
word_to_replace = "Whiskers"
replacement_word = "Smokey"

print(replace_in_file(source_file, destination_file, word_to_replace, replacement_word))
