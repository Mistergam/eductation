import json


with open('food_services.json', 'r', encoding='utf8') as f:
    services = json.load(f)

districts = {}
opers = {}
for service in services:
    district = service['District']
    oper = service['OperatingCompany']
    districts[district] = districts.get(district, 0) + 1
    if oper != "":
        opers[oper] = opers.get(oper, 0) + 1
max_district = max(districts, key=districts.get)
max_oper = max(opers, key=opers.get)
print(f'{max_district}: {districts[max_district]}')
print(f'{max_oper}: {opers[max_oper]}')
