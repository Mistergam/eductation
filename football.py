from zipfile import ZipFile
import json


def is_correct_json(string):
    try:
        json_data = json.loads(string)
        return True
    except Exception:
        return False


footballers = []

with ZipFile('data.zip') as zf:
    for file_info in zf.infolist():
        if file_info.filename.endswith('.json'):
            with zf.open(file_info) as file:
                content = file.read()
                if is_correct_json(content):
                    data = json.loads(content)
                    if data.get("team") == "Arsenal":
                        first_name = data.get("first_name", "")
                        last_name = data.get("last_name", "")
                        footballers.append((first_name, last_name))
footballers.sort(key=lambda x: (x[0], x[1]))
for first_name, last_name in footballers:
    print(f"{first_name} {last_name}")
