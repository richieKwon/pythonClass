from functools import wraps
from inspect import getgeneratorstate


def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine end')


c1 = coroutine1()

# print(c1, type(c1))

# next(c1)

# c1.send(777)

# GEN_CREATED : standby initial status
# GEN_RUNNING : running
# GEN_SUSPENDED : standby yield
# GEN_CLOSED : running completed


def coroutine2(x):
    print('>>> coroutine started', x)
    y = yield x
    print('>>> coroutine received', y)
    z = yield x + y
    print('>>> coroutine received', z)


c3 = coroutine2(10)
print(getgeneratorstate(c3))
print(next(c3))
print(getgeneratorstate(c3))

# decorator pattern


def coroutine7(func):
    '''Decorator runs until yield'''
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@ coroutine7
def summer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = summer()

print(su.send(100))
print(su.send(777))
