# Exercises from https://www.w3resource.com/python-exercises/generators-yield/index.php

# I'm avoiding itertools.permutations

# Recursive implementation (mine)
def get_permutations(list_, front=None):
    if len(list_) == 1:
        yield front + list_
    else:
        if front is None:
            front = []
            back = list_
        else:
            front = front + list_[:1]
            back = list_[1:]
        for j in range(len(back)):
            yield from get_permutations(back[j:] + back[:j], front)


# Sample solution
def list_permutations_old(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for p in list_permutations_old(elements[1:]):
            for i in range(len(elements)):
                yield p[:i] + elements[0:1] + p[i:]


# My solution rewritten by copilot (preserves order)
def list_permutations_rewritten(elements):
    if len(elements) == 1:
        yield elements
    else:
        for j in range(len(elements)):
            # Rotate the list so each element gets to be first
            rotated = elements[j:] + elements[:j]
            for p in list_permutations_rewritten(rotated[1:]):
                yield [rotated[0]] + p


# Another solution that copilot wrote (lexicographic order)
# Note: this is the same as the sample solution for exercise 11
def list_permutations(elements):
    if len(elements) == 1:
        yield elements
    else:
        for i in range(len(elements)):
            # Pick the i-th element, permute the rest, and prepend the picked element
            for p in list_permutations(elements[:i] + elements[i + 1 :]):
                yield [elements[i]] + p


def main():
    for ind, l_ in enumerate(list_permutations([1, 2, 3, 4])):
        print(ind, l_)


if __name__ == "__main__":
    main()
