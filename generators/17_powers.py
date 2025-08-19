import sys


def get_powers(number, exponent):
    for exp in range(1, exponent + 1):
        yield number**exp


if __name__ == "__main__":
    _, number, exponent = sys.argv
    for num in get_powers(int(number), int(exponent)):
        print(num)
