# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php

# The sample solution is more declarative.


def get_fibonacci_numbers():
    yield 0
    yield 1
    previous_two_numbers = [0, 1]
    while True:
        a, b = previous_two_numbers
        current = a + b
        yield current
        previous_two_numbers = [b, current]


def main():
    fibonacci = get_fibonacci_numbers()
    for _ in range(10):
        num = next(fibonacci)
        print(num)


if __name__ == "__main__":
    main()
