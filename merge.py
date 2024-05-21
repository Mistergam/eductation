import json


with open('data1.json', 'r', encoding='utf8') as f1, open('data2.json', 'r', encoding='utf8') as f2:
    d1 = json.load(f1)
    d2 = json.load(f2)
    d3 = {}
    for k in list(d1.keys()) + list(d2.keys()):
        if k in d2:
            d3[k] = d2[k]
        else:
            d3[k] = d1[k]
with open('data_merge.json', 'w', encoding='utf8') as f:
    json.dump(d3, f, indent=3)
