from zipfile import ZipFile


r = []
with ZipFile('workbook.zip') as zf:
    for f in zf.infolist():
        if f.date_time > (2021, 11, 30, 14, 22) and not f.is_dir():
            if '/' in f.filename:
                r.append(f.filename.split('/')[1])
            else:
                r.append(f.filename)
print(*sorted(r), sep='\n')
