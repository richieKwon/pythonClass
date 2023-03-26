from collections import abc
textExample = 'YeraRhee'

w = iter(textExample)

while True:
    try:
        print(next(w))

    except StopIteration as log:
        print(log)
        break

print(w)

# to check if it is iterable
print(hasattr(textExample, '__iter__'))
print(isinstance(textExample, abc.Iterable))


class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration()
        self._idx += 1
        return word

    def __iter__(self):
        print('Called__iter__')
        return self

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


w1 = WordSplitIter('YeraRhee is the winner?')
print(w1)
print(next(w1))
print(next(w1))
print(next(w1))
