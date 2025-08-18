# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php
import sys


def get_palindrome_number(starting):
    n = starting + 1
    while True:
        if n == int(str(n)[::-1]):
            yield n
        n += 1


if __name__ == "__main__":
    _, starting = sys.argv
    palindrome_numbers = get_palindrome_number(int(starting))
    print(next(palindrome_numbers))
