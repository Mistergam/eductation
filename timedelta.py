from datetime import date


result = [0] * 7

for y in range(1, 10000):
    for m in range(1, 13):
        current_date = date(y, m, 13)
        result[current_date.weekday()] += 1

for i in range(len(result)):
    print(i, '-', result[i])
