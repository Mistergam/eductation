import json


with open('people.json', 'r', encoding='utf8') as f:
    data = json.load(f)
keys = {key for obj in data for key in obj.keys()}
template_obj = {key: None for key in keys}
with open('updated_people.json', 'w', encoding='utf8') as fo:
    json.dump([template_obj | obj for obj in data], fo, indent=3)
