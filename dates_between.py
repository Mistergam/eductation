from datetime import datetime, timedelta


start_date, end_date = [datetime.strptime(input(), '%d.%m.%Y') for _ in range(2)]
current_date = start_date
while (current_date.day + current_date.month) % 2 == 0:
    current_date += timedelta(days=1)
result = []
while current_date <= end_date:
    if current_date.weekday() not in (0, 3):
        print(datetime.strftime(current_date, '%d.%m.%Y'), current_date.weekday())
    current_date += timedelta(days=3)
