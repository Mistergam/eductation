import calendar
from datetime import date


def get_all_mondays(year):
    s = 0
    for m in range(1, 13):
        for d in range(1, calendar.monthrange(year, m)[1] + 1):
            if date(year, m, d).weekday() == 0:
                s += 1
    return s

print(get_all_mondays(111))
