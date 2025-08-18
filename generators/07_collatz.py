# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php


def get_collatz(number):
    yield number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        yield number


if __name__ == "__main__":
    for number in [1, 2, 12, 19]:
        print(
            f"Number:{number}; Sequence:",
            ",".join([str(i) for i in get_collatz(number)]),
        )
