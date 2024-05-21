import sys


data = list(map(lambda x: int(x.strip()), sys.stdin.readlines()))
print(data)
i = len(data) - 1
while data[i] % 2:
    i -= 1
if i % 2:
    print('Анри')
else:
    print('Дима')
