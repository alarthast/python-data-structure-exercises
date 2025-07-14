import bill_splitting
import pytest


def test_no_name_given():
    rows = [
        "Clare     |20.9 ",
        "Rich      |20.9 ",
        "Rosie     |18.65",
        "Tom       |21.95",
    ]
    msg = bill_splitting.get_message(None)
    for row in rows:  # We don't care about the order of names
        assert row in msg


@pytest.mark.parametrize(
    "person,result",
    [
        (
            "Clare",
            "Clare should pay 20.9. Breakdown:\nBruschetta Originale - 5.35\nFiorentina - 10.65\nTiramasu - 4.9",
        ),
        (
            "Tom",
            "Tom should pay 21.95. Breakdown:\nCalamari - 6.0\nAmerican Hot - 11.5\nChocolate Fudge Cake - 4.45",
        ),
        (
            "Rich",
            "Rich should pay 20.9. Breakdown:\nBruschetta Originale - 5.35\nLa Reine - 10.65\nHoneycomb Cream Slice - 4.9",
        ),
        (
            "Rosie",
            "Rosie should pay 18.65. Breakdown:\nGarlic Bread - 4.35\nVeneziana - 9.4\nTiramasu - 4.9",
        ),
        ("Tim", "Tim did not have dinner"),
    ],
)
def test_person_given(person, result):
    assert bill_splitting.get_message(person) == result
