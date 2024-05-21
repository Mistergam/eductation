import json
import csv


dict_scores = {}
with open('exam_results.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f)
    keys = next(reader)
    keys[2] = 'best_score'
    exams = list(reader)
exams.sort(key=lambda x: (x[4], x[3]))
for exam in exams[1:]:
    dict_scores[exam[4]] = {keys[i]: exam[i] if i != 2 else int(exam[i]) for i in range(len(exam))}
best_scores = [d for d in dict_scores.values()]

with open('best_scores.json', 'w', encoding='utf8') as jsonfile:
    json.dump(best_scores, jsonfile, indent=3)
