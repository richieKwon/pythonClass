from inspect import signature
import random


class LotteryNumbers:
    def __init__(self):
        self._balls = [n for n in range(1, 56)]

    def pickNumbers(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(7)])

    def __call__(self):
        return self.pickNumbers()


game1 = LotteryNumbers()
print(game1.pickNumbers())
print(callable(str), callable(list), callable(
    game1.pickNumbers), callable(3.14), callable(LotteryNumbers))
print(game1())
