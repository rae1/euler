import eulersolver


def main():
    solver = eulersolver.EulerSolver()
    result = solver.solve(2)

    print('Result from problem one is {}'.format(result))


if __name__ == '__main__':
    main()
