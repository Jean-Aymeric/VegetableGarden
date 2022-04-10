from model.vegetable import Vegetable
from typing import TypeVar

SelfIVegetable = TypeVar("SelfIVegetable", bound="IVegetable")


class Tomato(Vegetable):
    __age: int

    def __init__(self):
        Vegetable.__init__(self, "Empty", ".")
        self.__age = 0

    def grow(self) -> SelfIVegetable:
        self.__age += 1
        if self.__age < 2:
            self.Sprite = "."
        elif self.__age < 5:
            self.Sprite = "t"
        elif self.__age < 10:
            self.Sprite = "T"
        elif self.__age < 12:
            self.Sprite = "#"
        else:
            self._die()
        return None
