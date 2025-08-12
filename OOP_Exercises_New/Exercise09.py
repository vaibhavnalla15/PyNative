""" Last Digit in Words: Write a class with a method that takes an integer and prints the last digit of that number in words. """

class NumberInWords:
    def last_digit_in_words(self, number):
        last_digit = number % 10 
        words =  ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return words[last_digit]
    

new = NumberInWords() 
print(new.last_digit_in_words(1865489423156))
            