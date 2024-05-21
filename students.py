import csv
import json

data = []
with open('students.json', 'r', encoding='utf8') as jsonfile:
    students = json.load(jsonfile)
for student in students:
    if student['age'] >= 18 and student['progress'] >= 75:
        data.append([student['name'], student['phone']])
data.sort(key=lambda x: x[0])
with open('data.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'phone'])
    writer.writerows(data)
