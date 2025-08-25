# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php

# I think the sample solution is for the first n numbers instead of for a range,
# but it's still useful

import sys


def is_prime(number):
    # The square root should have been used here
    for int_ in range(2, number):
        if number % int_ == 0:
            return False
    return True


def get_primes(lower, upper):
    for num in range(lower, upper + 1):
        if is_prime(num):
            yield num


def main(lower, upper):
    for num in get_primes(lower, upper):
        print(num)


if __name__ == "__main__":
    _, lower, upper = sys.argv
    main(int(lower), int(upper))
