import collections

from presidents_data import presidents_by_party

print(
    "There have been presidents from {} different parties".format(
        len(presidents_by_party)
    )
)

President = collections.namedtuple(
    "President",
    [
        "party",
        "name",
        "born",
        "took_office",
        "left_office",
        "age_took_office",
        "days_in_office",
    ],
)

PRESIDENTS = []
for party, records in presidents_by_party.items():
    for record in records:
        PRESIDENTS.append(
            President(
                party,
                record["name"],
                record["born"],
                record["took_office"],
                record["left_office"],
                (record["took_office"] - record["born"]).days // 365,
                (record["left_office"] - record["took_office"]).days,
            )
        )


def get_first_row_where_field_is_value(sorted_presidents, field, value):
    for president in sorted_presidents:
        if getattr(president, field) == value:
            return president
    assert False, f"No presidents found with {field} = {value}"


def get_counter_for_field(presidents, field, transform_func=None):
    values = [getattr(president, field) for president in presidents]
    if transform_func:
        values = [transform_func(value) for value in values]
    return collections.Counter(values)


def get_most_common_value(presidents, field, transform_func=None):
    counter = get_counter_for_field(presidents, field, transform_func)
    return counter.most_common(1)[0]


def aggregate(presidents, field_to_agg, by_field):
    aggregated = collections.defaultdict(int)
    for president in presidents:
        aggregated[president.party] += getattr(president, field_to_agg)
    return aggregated


# TODO:
# * Display a report that answers the following questions:


def report(presidents):
    # Use age_took_office for default sorting
    presidents = sorted(
        presidents,
        key=lambda president: president.age_took_office,
    )

    #   * Which party has had most presidents?
    most_common_party, most_common_party_count = get_most_common_value(
        presidents, "party"
    )

    #   * Who was the youngest Republican president when they took office?
    youngest_republican = get_first_row_where_field_is_value(
        presidents, "party", "Republican"
    )

    #   * Who was the oldest Democrat president when they took office?
    oldest_democrat = get_first_row_where_field_is_value(
        presidents[::-1], "party", "Democratic"
    )

    #   * Who was the youngest president (from any party) when they took office?
    youngest_president = presidents[0]

    #   * Who was the oldest president (from any party) when they took office?
    oldest_president = presidents[-1]

    #   * Which month saw the most presidents take office?
    most_common_month, most_common_month_count = get_most_common_value(
        presidents, "took_office", lambda date: date.strftime("%B")
    )

    #   * Which decade saw the most presidents take office?
    most_common_decade, most_common_decade_count = get_most_common_value(
        presidents, "took_office", lambda date: date.year // 10 * 10
    )

    #   * Which party has been in power for longest?
    days_in_power_by_party = aggregate(presidents, "days_in_office", "party")
    party_with_longest_total_time = max(
        days_in_power_by_party.keys(), key=days_in_power_by_party.get
    )

    #   * What is the average age of becoming president?
    average_age = sum(p.age_took_office for p in presidents) / len(presidents)

    #   * Which presidents have taken office more than once?
    name_counter = get_counter_for_field(presidents, "name")
    multi_office_presidents = [
        name for name, count in name_counter.items() if count > 1
    ]

    print(
        f"The {most_common_party} party has had the most presidents, with {most_common_party_count} presidents."
    )
    print(
        f"The youngest Republican president when they took office was {youngest_republican.name} at the age of {youngest_republican.age_took_office}."
    )
    print(
        f"The oldest Democrat president when they took office was {oldest_democrat.name} at the age of {oldest_democrat.age_took_office}."
    )
    print(
        f"The youngest president when they took office was {youngest_president.name} at the age of {youngest_president.age_took_office}."
    )
    print(
        f"The oldest president when they took office was {oldest_president.name} at the age of {oldest_president.age_took_office}."
    )
    print(
        f"The month with the most presidents taking office is {most_common_month} with {most_common_month_count} presidents."
    )
    print(
        f"The decade with the most presidents taking office is the {most_common_decade}s with {most_common_decade_count} presidents."
    )
    print(
        f"The party that has been in power for the longest total time is {party_with_longest_total_time}, with {days_in_power_by_party[party_with_longest_total_time]} days."
    )
    print(f"The average age of becoming president is {average_age:.2f} years.")
    print(
        "President(s) who have taken office more than once are: "
        + ",".join(multi_office_presidents)
    )


if __name__ == "__main__":
    report(PRESIDENTS)
