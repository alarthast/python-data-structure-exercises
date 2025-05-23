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

_FM_FREQUENCIES = {
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

FM_STATIONS = {v: k.replace("MHz", "FM") for k, v in _FM_FREQUENCIES.items()}

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


def get_table():
    def wrap(left, right, width):
        return "|" + left.ljust(width) + "|" + right.ljust(width) + "|"

    header_texts = ["Station Name", "Frequency"]
    width = max(len(item) for item in header_texts + list(FM_STATIONS.keys())) + 1
    border = "|" + 2 * ("-" * width + "|")
    header = wrap(header_texts[0], header_texts[1], width)
    contents = [wrap(name, freq, width) for name, freq in FM_STATIONS.items()]
    return "\n".join([border, header, border, *contents, border])


def get_message(station_name):
    if not station_name:
        return f"I know about {len(FM_STATIONS)} FM radio stations:\n{get_table()}"

    matched = {
        name: freq
        for name, freq in FM_STATIONS.items()
        if station_name.lower() in name.lower()
    }

    if not matched:
        all_stations = ", ".join(sorted(FM_STATIONS.keys()))
        return f"I don't know the frequency of {station_name}.\nI know about:\n{all_stations}"

    return "\n".join(
        [f"You can listen to {name} on {freq}" for name, freq in matched.items()]
    )


def main():
    args = get_parser().parse_args()
    print(get_message(args.station_name))


if __name__ == "__main__":
    main()
