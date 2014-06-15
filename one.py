
class One():
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

        print('Finding the sum of a bunch of multiples!')

        total_sum = sum(self.__find_all_divisible_in_range(limit, numbers))
        return total_sum

    def __find_all_divisible_in_range(self, limit, numbers):
        for current in range(1, limit):
            divisible = map(lambda number: current % number == 0, numbers)
            if any(divisible):
                print(current, end=' ')
                yield current