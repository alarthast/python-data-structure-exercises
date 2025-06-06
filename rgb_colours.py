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

COLOURS_TO_CODES = {colour.lower(): code.lower() for colour, code in COLOURS}
CODES_TO_COLOURS = {v: k for k, v in COLOURS_TO_CODES.items()}

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


def is_rgb_code(text):
    if len(text) == 3:
        try:
            int(text, 16)  # A rgb code should be convertible to hexadecimal
            return True
        except ValueError:
            pass
    return False


def get_message(user_input):
    user_input = user_input.lower()  # Convert at boundary

    code = COLOURS_TO_CODES.get(user_input)
    if code:
        return f"The RGB code for {user_input} is {code.upper()}"

    colour = CODES_TO_COLOURS.get(user_input)
    if colour:
        return f"The colour for {user_input.upper()} is {colour}"

    if is_rgb_code(user_input):
        return f"I don't know the colour for {user_input.upper()}"
    else:
        return f"I don't know the RGB code for {user_input}"


def main():
    args = get_parser().parse_args()
    message = get_message(args.input)
    print(message)


if __name__ == "__main__":
    main()
