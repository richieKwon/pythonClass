def gen2():
    yield from 'AB'
    yield from range(1, 4)


# t3 = gen2()
# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))
# print(next(t3))

def gen3_sub():
    print('sub coroutine.')
    x = yield 10
    print('Received: ', str(x))
    x = yield 100
    print('Received: ', str(x))


def gen4_main():
    yield from gen3_sub()


t5 = gen4_main()

print(next(t5))
# print(t5.send(7))
