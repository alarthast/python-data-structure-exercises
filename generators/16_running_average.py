import sys


def get_running_average(numbers):
    running_sum = 0
    for ind, num in enumerate(numbers, start=1):
        running_sum += num
        yield running_sum / ind


if __name__ == "__main__":
    numbers = [int(num) for num in sys.argv[1:]]
    for num in get_running_average(numbers):
        print(num)
