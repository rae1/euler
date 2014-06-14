def find_sum_of_multiples(limit, numbers):
    """
    Multiples of 3 and 5
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    print('Finding the sum of a bunch of multiples!')

    sumofmultiples = sum(find_all_divisible_in_range(limit, numbers))
    print()
    print(sumofmultiples)
    return sumofmultiples


def find_all_divisible_in_range(limit, numbers):
    for current in range(1, limit):
        divisible = map(lambda number: current % number == 0, numbers)
        if any(divisible):
            print(current, end=' ')
            yield current