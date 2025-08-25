import sys


def is_armstrong_number(number):
    digits = [int(i) for i in str(number)]
    n = len(digits)

    return sum(digit**n for digit in digits) == number


def get_armstrong_numbers(starting):
    num = starting
    while True:
        num += 1
        if is_armstrong_number(num):
            yield num


if __name__ == "__main__":
    _, number = sys.argv
    armstrong_numbers = get_armstrong_numbers(int(number))
    print(next(armstrong_numbers))
