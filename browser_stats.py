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
WideRow = collections.namedtuple("WideRow", ["date", *browsers])
wide_data = [
    WideRow(
        date=get_date(year, month),
        chrome=data["Chrome"],
        ie=data["IE"],
        firefox=data["Firefox"],
        safari=data["Safari"],
        opera=data["Opera"],
    )
    for year, inner_dict in browser_stats_by_year_and_month.items()
    for month, data in inner_dict.items()
]

TallRow = collections.namedtuple("TallRow", ["date", "browser", "market_share"])
tall_data = [
    TallRow(
        date=get_date(year, month),
        browser=browser,
        market_share=market_share,
    )
    for year, inner_dict in browser_stats_by_year_and_month.items()
    for month, data in inner_dict.items()
    for browser, market_share in data.items()
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
min_date = min(row.date for row in wide_data)
max_date = max(row.date for row in wide_data)
print(
    f"The report covers the period between {min_date.strftime('%B %Y')} and {max_date.strftime('%B %Y')}."
)

#   * In the period covered, which browsers have had over 50% of market share?
browsers_with_over_half_market_share = set()
for row in tall_data:
    if row.market_share > 50:
        browsers_with_over_half_market_share.add(row.browser)
print(
    f'In the period covered, the following browsers had over 50% market share: {", ".join(browsers_with_over_half_market_share)}'
)

#   * In which month did Firefox first become the most popular browser?
for row in sorted(wide_data, key=operator.attrgetter("date")):
    most_popular_browser = max(browsers, key=row.__getattribute__)
    if most_popular_browser == "firefox":
        break
print(f"Firefox first became the most popular browser in {row.date.strftime('%B %Y')}.")

#   * In which month did Chrome first overtake IE in popularity?
for row in sorted(wide_data, key=operator.attrgetter("date")):
    if row.chrome > row.ie:
        break
print(f"Chrome first overtook IE in popularity in {row.date.strftime('%B %Y')}.")

#   * In which month was Firefox's popularity highest?
print(
    f"Firefox's popularity was highest in {max(wide_data, key=operator.attrgetter('firefox')).date.strftime('%B %Y')}."
)


#   * In which month was the combined popularity of Safari and Opera highest?
print(
    f"The combined popularity of Safari and Opera was highest in {max(wide_data, key=lambda row: row.safari + row.opera).date.strftime('%B %Y')}."
)


#   * Which month saw the biggest percentage point rise in Chrome's popularity?
ChromeRow = collections.namedtuple("ChromeRow", ["date", "current", "previous"])
tall_data_filtered_to_chrome = sorted(
    [row for row in tall_data if row.browser == "Chrome"],
    key=operator.attrgetter("date"),
)
dates, _, current = zip(*tall_data_filtered_to_chrome[1:])
_, _, previous = zip(*tall_data_filtered_to_chrome[:-1])
chrome_data = [
    ChromeRow(date=date, current=current, previous=previous)
    for date, current, previous in zip(dates, current, previous)
]
print(
    f"The month that saw the biggest percentage point rise in Chrome's popularity was {max(chrome_data, key=lambda row: row.current - row.previous).date.strftime('%B %Y')}."
)

#   * Which month saw the biggest percentage point
