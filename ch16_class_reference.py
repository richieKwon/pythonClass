x = {'name': 'richie', 'age': 20}
y = x

# id means address in memory
print(id(x), id(y))
# Is id of x equal to one of y?
print(x is y)

# value is the same?
print(x == y)

x['class'] = 100

print(x, y)

z = {'name': 'richie', 'age': 20, 'class': 100}

print(x is z)

# however, in case of tuple,
tuple1 = (10, 7)
tuple2 = tuple1

print(tuple1 is tuple2)
