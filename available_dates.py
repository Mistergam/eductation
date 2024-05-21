from datetime import datetime, timedelta


def get_dates_range(list_dates):
    p = '%d.%m.%Y'
    date_list = []
    for el in list_dates:
        if '-' not in el:
            date_list.append(datetime.strptime(el, p))
        else:
            start, end = (datetime.strptime(d, p) for d in el.split('-'))
            current_date = start
            while current_date <= end:
                date_list.append(current_date)
                current_date += timedelta(days=1)
    return date_list


def get_book_dates(string):
    p = '%d.%m.%Y'
    date_list = []
    if len(string.split('-')) == 1:
        date_list.append(datetime.strptime(string, p))
    else:
        start, end = (datetime.strptime(d, p) for d in string.split('-'))
        current_date = start
        while current_date <= end:
            date_list.append(current_date)
            current_date += timedelta(days=1)
    return date_list


def is_available_date(booked_dates, dates_for_booking):
    return all(d not in get_dates_range(booked_dates) for d in get_book_dates(dates_for_booking))


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-03.11.2021'
print(is_available_date(dates, some_date))
