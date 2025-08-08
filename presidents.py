import collections
import operator

from presidents_data import presidents_by_party

print(
    "There have been presidents from {} different parties".format(
        len(presidents_by_party)
    )
)

President = collections.namedtuple(
    "President",
    ["party", "name", "born", "took_office", "left_office", "age_took_office"],
)

presidents = []
for party, records in presidents_by_party.items():
    for record in records:
        presidents.append(
            President(
                party,
                record["name"],
                record["born"],
                record["took_office"],
                record["left_office"],
                (record["took_office"] - record["born"]).days // 365,
            )
        )
# Use age_took_office for default sorting
presidents = sorted(
    presidents,
    key=lambda president: president.age_took_office,
)

# TODO:
# * Display a report that answers the following questions:
#   * Which party has had most presidents?
party = max(
    presidents_by_party.keys(), key=lambda party: len(presidents_by_party.get(party))
)
print(
    f"The {party} party has had the most presidents, with {len(presidents_by_party[party])} presidents."
)
#   * Who was the youngest Republican president when they took office?
for president in presidents:
    if president.party == "Republican":
        break
print(
    f"The youngest Republican president when they took office was {president.name} at the age of {president.age_took_office}."
)
#   * Who was the oldest Democrat president when they took office?
for president in presidents[::-1]:
    if president.party == "Democratic":
        break
print(
    f"The oldest Democrat president when they took office was {president.name} at the age of {president.age_took_office}."
)
#   * Who was the youngest president (from any party) when they took office?
print(
    f"The youngest president when they took office was {presidents[0].name} at the age of {presidents[0].age_took_office}."
)
#   * Who was the oldest president (from any party) when they took office?
print(
    f"The oldest president when they took office was {presidents[-1].name} at the age of {presidents[-1].age_took_office}."
)
#   * Which month saw the most presidents take office?
months = sorted([president.took_office.strftime("%B") for president in presidents])
months_counter = collections.Counter(months)
((most_common_month, most_common_count),) = months_counter.most_common(1)
print(months_counter)
print(
    f"The month with the most presidents taking office is {most_common_month} with {most_common_count} presidents."
)
#   * Which decade saw the most presidents take office?
years = sorted([president.took_office.year for president in presidents])
decades = [year // 10 * 10 for year in years]
decades_counter = collections.Counter(decades)
print(decades_counter)
((most_common_decade, most_common_count),) = decades_counter.most_common(1)
print(
    f"The decade with the most presidents taking office is the {most_common_decade}s with {most_common_count} presidents."
)
#   * Which party has been in power for longest?
# Essentially recreating the initial dict so could have used that too
presidents_by_party = collections.defaultdict(list)
for president in sorted(presidents, key=operator.attrgetter("took_office")):
    presidents_by_party[president.party].append(president)
years_in_power_by_party = {
    party: sum(
        (president.left_office - president.took_office).days / 365
        for president in party_presidents
    )
    for party, party_presidents in presidents_by_party.items()
}
party_with_longest_total_time = max(
    years_in_power_by_party.keys(), key=years_in_power_by_party.get
)
print(
    f"The party that has been in power for the longest total time is {party_with_longest_total_time}, with {years_in_power_by_party[party_with_longest_total_time]:.2f} years."
)
#   * What is the average age of becoming president?
average_age = sum(p.age_took_office for p in presidents) / len(presidents)
print(f"The average age of becoming president is {average_age:.2f} years.")
#   * Which presidents have taken office more than once?
