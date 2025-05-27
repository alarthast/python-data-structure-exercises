# This program knows about the RGB code corresponding to common colours.
#
# Usage:
#
# $ python rgb_colours.py [colour]
#
# For instance:
#
# $ python rgb_colours.py red
# The RGB code for red is F00
#
# or:
#
# $ python rgb_colours.py "burnt sienna"
# I don't know the RGB code for burnt sienna
import argparse

COLOURS = [
    ["red", "F00"],
    ["yellow", "FF0"],
    ["green", "0F0"],
    ["cyan", "0FF"],
    ["blue", "00F"],
    ["magenta", "F0F"],
]


# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that users can also enter an RGB colour code, and be
#   told the name of the corresponding colour.
# * Change the program so that it ignores the case of the user's input.


def get_parser():
    parser = argparse.ArgumentParser(
        description="This program knows about the RGB code corresponding to common colours."
    )
    parser.add_argument(
        "input",
        type=str,
        help="Colour for which the RGB code is requested, or vice versa",
    )
    return parser


def get_message(user_input):
    for colour, code in COLOURS:
        if colour == user_input:
            return f"The RGB code for {user_input} is {code}"
        elif code == user_input:
            return f"The colour for {user_input} is {colour}"
    try:
        int(user_input, 16)  # Would not error if a RGB code is provided
        return f"I don't know the colour for {user_input}"
    except ValueError:  # Assume a colour is provided
        return f"I don't know the RGB code for {user_input}"


def main():
    args = get_parser().parse_args()
    message = get_message(args.input)
    print(message)


if __name__ == "__main__":
    main()
