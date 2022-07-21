from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return self.param * 2 + 0.3


coat = Coat(34)
suit = Suit(120)
print(coat + suit)
