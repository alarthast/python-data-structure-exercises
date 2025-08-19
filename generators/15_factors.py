# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php
import sys


def get_factors(number):
    for num in range(1, number + 1):
        if number % num == 0:
            yield num


if __name__ == "__main__":
    _, number = sys.argv
    for num in get_factors(int(number)):
        print(num)
