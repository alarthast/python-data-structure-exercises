# This program displays a report about browser usage statistics, as recorded by
# w3schools.com.
#
# Usage:
#
# $ python browser_stats.py

import collections
import datetime
import operator

from browser_stats_data import browser_stats_by_year_and_month


def get_date(year, month):
    return datetime.datetime.strptime(f"{year}{month}", "%Y%B").date()


browsers = ("chrome", "ie", "firefox", "safari", "opera")
Row = collections.namedtuple("WideRow", ["date", *browsers])
data = [
    Row(
        date=get_date(year, month),
        chrome=stats["Chrome"],
        ie=stats["IE"],
        firefox=stats["Firefox"],
        safari=stats["Safari"],
        opera=stats["Opera"],
    )
    for year, inner_dict in browser_stats_by_year_and_month.items()
    for month, stats in inner_dict.items()
]

print(
    "browser_stats_by_year_and_month is a {} with {} elements".format(
        type(browser_stats_by_year_and_month).__name__,
        len(browser_stats_by_year_and_month),
    )
)


# TODO:
# * Display a report that answers the following questions:
#   * What period does the report cover?
min_date = min(row.date for row in data)
max_date = max(row.date for row in data)
print(
    f"The report covers the period between {min_date.strftime('%B %Y')} and {max_date.strftime('%B %Y')}."
)


#   * In the period covered, which browsers have had over 50% of market share?
def get_browsers_with_over_half_market_share(data):
    browsers_with_over_half_market_share = set()
    for row in data:
        for k, v in row._asdict().items():
            if isinstance(v, float) and v > 50:
                browsers_with_over_half_market_share.add(k)
    return browsers_with_over_half_market_share


print(
    f'In the period covered, the following browsers had over 50% market share: {", ".join(get_browsers_with_over_half_market_share(data))}'
)

#   * In which month did Firefox first become the most popular browser?
for row in sorted(data, key=operator.attrgetter("date")):
    most_popular_browser = max(browsers, key=row.__getattribute__)
    if most_popular_browser == "firefox":
        break
print(f"Firefox first became the most popular browser in {row.date.strftime('%B %Y')}.")

#   * In which month did Chrome first overtake IE in popularity?
for row in sorted(data, key=operator.attrgetter("date")):
    if row.chrome > row.ie:
        break
print(f"Chrome first overtook IE in popularity in {row.date.strftime('%B %Y')}.")

#   * In which month was Firefox's popularity highest?
print(
    f"Firefox's popularity was highest in {max(data, key=operator.attrgetter('firefox')).date.strftime('%B %Y')}."
)


#   * In which month was the combined popularity of Safari and Opera highest?
print(
    f"The combined popularity of Safari and Opera was highest in {max(data, key=lambda row: row.safari + row.opera).date.strftime('%B %Y')}."
)


#   * Which month saw the biggest percentage point rise in Chrome's popularity?
ChromeRow = collections.namedtuple("ChromeRow", ["date", "current", "previous"])
sorted = sorted(data, key=operator.attrgetter("date"))
chrome_data = [
    ChromeRow(date=date, current=current, previous=previous)
    for date, current, previous in zip(
        [datum.date for datum in sorted[:-1]],
        [datum.chrome for datum in sorted[:-1]],
        [datum.chrome for datum in sorted[1:]],
    )
]
print(
    f"The month that saw the biggest percentage point rise in Chrome's popularity was {max(chrome_data, key=lambda row: row.current - row.previous).date.strftime('%B %Y')}."
)

#   * Which month saw the biggest percentage point
