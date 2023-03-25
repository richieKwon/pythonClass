import random
import abc


class randomNumber(abc.ABC):

    @abc.abstractclassmethod
    def load(self, iterobj):
        '''Iterable objects are here '''

# class pickUpItem(abc.ABC):
    @abc.abstractclassmethod
    def pick(self, iterobj):
        ''' '''

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))


class CraneMachine(randomNumber):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty! Nothing in the box')

    def __call__(self):
        return self.pick()


print(issubclass(randomNumber, CraneMachine))
print(issubclass(CraneMachine, randomNumber))
print(CraneMachine.__mro__)

cm = CraneMachine(range(1, 100))
print(cm())
print(cm.inspect())
