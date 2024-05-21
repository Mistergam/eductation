import csv


with open('wifi.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    temp = list(reader)[1:]
    data = sorted([(row[1], int(row[3])) for row in temp])
d = {}
for rayon, count in data:
    if rayon in d:
        d[rayon] += count
    else:
        d[rayon] = count

for r, c in dict(sorted(d.items(), reverse=True, key=lambda item: item[1])).items():
    print(f'{r}: {c}')
