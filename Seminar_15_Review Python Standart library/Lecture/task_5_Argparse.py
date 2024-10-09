import argparse


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parses = argparse.ArgumentParser(description='My first argument parses')

    parses.add_argument('param', metavar='a b c', type=float, nargs=3,
                        help='enter  a b c separated by a space')
    args = parses.parse_args()
    print(quadratic_equations(*args.param))
