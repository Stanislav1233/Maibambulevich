import time
from functools import wraps


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} выполнена за {end - start:.6f} сек.")
        return result
    return wrapper



@timer
def f():
    time.sleep(1.5)
    return "готово"


f()
