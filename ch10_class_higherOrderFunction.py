from operator import add
from functools import reduce


def factorial(n):
    ''' Factorial function > n :int '''
    if n == 1:
        return 1
    return n * factorial(n-1)


print(list(map(factorial, range(1, 6))))
print(list(map(factorial, filter(lambda x: x % 2, range(1, 6)))))

# function tools
print(reduce(add, range(0, 11)))
print(reduce(lambda x, temp: x+temp, range(0, 11)))
print(sum(range(1, 11)))

# callable
