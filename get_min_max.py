from dt import date


def get_min_max(dates):
    if dates:
        return (min(dates), max(dates))
    return tuple()


def get_date_range(start, end):
    if start > end:
        return []
    return [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end) + 1)]


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    sat_count = 0
    for i in range(date.toordinal(start), date.toordinal(end) + 1):
        if date.fromordinal(i).weekday() == 5:
            sat_count += 1
    return sat_count

date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))