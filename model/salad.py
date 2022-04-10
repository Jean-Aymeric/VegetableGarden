from model.vegetable import Vegetable
from typing import TypeVar

SelfIVegetable = TypeVar("SelfIVegetable", bound="IVegetable")


class Salad(Vegetable):
    __age: int

    def __init__(self):
        Vegetable.__init__(self, "Empty", "s")
        self.__age = 0

    def grow(self) -> SelfIVegetable:
        self.__age += 1
        if self.__age < 4:
            self.Sprite = "s"
        elif self.__age < 7:
            self.Sprite = "S"
        elif self.__age < 11:
            self.Sprite = "$"
        else:
            self._die()
        return None
