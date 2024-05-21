from zipfile import ZipFile


with ZipFile('workbook.zip') as zf:
    print(len(list(filter(lambda x: not x.is_dir(), zf.infolist()))))
