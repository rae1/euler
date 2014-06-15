import eulersolver


def main():
    solver = eulersolver.EulerSolver()
    result = solver.solve(1)

    print('Result from problem one is {}'.format(result))


if __name__ == '__main__':
    main()
