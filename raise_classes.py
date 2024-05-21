import csv


with open('student_counts.csv', 'r', encoding='utf-8') as fi:
    reader = list(csv.DictReader(fi))
    sorted_keys = ['year'] + sorted(list(reader[0].keys())[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
    output = [{k: d[k] for k in sorted_keys} for d in reader]
with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as fo:
    writer = csv.DictWriter(fo, fieldnames=sorted_keys)
    writer.writeheader()
    writer.writerows(output)
