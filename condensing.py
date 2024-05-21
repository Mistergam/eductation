import csv


def condense_csv(filename, id_name):
    with open(filename, 'r', encoding='utf-8') as fi, open('condensed.csv', 'w', encoding='utf-8') as fo:
        reader = csv.reader(fi)
        data = {}
        for obj, attr, value in reader:
            if obj not in data:
                data[obj] = {id_name: obj}
            data[obj][attr] = value
    with open('condensed.csv', 'w', encoding='utf-8', newline='') as fo:
        writer = csv.DictWriter(fo, fieldnames=data[obj])
        writer.writeheader()
        writer.writerows(data.values())


condense_csv('data2.csv', 'object_ID')
