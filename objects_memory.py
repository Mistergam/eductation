import gc
import types


def is_user_defined(obj):
    """Проверяет, является ли объект определенным пользователем (не системным)"""
    if isinstance(obj, types.ModuleType):
        return False
    if isinstance(obj, (types.BuiltinFunctionType, types.BuiltinMethodType)):
        return False
    if isinstance(obj, type):
        if obj.__module__ == 'builtins':
            return False
    if hasattr(obj, '__module__'):
        return not obj.__module__.startswith('builtins')
    return True


gc.collect()
n1 = (1, [1, 2, 3], 100)
print(id(n1))
n1[1].append(5)
print(id(n1))
print(n1)

# Включаем сборщик мусора
gc.collect()

# Получаем все объекты, которые в данный момент находятся в памяти
objects = gc.get_objects()

# Фильтруем объекты, созданные именно вашим кодом
user_defined_objects = [obj for obj in objects if is_user_defined(obj)]

# Печатаем информацию об этих объектах
for obj in user_defined_objects:
    print(f'{type(obj)}: {repr(obj)}')