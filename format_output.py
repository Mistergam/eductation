from zipfile import ZipFile


output = []
with ZipFile('workbook.zip') as zf:
    for f in filter(lambda x: not x.is_dir(), zf.infolist()):
        name = f.filename if '/' not in f.filename else f.filename.split('/')[1]
        Y, m, d, H, M, S = f.date_time
        output.append(f'''{name}
  Дата модификации файла: {Y}-{str(m).zfill(2)}-{str(d).zfill(2)} {str(H).zfill(2)}:{str(M).zfill(2)}:{str(S).zfill(2)}
  Объем исходного файла: {f.file_size} байт(а)
  Объем сжатого файла: {f.compress_size} байт(а)''')

print(*sorted(output), sep='\n\n')
