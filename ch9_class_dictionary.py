# find hashValue

from unicodedata import name
from types import MappingProxyType
import csv
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))

# Dictionary comprehension
# with open('', 'r', encoding='UTF-8') as f:
#     temp = csv.reader(f)
#     next(temp)
#     NA_CODES = [tuple(x) for x in temp]

# n_code1 = {country: code for country, code in NA_CODES}

# Dictionary setdefault
source = (
    ('key1', 'value1'),
    ('key1', 'value2'),
    ('key2', 'value3'),
    ('key2', 'value4'),
)

new_dictionary = {}

for k, v in source:
    new_dictionary.setdefault(k, []).append(v)

print(new_dictionary)

# immutable dictionary > Impossible to change values
dict7 = {'key1': 'testValue1'}
dict7_frozen = MappingProxyType(dict7)
print(dict7 is dict7_frozen)

# immutable set > Impossible to change values
setExample1 = {'apple', 'orange', 'banana'}
setExample2 = set(['apple', 'orange', 'banana'])
# empty set
setExample3 = set()
setExample4 = frozenset({'apple', 'orange', 'banana'})


# comprehending set
print(
    {name(chr(i), '') for i in range(0, 256)}
)
