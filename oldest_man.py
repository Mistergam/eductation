from datetime import datetime


data = list(map(lambda el: [el[0], datetime.strptime(el[1], '%d.%m.%Y')],
                [input().rsplit(' ', 1) for _ in range(int(input()))]))
min_date = min([el[1] for el in data])
min_date_output = datetime.strftime(min_date, '%d.%m.%Y')
result = []
for el in data:
    if el[1] == min_date:
        result.append(el[0])
if len(result) == 1:
    print(min_date_output, result[0])
elif len(result) > 1:
    print(min_date_output, len(result))
