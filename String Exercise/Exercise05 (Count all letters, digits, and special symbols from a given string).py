""" Count all letters, digits, and special symbols from a given string """
# Hints:-
# Use the following string functions:-
# 1. isalpha(): To check if a string/character is an alphabet
# 2. isdigit(): To check if a string/character is a digit.
# 3. Iterate each character from a string using a for loop
# 4. In each loop iteration, check if the current character is the alphabet using an isalpha() function.
# 5. If yes, increase the character counter. Check if it is a digit using the isdigit() function and increase the digit counter; otherwise,
#    increase the symbol counter.
# 6. Print the value of each counter

def find_digits_chars_symbols(str1):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in str1:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    print(f"Chars= {char_count}, Digits= {digit_count}, Symbol= {symbol_count}")

sample_str = "P@yn2at&#i5ve"
print("Total counts of Chars, Digits, and Symbols \n")
find_digits_chars_symbols(sample_str)