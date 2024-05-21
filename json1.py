import json

with open('data.json', 'r', encoding='utf8') as f:
    data = json.load(f)
    output_data = []
    for el in data:
        if isinstance(el, str):
            output_data.append(el + '!')
        elif type(el) is int:
            output_data.append(el + 1)
        elif type(el) is bool:
            output_data.append(not el)
        elif isinstance(el, list):
            output_data.append(el * 2)
        elif isinstance(el, dict):
            el['newkey'] = None
            output_data.append(el)
with open('new_data.json', 'w', encoding='utf8') as fo:
    json.dump(output_data, fo, indent=3)
