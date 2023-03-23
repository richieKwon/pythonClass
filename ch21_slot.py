# Slot : manage instance property by using Set (instead of __dict__)

import timeit


class TestA:
    __slots__ = ('a',)


class TestB:
    pass


use_slot = TestA()
no_slot = TestB()


def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner


print(min(timeit.repeat(repeat_outer(use_slot), number=100)))
print(min(timeit.repeat(repeat_outer(no_slot), number=100)))
