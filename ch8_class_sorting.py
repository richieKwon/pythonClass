# sort vs sorted
# reverse, key=len, key=str.lower, key = func

fruit = ['orange', 'apple', 'mango', 'strawberry', 'banana']

# sorted : after sorting items, a new object returns
print(sorted(fruit))
print(sorted(fruit, reverse=True))
print(sorted(fruit, key=len))
print(sorted(fruit, key=lambda x: x[-1]))

# sort : after sorting items, the object returns (the original object changes)
a = fruit.sort(reverse=True)
print(a, fruit)
