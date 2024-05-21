import json


with open('food_services.json', 'r', encoding='utf8') as f:
    services = json.load(f)

types = {}
for service in services:
    t = service['TypeObject']
    n = service['Name']
    s = service['SeatsCount']
    if t not in types or s > types[t][1]:
        types[t] = (n, s)

for k in sorted(types):
    print(f'{k}: {types[k][0]}, {types[k][1]}')
