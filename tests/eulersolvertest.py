import unittest
import eulersolver


class EulerSolverTestCase(unittest.TestCase):
    def test_solves_problem_one(self):
        solver = eulersolver.EulerSolver()

        result = solver.solve_problem_one()

        self.assertEqual(result, 233168)

    def test_find_sum_of_multiples_of_4_and_limit_10_should_be_12(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_sum_of_multiples(10, [4])

        self.assertEqual(result, 12)

    def test_find_sum_of_multiples_of_3_5_and_limit_10_should_be_23(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_sum_of_multiples(10, [3, 5])

        self.assertEqual(result, 23)

    def test_find_all_fibonacci_terms_less_than_1_should_be_1(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_all_fibonacci_terms_less_than(1)

        self.assertEqual(list(result), [1])

    def test_find_all_fibonacci_terms_less_than_3_should_be_1_2(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_all_fibonacci_terms_less_than(3)

        self.assertEqual(list(result), [1, 2])

    def test_find_all_fibonacci_terms_less_than_10_should_be_1_2_3_5_8(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_all_fibonacci_terms_less_than(10)

        self.assertEqual(list(result), [1, 2, 3, 5, 8])

    def test_find_all_even_fibonacci_terms_less_than_10_should_be_2_8(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_all_fibonacci_terms_less_than(10, lambda term: term % 2 == 0)

        self.assertEqual(list(result), [2, 8])

    def test_find_all_fibonacci_terms_less_than_400000000_should_not_take_long(self):
        solver = eulersolver.EulerSolver()

        result = solver.find_all_fibonacci_terms_less_than(400000000)

        print(list(result))
