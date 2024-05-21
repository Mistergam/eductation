import csv


with open('prices.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    data = list(reader)
    products = reader.fieldnames[1:]
    prices = []
    for d in data:
        for prod in products:
            prices.append(int(d[prod]))
    min_price = min(prices)
    output = []
    for d in data:
        for prod in products:
            if int(d[prod]) == min_price:
                output.append((prod, d['Магазин']))

output.sort(key=lambda x: (x[0], x[1]))
print(f'{output[0][0]}: {output[0][1]}')
