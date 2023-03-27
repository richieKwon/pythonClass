class SampleException(Exception):
    '''Exception examples'''


def coroutine_except():
    print('>> coroutine stated')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('>> SampleException is going')
            else:
                print('>> coroutine received. {}'.format(x))

    finally:
        print('>> coroutine ends')


exe_co = coroutine_except()
print(next(exe_co))
print(exe_co.send(100))
print(exe_co.throw(SampleException))
print(exe_co.close())
