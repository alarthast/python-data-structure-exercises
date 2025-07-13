# This program reports how much individuals should pay for their order at
# dinner.
#
# Usage:
#
# $ python bill_splitting.py [name]
#
# For instance:
#
# $ python bill_splitting.py Tom
# Tom should pay 38.55
#
# or:
#
# $ python bill_splitting.py Tim
# Tim did not have dinner
import argparse
import itertools

BILL_ITEMS = [
    ["Tom", "Calamari", 6.00],
    ["Tom", "American Hot", 11.50],
    ["Tom", "Chocolate Fudge Cake", 4.45],
    ["Clare", "Bruschetta Originale", 5.35],
    ["Clare", "Fiorentina", 10.65],
    ["Clare", "Tiramasu", 4.90],
    ["Rich", "Bruschetta Originale", 5.35],
    ["Rich", "La Reine", 10.65],
    ["Rich", "Honeycomb Cream Slice", 4.90],
    ["Rosie", "Garlic Bread", 4.35],
    ["Rosie", "Veneziana", 9.40],
    ["Rosie", "Tiramasu", 4.90],
]


def by_name(list_item):
    return list_item[0]


BILL_ITEMS.sort(key=by_name)


# TODO:
# * Implement the program as described in the comments at the top of the file.
class Order:
    def __init__(self, menu_item, price):
        self.menu_item = menu_item
        self.price = price


ORDERS_BY_PERSON = {
    person: [Order(menu_item, price) for (_, menu_item, price) in group]
    for person, group in itertools.groupby(BILL_ITEMS, key=by_name)
}
AMOUNT_OWED_BY_PERSON = {
    person: sum(order.price for order in orders)
    for person, orders in ORDERS_BY_PERSON.items()
}


def get_parser():
    parser = argparse.ArgumentParser(
        description="This program reports how much individuals should pay for their order at dinner."
    )
    parser.add_argument("person", nargs="?", help="Name of the person at dinner")
    return parser


def get_message(person):
    if not person:
        return "\n".join(
            [
                f"{name:<10}|{amount_owed:<5}"
                for (name, amount_owed) in AMOUNT_OWED_BY_PERSON.items()
            ]
        )
    orders = ORDERS_BY_PERSON.get(person)
    if not orders:
        return f"{person} did not have dinner"
    breakdown = "\n".join([f"{order.menu_item} - {order.price}" for order in orders])
    return f"{person} should pay {AMOUNT_OWED_BY_PERSON.get(person)}. Breakdown:\n{breakdown}"


def main():
    args = get_parser().parse_args()
    print(get_message(args.person))


if __name__ == "__main__":
    main()

# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed
