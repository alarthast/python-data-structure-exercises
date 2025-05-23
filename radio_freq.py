# This program knows about the frequencies of various FM radio stations in
# London.
#
# Usage:
#
# $ python radio_freq.py [station_name]
#
# For instance:
#
# $ python radio_freq.py "Radio 4"
# You can listen to Radio 4 on 92.5 FM
#
# or:
#
# $ python radio_freq.py "BBC Radio 5"
# I don't know the frequency of BBC Radio 5

import argparse

fm_frequencies = {
    "89.1 MHz": "BBC Radio 2",
    "91.3 MHz": "BBC Radio 3",
    "93.5 MHz": "BBC Radio 4",
    "94.9 MHz": "BBC London",
    "95.8 MHz": "Capital FM",
    "97.3 MHz": "LBC",
    "98.8 MHz": "BBC Radio 1",
    "100.0 MHz": "Kiss FM",
    "100.9 MHz": "Classic FM",
    "105.4 MHz": "Magic",
    "105.8 MHz": "Virgin",
    "106.2 MHz": "Heart 106.2",
}

fm_stations = {v: k for k, v in fm_frequencies.items()}

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that if the radio station is not found, the user is
#   given a list of all stations that the program does know about.
# * Change the program so that if it is called without arguments, a table of
#   all radio stations and their frequencies is displayed.


def get_parser():
    parser = argparse.ArgumentParser(
        description="This program knows about the frequencies of various FM radio stations in London."
    )
    parser.add_argument(
        "station_name", nargs="?", default="", help="Name of the radio station"
    )
    return parser


def get_message(station_name):
    if not station_name:
        return "I know about {} FM radio stations".format(len(fm_frequencies))

    matched = {
        name: freq
        for name, freq in fm_stations.items()
        if station_name.lower() in name.lower()
    }

    if not matched:
        all_stations = ", ".join(fm_stations.keys())
        return f"I don't know the frequency of {station_name}.\nI know about:\n{all_stations}"

    return "\n".join(
        [
            f"You can listen to {name} on {freq.replace('MHz', 'FM')}"
            for name, freq in matched.items()
        ]
    )


def main():
    args = get_parser().parse_args()
    print(get_message(args.station_name))


if __name__ == "__main__":
    main()
