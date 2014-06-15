import unittest
import onesolver


class OneSolverTestFixture(unittest.TestCase):
    def test_find_sum_of_multiples_of_4_and_limit_10_should_be_12(self):
        first = onesolver.OneSolver()
        result = first.find_sum_of_multiples(10, [4])
        self.assertEqual(result, 12)

    def test_find_sum_of_multiples_of_3_5_and_limit_10_should_be_23(self):
        first = onesolver.OneSolver()
        result = first.find_sum_of_multiples(10, [3, 5])
        self.assertEqual(result, 23)

    def test_find_sum_of_multiples_of_3_5_and_limit_1000(self):
        first = onesolver.OneSolver()
        result = first.find_sum_of_multiples(1000, [3, 5])
        self.assertEqual(result, 233168)