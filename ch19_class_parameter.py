def mul(x, y):
    x += y
    return x


def mul2(x, y):
    z = x + y
    return z


x = 10
y = 5

# print(mul(x, y), x, y)

a = [10, 100]
b = [5, 10]

# print(mul(a, b), a, b)

c = (10, 8)
d = (9, 7)

print(mul(c, d), c, d)

print(id(mul2(a, b)), id(a), id(b))
print(mul2(a, b), a, b)

# immutable example
tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print(tt1 is tt2)
print(tt2 is tt3)

ss1 = 'Apple'
ss2 = 'Apple'

print(ss1 is ss2)
