# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php
import sys


def is_happy(number):
    num = number
    seen = set()
    while True:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
        if num in seen:
            return False
        if num == 1:
            return True


def get_happy_numbers(starting):
    num = starting
    while True:
        num += 1
        if is_happy(num):
            yield num


if __name__ == "__main__":
    _, number = sys.argv
    happy_numbers = get_happy_numbers(int(number))
    print(next(happy_numbers))
