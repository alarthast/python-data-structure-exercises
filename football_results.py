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


TOTAL_GOALS = {}
TOTAL_POINTS = {}
for match in RESULTS:
    for team, goals in match.items():
        TOTAL_GOALS[team] = TOTAL_GOALS.get(team, 0) + goals
    for team, wdl in get_win_draw_or_lose(match).items():
        TOTAL_POINTS[team] = TOTAL_POINTS.get(team, 0) + POINTS[wdl]
print("There were {} matches in the group".format(len(RESULTS)))


# TODO: Write code to answer the following questions:
def format(match: dict):  # Convert an entry into a human readable string
    return " vs ".join(match.keys())


def get_key_for_extremum_including_ties(d: dict, func: callable):
    val = func(d.values())
    return ", ".join([k for k, v in d.items() if v == val])


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
