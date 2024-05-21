import time


def get_the_fastest_func(funcs, arg):
    results = []
    for func in funcs:
        start = time.perf_counter_ns()
        result = func(arg)
        end = time.perf_counter_ns()
        results.append((func, end - start))
    results.sort(key=lambda el: el[1])
    print(*results)
    return results[0][0]


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_00)))
