# sequence type
# Container can contain many different kind of types of data: int, string and so on - tuple, list, collections.deque
# Flat can contain only one type of data : str, bytes, bytearray, array.array, memoryview
# mutable : list, bytearray, array.array, memoryview, deque
# immutable : tuple, str, bytes


# comprehending Lists
import array
chars = '!@£$'
chars2 = 'YeraRhee'
code = [ord(s) for s in chars]
code2 = [i for i in chars2]
code3 = [ord(s) for s in chars if ord(s) > 40]
code4 = list(map(ord, chars))
code5 = list(filter(lambda x: x > 40, map(ord, chars)))
print(code4)

# Generator - create a one item at one go. do not stay in memory
tuple_generatorTest = (ord(s) for s in chars)
print(tuple_generatorTest)
print(next(tuple_generatorTest))
print(next(tuple_generatorTest))
array_Test = array.array('I', ((ord(s) for s in chars)))
print(array_Test.tolist())

# List example
mark1 = [['~'] * 3 for n in range(3)]
mark2 = [['~']*3] * 3
print(mark1)
print(mark2)

print([id(i) for i in mark1])
print([id(i) for i in mark2])
