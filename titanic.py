import csv


with open('titanic.csv', 'r', encoding='utf-8') as f:
    data = list(filter(lambda line: int(line[0]) == 1 and float(line[3]) < 18, list(csv.reader(f, delimiter=';'))[1:]))
for row in sorted(data, key=lambda r: r[2], reverse=True):
    print(row[1])
