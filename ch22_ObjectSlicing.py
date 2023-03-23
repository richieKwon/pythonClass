class ObjectsSlice():
    def __init__(self):
        self._numbers = [n for n in range(0, 8)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]


s = ObjectsSlice()

print(s.__dict__)
print(len(s))
print(len(s._numbers))
print(s[0:4])
