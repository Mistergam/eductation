import json


result = []
with open('pools.json', 'r', encoding='utf8') as f:
    pools = json.load(f)
for pool in pools:
    length = pool['DimensionsSummer']['Length']
    width = pool['DimensionsSummer']['Width']
    time = pool['WorkingHoursSummer']['Понедельник'].split('-')
    address = pool['Address']
    if time[0] <= '10:00' and time[1] >= '12:00':
        result.append((length, width, address))
result.sort(key=lambda r: (r[0], r[1]), reverse=True)
print(f'{result[0][0]}x{result[0][1]}', result[0][2], sep='\n')
