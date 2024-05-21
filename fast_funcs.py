from math import factorial                   # функция из модуля math
import time


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


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


print(get_the_fastest_func([factorial, factorial_recurrent, factorial_classic], 900))
