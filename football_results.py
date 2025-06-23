# This file contains a list of results from Group F of the Euro 2016
# championship.  Each item in the list of results is a dictionary, whose keys
# are the names of the teams playing a match, and whose values are the number
# of goals scored by each team in the match.
#
# When the file is run, it should display some facts about the final results in
# the group.
#
# NB Teams score three points for a win and one point for a draw.
from collections import Counter

RESULTS = [
    {"Austria": 0, "Hungary": 2},
    {"Portugal": 1, "Iceland": 1},
    {"Iceland": 1, "Hungary": 1},
    {"Portugal": 0, "Austria": 0},
    {"Iceland": 2, "Austria": 1},
    {"Hungary": 3, "Portugal": 3},
]

POINTS = {"W": 3, "D": 1, "L": 0}

TOTAL_GOALS = Counter()
HISTORY = Counter()
for match in RESULTS:
    TOTAL_GOALS.update(match)
    if len(set(match.values())) == 1:  # draw
        HISTORY.update([f"{team}_D" for team in match])
    else:
        (loser, winner) = sorted(match.keys(), key=match.get)
        HISTORY.update([f"{loser}_L", f"{winner}_W"])

TOTAL_POINTS = Counter()
for key, count in HISTORY.items():
    team, wdl = key.split("_")
    TOTAL_POINTS.update({team: POINTS.get(wdl) * count})


def format(match: dict):  # Convert an entry into a human readable string
    return " vs ".join(match.keys())


def get_key_for_extremum_including_ties(d: dict, func: callable):
    return ", ".join([k for k, v in d.items() if v == func(d.values())])


def main():
    # TODO: Write code to answer the following questions:
    print("There were {} matches in the group".format(len(RESULTS)))

    print(
        "The match with the most goals was",
        format(max(RESULTS, key=lambda match: sum(match.values()))),
    )
    print(
        "The match with the fewest goals was",
        format(min(RESULTS, key=lambda match: sum(match.values()))),
    )
    print(
        "The team(s) with the most total goals was",
        get_key_for_extremum_including_ties(TOTAL_GOALS, max),
    )
    print(
        "The team(s) with the fewest total goals was",
        get_key_for_extremum_including_ties(TOTAL_GOALS, min),
    )
    print(
        "The team(s) with the most points was",
        get_key_for_extremum_including_ties(TOTAL_POINTS, max),
    )
    print(
        "The team(s) with the fewest points was",
        get_key_for_extremum_including_ties(TOTAL_POINTS, min),
    )

    # TODO (extra): Write code to compute and display a league table
    print("-" * 25)
    print(f"{'Team':<10}|G |W |D |L |P")
    print("-" * 25)

    for team in TOTAL_GOALS.keys():
        print(
            f"{team:<10}|{TOTAL_GOALS[team]:<2}|{HISTORY.get(f'{team}_W',0):<2}|{HISTORY.get(f'{team}_D',0):<2}|{HISTORY.get(f'{team}_L',0):<2}|{TOTAL_POINTS[team]:<2}"
        )


if __name__ == "__main__":
    main()
