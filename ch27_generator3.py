import itertools

gen1 = itertools.count(1, 5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))

print()
print()


gen2 = itertools.takewhile(lambda n: n < 30, itertools.count(1, 5))
for v in gen2:
    print(v)


gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for v in gen3:
    print(v)

gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)


gen5 = itertools.chain('ABC', range(1, 11, 2))
print(list(gen5))

gen6 = itertools.chain(enumerate('ABCDE'))
print(list(gen6))

gen7 = itertools.product('ABCDE')
print(list(gen7))


gen8 = itertools.product('ABCDE', repeat=2)
print(list(gen8))

# grouping
gen9 = itertools.groupby('AAAABBCCCCDDEEEE')
for chr, group in gen9:
    print(chr, group)
    print(chr, list(group))
