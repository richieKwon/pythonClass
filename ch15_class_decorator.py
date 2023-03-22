# decorator - for precise code and get rid of duplications
# easier and preciser than closure
# hard to debug if you use it too much

import time


def performance(func):
    def performance_clocked(*args):
        startTime = time.perf_counter()
        result = func(*args)
        endTime = time.perf_counter() - startTime
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print(startTime)
        print(name)
        print(arg_str)
        print(result)
        return result
    return performance_clocked


def time_func(seconds):
    time.sleep(seconds)


@performance
def sum_func(*numbers):
    return sum(numbers)


# non decorator
# non_deco = performance(sum_func)
# print(non_deco(2))

# decorator
print(sum_func(1, 2, 3, 4, 5))
