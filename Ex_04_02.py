"""
Завдання 2
Напишіть декоратор, який буде заміряти час виконання для наданої функції.
"""

import time

def my_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        my_rez = func
        end_time = time.time() - start_time
        return end_time
    return wrapper

@my_wrapper
def my_func():
    x = [x * 554 for x in range(10000000000)]
    return x

print(my_func())