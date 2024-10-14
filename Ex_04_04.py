






from functools import lru_cache
import time


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


start_time = time.time()
fib(25)
print(f'{time.time()-start_time}')

start_time = time.time()
fib_cache(256)
print(f'{time.time()-start_time}')

start_time = time.time()
fib_cache_ten(256)
print(f'{time.time()-start_time}')

start_time = time.time()
fib_cache_sixteen(256)
print(f'{time.time()-start_time}')
