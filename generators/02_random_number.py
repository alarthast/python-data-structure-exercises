# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php

# See the sample solution that uses `while True`, which seems better.

import sys
import random


def get_random_numbers(lower, upper, num_to_generate):
    yield from (random.randint(lower, upper) for _ in range(num_to_generate))


def main(lower, upper, num_to_generate=10):
    for num in get_random_numbers(lower, upper, num_to_generate):
        print(num)


if __name__ == "__main__":
    _, lower, upper = sys.argv
    main(int(lower), int(upper))
