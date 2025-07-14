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
import sys

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


# TODO:
# * Implement the program as described in the comments at the top of the file.
ORDERS_BY_PERSON = {}
for name, menu_item, price in BILL_ITEMS:
    orders = ORDERS_BY_PERSON.get(name, []) + [(menu_item, price)]
    ORDERS_BY_PERSON.update({name: orders})
MENU_ITEMS_BY_PERSON = {
    name: tuple(order[0] for order in orders)
    for name, orders in ORDERS_BY_PERSON.items()
}
PRICES_BY_PERSON = {
    name: tuple(order[1] for order in orders)
    for name, orders in ORDERS_BY_PERSON.items()
}


def get_message(person):
    if not person:
        return "\n".join(
            [
                f"{name:<10}|{sum(prices):<5}"
                for (name, prices) in PRICES_BY_PERSON.items()
            ]
        )
    menu_items = MENU_ITEMS_BY_PERSON.get(
        person,
    )
    prices = PRICES_BY_PERSON.get(person)

    if not menu_items:
        return f"{person} did not have dinner"
    breakdown = "\n".join(
        [f"{menu_items[i]} - {prices[i]}" for i in range(len(menu_items))]
    )
    return f"{person} should pay {sum(prices)}. Breakdown:\n{breakdown}"


def main():
    try:
        person = sys.argv[1]
    except IndexError:
        person = None
    print(get_message(person))


if __name__ == "__main__":
    main()

# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed
