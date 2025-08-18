# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php

# My solution is trying to get combinations of all possible lengths
def index(iterable, inds):
    return [iterable[i] for i in inds]


def get_combinations(list_, seen):
    num_elements = len(list_)
    if num_elements > 2:
        for pos in range(num_elements):
            # exclude the element at pos
            inds = [j for j in range(num_elements) if j != pos]
            yield from get_combinations(index(list_, inds), seen)
    if tuple(list_) not in seen:
        seen.add(tuple(list_))
        yield list_


# Sample solution with added print statements - combinations are of fixed length.
def list_combinations(elements, r):
    if r == 0:
        yield []
    elif r > len(elements):
        print(
            f"Returning - r={r} is greater than the number of elements {len(elements)}"
        )
        return
    else:
        for i in range(len(elements)):
            current_element = elements[i]
            remaining_elements = elements[i + 1 :]
            print(
                f"Current: {current_element}, Remaining: {remaining_elements}, r: {r}, listing combinations of {r-1}"
            )
            for combination in list_combinations(remaining_elements, r - 1):
                print(f"Yielding: {current_element} + {combination}")
                yield [current_element] + combination


# Solution written by copilot
def get_combinations_copilot(list_):
    # Generates all combinations of all possible lengths (from 1 to len(list_))
    def generate_combinations_recursive(current, start, length):
        # If the current combination has reached the desired length, yield a copy
        if len(current) == length:
            yield current[:]
            return
        # Iterate through the list, starting from 'start' index
        for i in range(start, len(list_)):
            current.append(list_[i])  # Add element to current combination
            # Recursively build combinations with the next elements
            yield from generate_combinations_recursive(current, i + 1, length)
            current.pop()  # Remove last element to backtrack

    num_elements = len(list_)
    # Generate combinations for all lengths from 1 to num_elements
    for r in range(1, num_elements + 1):
        yield from generate_combinations_recursive([], 0, r)


if __name__ == "__main__":
    seen = set()
    for comb in get_combinations([1, 2, 3, 4, 5], seen):
        print(comb)
