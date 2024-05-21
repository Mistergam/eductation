with open('files.txt', encoding="UTF-8") as f:
    data = f.readlines()
size_volumes = {'MB': 1024 ** 2, 'KB': 1024, 'B': 1, 'GB': 1024 ** 3}
d = {}
for line in data:
    ext = line.split()[0].split('.')[1]
    name = line.split()[0].split('.')[0] + '.' + ext
    size = int(line.split()[1]) * size_volumes[line.split()[2]]
    if ext in d:
        d[ext][0] += [name]
        d[ext][1] += size
    else:
        d[ext] = [[name], size]

for ext in sorted(d):
    print(*sorted(d[ext][0]), sep='\n')
    print('-' * 10)
    s = d[ext][1]
    if s < size_volumes['KB']:
        print(f'Summary: {s} B')
    elif s < size_volumes['MB']:
        print(f"Summary: {round(s / size_volumes['KB'])} KB")
    elif s < size_volumes['GB']:
        print(f"Summary: {round(s / size_volumes['MB'])} MB")
    else:
        print(f"Summary: {round(s / size_volumes['GB'])} GB")
    print()
