from datetime import date, datetime


with open('diary.txt', encoding='UTF-8') as f:
    d = {}
    key = None
    for line in f:
        if line[:10].replace('.', '').strip().isdigit():
            key = line.strip()
            d[key] = ''
        elif line.strip() == '':
            d[key] = d[key].strip()
            continue
        else:
            d[key] += line

i = 1
for key in sorted(d, key=lambda key: datetime.strptime(key, '%d.%m.%Y; %H:%M')):
    print(key)
    print(d[key])
    if i == len(d):
        break
    print()
    i += 1

