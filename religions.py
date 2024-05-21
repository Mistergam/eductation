import json


with open('countries.json', 'r', encoding='utf8') as f:
    data = json.load(f)
output_data = {}
for obj in data:
    output_data.setdefault(obj['religion'], []).append(obj['country'])
with open('religion.json', 'w', encoding='utf8') as fo:
    json.dump(output_data, fo, indent=3)
