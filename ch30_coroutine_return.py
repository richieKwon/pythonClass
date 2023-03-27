def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return avg


avger = averager_re()

print(next(avger))
avger.send(100)
avger.send(200)

try:
    avger.send(None)
except StopIteration as e:
    print(e.value)
