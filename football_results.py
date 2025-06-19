# This file contains a list of results from Group F of the Euro 2016
# championship.  Each item in the list of results is a dictionary, whose keys
# are the names of the teams playing a match, and whose values are the number
# of goals scored by each team in the match.
#
# When the file is run, it should display some facts about the final results in
# the group.
#
# NB Teams score three points for a win and one point for a draw.

RESULTS = [
    {"Austria": 0, "Hungary": 2},
    {"Portugal": 1, "Iceland": 1},
    {"Iceland": 1, "Hungary": 1},
    {"Portugal": 0, "Austria": 0},
    {"Iceland": 2, "Austria": 1},
    {"Hungary": 3, "Portugal": 3},
]

POINTS = {"W": 3, "D": 1, "L": 0}


def get_win_draw_or_lose(match: dict):
    if len(set(match.values())) == 1:  # draw
        return {team: "D" for team in match}
    (loser, winner) = sorted(match.keys(), key=match.get)
    return {loser: "L", winner: "W"}


def get_total_points(history: dict):
    return sum(POINTS.get(key) * value for key, value in history.items())


TOTAL_GOALS = {}
HISTORY = {}
for match in RESULTS:
    for team, goals in match.items():
        TOTAL_GOALS[team] = TOTAL_GOALS.get(team, 0) + goals
    for team, wdl in get_win_draw_or_lose(match).items():
        hist = HISTORY.get(team, {})
        hist[wdl] = hist.get(wdl, 0) + 1
        HISTORY[team] = hist

TOTAL_POINTS = {team: get_total_points(wdl) for team, wdl in HISTORY.items()}


# TODO: Write code to answer the following questions:
def format(match: dict):  # Convert an entry into a human readable string
    return " vs ".join(match.keys())


def get_key_for_extremum_including_ties(d: dict, func: callable):
    val = func(d.values())
    return ", ".join([k for k, v in d.items() if v == val])


def main():
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

    for team in HISTORY.keys():
        goals = TOTAL_GOALS[team]
        history = HISTORY[team]
        points = TOTAL_POINTS[team]
        print(
            f"{team:<10}|{goals:<2}|{history.get('W',0):<2}|{history.get('D',0):<2}|{history.get('L',0):<2}|{points:<2}"
        )


if __name__ == "__main__":
    main()
