from dt import date


def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except:
        return False


entry = input()
while entry != 'end':
    if is_correct(*entry.split('.')):
        print('Корректная')
    else:
        print('Некорректная')
    entry = input()

print(is_correct(12, 05))