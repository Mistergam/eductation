from zipfile import ZipFile


with ZipFile('workbook.zip') as zf:
    init_size = sum([f.file_size for f in zf.infolist()])
    arch_size = sum([f.compress_size for f in zf.infolist()])
print('Объем исходных файлов:', init_size, 'байт(а)')
print('Объем сжатых файлов:', arch_size, 'байт(а)')
