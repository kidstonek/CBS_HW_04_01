"""
Завдання 5
Створіть список цілих чисел. Отримайте список квадратів
непарних чисел із цього списку.

"""

def my_wrapper(func):
    def wrapper(*args, **kwargs):
        return list(filter(lambda x: (x % 2 != 0 ), func(*args, **kwargs)))
    return wrapper

@my_wrapper
def int_numbers(n: int):
    return [i for i in range(1,n)]


number = int(input("please q-ty of numbers: "))

print(int_numbers(number))