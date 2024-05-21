from zipfile import ZipFile


compress_values = []
with ZipFile('workbook.zip') as zf:
    for f in zf.infolist():
        if not f.is_dir():
            compress_values.append((f.filename, f.compress_size / f.file_size))
compress_values.sort(key=lambda x: x[1])
print(compress_values[0][0].split('/')[1])
