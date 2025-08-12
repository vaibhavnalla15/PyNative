""" Design a class SeriesCalculator that calculates the sum of an arithmetic series. """


def calculate_sum(n, a=1, d=2):
    # Sum of the first n terms of an arithmetic series
    return n * (2 * a + (n - 1) * d) // 2


class SeriesCalculator:
    pass

# Test the calculator
sc = SeriesCalculator()
print("Sum of series:", calculate_sum(3))
