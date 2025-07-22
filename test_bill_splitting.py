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
            "Clare should pay 20.9. Breakdown:\nBruschetta Originale, Fiorentina, Tiramasu",
        ),
        (
            "Tom",
            "Tom should pay 21.95. Breakdown:\nCalamari, American Hot, Chocolate Fudge Cake",
        ),
        (
            "Rich",
            "Rich should pay 20.9. Breakdown:\nBruschetta Originale, La Reine, Honeycomb Cream Slice",
        ),
        (
            "Rosie",
            "Rosie should pay 18.65. Breakdown:\nGarlic Bread, Veneziana, Tiramasu",
        ),
        ("Tim", "Tim did not have dinner"),
    ],
)
def test_person_given(person, result):
    assert bill_splitting.get_message(person) == result
