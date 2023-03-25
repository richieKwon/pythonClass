l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)

# print(l1 is l2)
# print(l1[2] is l2[2])
# print(id(l1[2]), id(l2[2]))
# print()
# print(id(l1[1]), id(l2[1]))
# l2[1].append(100)
# print(l1, l2)
# print(l1[1] is l2[1])
# print(id(l1[1]), id(l2[1]))

# print(id(l1[2]), id(l2[2]))
# l2[2] += (10, 11)
# print(l1, l2)
# print(l1[2] is l2[2])
# print(id(l1[2]), id(l2[2]))

print(id(l1[0]), id(l1[0]))
l1[0] = 7
print(l1, l2)
print(id(l1[0]), id(l1[0]))

print()

print(id(l1[0]), id(l1[0]))
l2[0] = 77
print(l1, l2)
print(id(l1[0]), id(l1[0]))
print(l1[0] == l2[0])
print(l1[0] is l2[0])
