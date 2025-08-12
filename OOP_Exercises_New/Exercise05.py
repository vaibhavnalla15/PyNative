""" Create a class MaxFinder that identifies the largest number in a list. """
class MaxFinder:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        if not self.numbers:
            return "List is empty"
        return max(self.numbers)

# Example
finder = MaxFinder([1, 3, 2, 5, 4])
print("The largest number is:", finder.find_max())