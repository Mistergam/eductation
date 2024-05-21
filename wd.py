from datetime import datetime, date, time


def to_min(time):
        hours, minutes = list(map(int, time.split(':')))
        return hours * 60 + minutes
def diff(start, end):
        return to_min(end) - to_min(start)


dt, tm = input().split()
d = {wd: ('9:00', '21:00') if 0 <= wd <= 4 else ('10:00', '18:00') for wd in range(7)}
result = diff(tm, d[datetime.strptime(dt, '%d.%m.%Y').weekday()][1])
if result < 0 or to_min(tm) < to_min(d[datetime.strptime(dt, '%d.%m.%Y').weekday()][0]):
        print('Магазин не работает')
else:
        print(diff(tm, d[datetime.strptime(dt, '%d.%m.%Y').weekday()][1]))
