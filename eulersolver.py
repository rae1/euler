class EulerSolver():
    """
    Multiples of 3 and 5
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    def __init__(self):
        pass

    def solve(self):
        return self.find_sum_of_multiples(1000, [3, 5])

    def find_sum_of_multiples(self, limit, numbers):
        total_sum = sum(self.find_all_divisible_in_range(limit, numbers))
        return total_sum

    def find_all_divisible_in_range(self, limit, numbers):
        def is_multiple_of(numerator):
            return lambda denominator: numerator % denominator == 0

        for current in range(1, limit):
            multiple = map(is_multiple_of(current), numbers)
            if any(multiple):
                yield current