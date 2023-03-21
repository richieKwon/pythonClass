class avg:
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        return sum(self._series)/len(self._series)


def closureExample():
    # Free variable
    closureSeries = []

    # closure area
    def averager(v):
        closureSeries.append(v)
        return sum(closureSeries)/len(closureSeries)
    return averager


avg_closure1 = closureExample()
print(avg_closure1)
print(avg_closure1(1))
print(avg_closure1(2))
print(avg_closure1(3))
print(avg_closure1.__code__.co_freevars)

print(dir(avg_closure1.__closure__[0]))
print(dir(avg_closure1.__closure__[0].cell_contents))
