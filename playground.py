import csv
import json


addresses = {}

with open('playgrounds.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        addresses.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])

with open('addresses.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(addresses, jsonfile, ensure_ascii=False, indent=3)
