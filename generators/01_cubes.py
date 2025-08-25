# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php

import sys


def get_cubes(n):
    for num in range(1, n + 1):
        yield num**3


def main(n):
    for cube in get_cubes(n):
        print(cube)


if __name__ == "__main__":
    _, n = sys.argv
    main(int(n))
