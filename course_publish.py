from datetime import datetime


def choose_plural(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f'{str(amount)} {declensions[0]}'
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        return f'{str(amount)} {declensions[1]}'
    else:
        return f'{str(amount)} {declensions[2]}'


decl_d = ('день', 'дня', 'дней')
decl_h = ('час', 'часа', 'часов')
decl_m = ('минута', 'минуты', 'минут')
p = '%d.%m.%Y %H:%M'

input_date = datetime.strptime(input(), p)
publish_date = datetime.strptime('08.11.2022 12:00', p)
diff_d = (publish_date - input_date).days
diff_h = (publish_date - input_date).hour
diff_m = (publish_date - input_date).minute

print(f'До выхода курса осталось: {choose_plural(diff_d, decl_d)}')

