# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php
import sys

# You can tell I am not a mathematician cos I misunderstood the question
# The solution is similar to exercise 3 except for another conditional so I won't reimplement


def get_prime_factors(number):
    num = 2
    while True:
        if number == num:
            yield num
            break
        if number % num != 0:
            num += 1
            continue
        yield num
        number = number // num


if __name__ == "__main__":
    _, number = sys.argv
    for num in get_prime_factors(int(number)):
        print(num)
