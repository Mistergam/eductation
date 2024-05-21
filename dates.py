from datetime import datetime, timedelta


p = '%d.%m.%Y'
t = '%d.%m'
target_date = datetime.strptime(input(), p) + timedelta(days=1)
current = target_date
check_list = []
while current <= target_date + timedelta(days=6):
    check_list.append(current.strftime(t))
    current += timedelta(days=1)
input_data = [input().rsplit(' ', 1) for _ in range(int(input()))]
output_data = sorted(input_data, key=lambda el: el[1], reverse=True)
result = [name for name, dt in output_data if dt.strftime(t) in check_list]
if len(result):
    print(result[0])
else:
    print('Дни рождения не планируются')
