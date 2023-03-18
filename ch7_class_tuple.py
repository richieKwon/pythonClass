# packing and unpacking
print(divmod(100, 9))
print(divmod(*(100, 9)))

x, y, *rest = range(10)
print(x, y, rest)
print(x, y, *rest)

# Mutable vs Immutable - check memory address
l = (1, 2, 3)
m = [4, 5, 6]

print(id(l), id(m))

l = l * 2
m = m * 2
print(id(l), id(m))

l *= 2
m *= 2
print(id(l), id(m))
