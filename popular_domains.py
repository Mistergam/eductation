import csv


with open('data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    r = list(reader)[1:]
    list_domains = [row[2].split('@')[1] for row in r]
d = {}
for domain in list_domains:
    if domain in d:
        d[domain] += 1
    else:
        d[domain] = 1
rows_to_write = [[domain, usage] for domain, usage in dict(sorted(d.items(), key=lambda item: (item[1], item[0]))).items()]

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['domain', 'usage'])
    writer.writerows(rows_to_write)
