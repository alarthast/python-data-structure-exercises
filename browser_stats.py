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
browser_data = [
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


def get_first_occurrence_of_event(sorted_data, boolean_function):
    for row in sorted_data:
        if boolean_function(row):
            return row


def get_browsers_with_over_half_market_share(data):
    browsers_with_over_half_market_share = set()
    for row in data:
        for k, v in row._asdict().items():
            if isinstance(v, float) and v > 50:
                browsers_with_over_half_market_share.add(k.title())
    return browsers_with_over_half_market_share


def get_stats_for_browser_with_comparison_to_previous_month(sorted_data, browser):
    ComparisonRow = collections.namedtuple(
        "ComparisonRow", ["date", "current", "previous"]
    )
    return [
        ComparisonRow(date=date, current=current, previous=previous)
        for date, current, previous in zip(
            [datum.date for datum in sorted_data[:-1]],
            [getattr(datum, browser) for datum in sorted_data[:-1]],
            [getattr(datum, browser) for datum in sorted_data[1:]],
        )
    ]


# TODO:
# * Display a report that answers the following questions:
#   * What period does the report cover?
def report(data):
    data = sorted(data, key=operator.attrgetter("date"))

    date_when_firefox_first_became_most_popular = get_first_occurrence_of_event(
        data, lambda row: max(browsers, key=row.__getattribute__) == "firefox"
    ).date

    date_when_chrome_first_overtook_ie_in_popularity = get_first_occurrence_of_event(
        data, lambda row: row.chrome > row.ie
    ).date

    chrome_comparison_data = get_stats_for_browser_with_comparison_to_previous_month(
        data, "chrome"
    )

    print(
        f"The report covers the period between {min(row.date for row in data).strftime('%B %Y')} and {max(row.date for row in data).strftime('%B %Y')}."
    )

    #   * In the period covered, which browsers have had over 50% of market share?
    print(
        f'In the period covered, the following browsers had over 50% market share: {", ".join(get_browsers_with_over_half_market_share(data))}'
    )

    #   * In which month did Firefox first become the most popular browser?
    print(
        f"Firefox first became the most popular browser in {date_when_firefox_first_became_most_popular.strftime('%B %Y')}."
    )

    #   * In which month did Chrome first overtake IE in popularity?
    print(
        f"Chrome first overtook IE in popularity in {date_when_chrome_first_overtook_ie_in_popularity.strftime('%B %Y')}."
    )

    #   * In which month was Firefox's popularity highest?
    print(
        f"Firefox's popularity was highest in {max(data, key=operator.attrgetter('firefox')).date.strftime('%B %Y')}."
    )

    #   * In which month was the combined popularity of Safari and Opera highest?
    print(
        f"The combined popularity of Safari and Opera was highest in {max(data, key=lambda row: row.safari + row.opera).date.strftime('%B %Y')}."
    )

    #   * Which month saw the biggest percentage point rise in Chrome's popularity?
    print(
        f"The month that saw the biggest percentage point rise in Chrome's popularity was {max(chrome_comparison_data, key=lambda row: row.current - row.previous).date.strftime('%B %Y')}."
    )


if __name__ == "__main__":
    report(browser_data)
