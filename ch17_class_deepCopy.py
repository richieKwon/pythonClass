ex1 = [10, [100, 107], (1, 2, 3)]
ex2 = ex1
ex3 = list(ex1)

print(ex1 is ex2)
print(ex1 is ex3)
print(ex3)


print(id(ex1[2]))
# tuple - allocate new address because of the nature of immutable
ex1[2] += (110, 120)
print(id(ex1[2]))
print(ex1)

listexample = [1, [2, 3], 4, 5]

print(id(listexample[1]))

listexample[1] += [110, 120]
print(id(listexample[1]))
print(listexample)


# DeepCopy
