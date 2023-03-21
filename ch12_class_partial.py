from operator import mul
from functools import partial

# to use call back function

# fix parameters
five = partial(mul, 5)

six = partial(five, 7)

print([five(i) for i in range(1, 10)])
print(list(map(five, range(1, 11))))
