class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')

    # generator
    def __iter__(self):
        for word in self._text:
            yield word
        return

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


def generator_ex():
    yield 'A'
    yield 'B'


temp2 = [x * 3 for x in generator_ex()]
temp3 = (x * 3 for x in generator_ex())

print(temp2)
print(temp3)

for i in temp3:
    print(i)
