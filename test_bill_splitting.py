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
    for row in rows:
        assert row in msg


@pytest.mark.parametrize(
    "person,result",
    [
        (
            "Clare",
            "Clare should pay 20.9. Breakdown:\nBruschetta Originale - 5.35\nFiorentina - 10.65\nTiramasu - 4.9",
        )
    ],
)
def test_person_given(person, result):
    assert bill_splitting.get_message(person) == result
