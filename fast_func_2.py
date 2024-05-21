import time


def get_the_fastest_func(funcs):
    results = []
    for func in funcs:
        start = time.perf_counter_ns()
        result = func()
        end = time.perf_counter_ns()
        results.append((func, end - start))
    results.sort(key=lambda el: el[1])
    print(*results)
    return results[0][0]


def for_and_append():  # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():  # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


print(get_the_fastest_func([for_and_append, list_comprehension]))
