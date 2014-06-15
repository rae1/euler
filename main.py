import eulersolver


def main():
    first = eulersolver.EulerSolver()
    result = first.solve()

    print('Result from problem one is {}'.format(result))


if __name__ == '__main__':
    main()
