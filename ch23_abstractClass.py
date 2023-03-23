# even if sequence was not inherited, __iter__ & __contain__ work
# which is called sequence protocol. searching for something necessary in the object automatically

from collections.abc import Sequence


class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]


i1 = IterTestA()

print(3 in i1[1:10])
print([i for i in i1])


class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]

    def __len__(self, idx):
        return len(range(1, 50, 2))


i2 = IterTestB()
