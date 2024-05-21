import csv


with open('sales.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter=';')

    result = [row[0] for row in reader if row[1].isdigit() and int(row[2]) < int(row[1])]
print(*result, sep='\n')
