from zipfile import ZipFile


def format_bytes(size):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    for unit in units:
        if size < 1024:
            return f"{round(size)} {unit}"
        size = size / 1024


result = []
with ZipFile('desktop.zip') as zf:
    for f in zf.infolist():
        c = f.filename.count('/')
        if f.is_dir():
            print('  ' * (c - 1) + f.filename.split('/')[c - 1])
        else:
            print('  ' * c + f.filename.split('/')[c] + ' ' + format_bytes(f.file_size))
