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

TOTAL_GOALS = {}
for match in RESULTS:
    for team, goals in match.items():
        try:
            TOTAL_GOALS[team] += goals
        except KeyError:
            TOTAL_GOALS[team] = goals

print("There were {} matches in the group".format(len(RESULTS)))


# TODO: Write code to answer the following questions:
def format(match):  # Convert an entry into a human readable string
    return " vs ".join(match.keys())


print(
    "The match with the most goals was",
    format(max(RESULTS, key=lambda match: sum(match.values()))),
)
print(
    "The match with the fewest goals was",
    format(min(RESULTS, key=lambda match: sum(match.values()))),
)
print("The team with the most total goals was", max(TOTAL_GOALS, key=TOTAL_GOALS.get))
print("The team with the fewest total goals was", min(TOTAL_GOALS, key=TOTAL_GOALS.get))
print("The team with the most points was", "?")
print("The team with the fewest points was", "?")

# TODO (extra): Write code to compute and display a league table
