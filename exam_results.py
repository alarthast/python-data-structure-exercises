# This program interactively asks about your exam marks, and reports the
# corresponding grades.
#
# Usage:
#
# $ python exam_results.py
#
# A session with the program might look like the following:
#
# $ python exam_results.py
# What marks did you get in Maths?
# > 63
# What marks did you get in Philosophy?
# > 54
# What marks did you get in Geography?
# > 71
# What marks did you get in Music?
# > 68
#
# Your grades:
#
# Maths: B
# Philosophy: C
# Geography: A
# Music: B


SUBJECTS = ("Maths", "Philosophy", "Geography", "Music")

GRADE_BOUNDARIES = {
    "A": [70, 100],
    "B": [60, 69],
    "C": [50, 59],
    "D": [40, 49],
    "E": [30, 39],
    "F": [0, 29],
}


def get_grade(mark: int):
    for grade, (lower, upper) in GRADE_BOUNDARIES.items():
        if mark >= lower and mark <= upper:
            return grade
    raise ValueError("Mark sits outside of all grade boundaries.")


grades = {}

print("This program will ask you your marks and tell you what grade you got.")
for subject in SUBJECTS:
    question = "What marks did you get in {}?\n".format(subject)
    while True:
        try:
            grades[subject] = get_grade(int(input(question)))
            break
        except ValueError:
            question = f"That's not a valid mark. Try again - what marks did you get in {subject}?\n"

print("\nYour grades:\n")
for subject, grade in grades.items():
    print(f"{subject}: {grade}")

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Modify the program to handle the case where the user enters an invalid mark
#   (such as 150, or -25.5, or "bananas")
# * Modify the program to ask the user for the subjects that they've taken.
