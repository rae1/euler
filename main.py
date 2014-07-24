import eulersolver
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--problem', type=int, help='Number of problem to solve', default=1)
    args = parser.parse_args()

    problem_number = args.problem
    solver = eulersolver.EulerSolver()
    problem_result = solver.solve(problem_number)

    print('Result from problem {} is: {}'.format(problem_number, problem_result))


if __name__ == '__main__':
    main()
