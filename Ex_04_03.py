"""
Завдання 3
Напишіть програму яка буде виводити 25 перших чисел Фібоначі,
використовуючи для цього три наведені в тексті заняття функції — без кешу,
з кешем довільної довжини, з кешем з модулю functools з максимальною кількістю 10
елементів та з кешем з модулю functools з максимальною кількістю 16 елементів.
"""

from functools import lru_cache


def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


@lru_cache(maxsize=None)
def fib_cache(n):
    if n < 2:
        return n
    return fib_cache(n-1) + fib_cache(n-2)


@lru_cache(maxsize=10)
def fib_cache_ten(n):
    if n < 2:
        return n
    return fib_cache_ten(n-1) + fib_cache_ten(n-2)


@lru_cache(maxsize=16)
def fib_cache_sixteen(n):
    if n < 2:
        return n
    return fib_cache_sixteen(n-1) + fib_cache_sixteen(n-2)


# print([fib(n) for n in range(25)])
# print([fib_cache(n) for n in range(25)])
# print([fib_cache_ten(n) for n in range(25)])
# print([fib_cache_sixteen(n) for n in range(25)])

