import csv
from functools import reduce

'''
with open('name_log.csv', 'r', encoding='utf-8') as fi:
    reader = csv.DictReader(fi)
    dict_temp = list(sorted(reader, key=lambda d: (d['email'], d['dtime'])))
dict_out = {}
for d in dict_temp:
    email = d['email']
    dtime = d['dtime']
    if email not in dict_out or dtime > dict_out[email]['dtime']:
        dict_out[email] = d
dict_out = list(dict_out.values())
cols = dict_out[0].keys()
with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as fo:
    writer = csv.DictWriter(fo, fieldnames=cols)
    writer.writeheader()
    writer.writerows(dict_out)
'''
#укороченная версия - очень понравилась, так что пробую воспроизвести не переписывая.

with open('name_log.csv', 'r', encoding='utf-8') as fi, open('new_name_log.csv', 'w', encoding='utf-8', newline='') as fo:
    reader, writer = csv.reader(fi), csv.writer(fo)
    writer.writerow(next(reader))
    writer.writerows({line[1]: line for line in sorted(reader, key=lambda x: (x[1], x[2]))}.values())
