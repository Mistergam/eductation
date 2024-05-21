import csv
from functools import reduce


with open('salary_data.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=';')
    s = 0
    result = reduce(lambda name, sal: [name, s + int(sal)], reader)

for line in sorted(result, key=lambda el: (el[1], el[0])):
    print(line[0])

