from collections import namedtuple

from presidents_data import presidents_by_party

print(
    "There have been presidents from {} different parties".format(
        len(presidents_by_party)
    )
)

President = namedtuple(
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

presidents_sorted = sorted(
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
for president in presidents_sorted:
    if president.party == "Republican":
        youngest_republican = president
        break
print(
    f"The youngest Republican president when they took office was {youngest_republican.name} at the age of {youngest_republican.age_took_office}."
)
#   * Who was the oldest Democrat president when they took office?
for president in presidents_sorted[::-1]:
    if president.party == "Democratic":
        oldest_democrat = president
        break
print(
    f"The oldest Democrat president when they took office was {oldest_democrat.name} at the age of {oldest_democrat.age_took_office}."
)
#   * Who was the youngest president (from any party) when they took office?
print(
    f"The youngest president when they took office was {presidents_sorted[0].name} at the age of {presidents_sorted[0].age_took_office}."
)
#   * Who was the oldest president (from any party) when they took office?
print(
    f"The oldest president when they took office was {presidents_sorted[-1].name} at the age of {presidents_sorted[-1].age_took_office}."
)
#   * Which month saw the most presidents take office?
#   * Which decade saw the most presidents take office?
#   * Which party has been in power for longest?
#   * What is the average age of becoming president?
average_age = sum(p.age_took_office for p in presidents) / len(presidents)
print(f"The average age of becoming president is {average_age:.2f} years.")
#   * Which presidents have taken office more than once?
