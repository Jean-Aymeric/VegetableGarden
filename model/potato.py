from model.vegetable import Vegetable
from typing import TypeVar

SelfIVegetable = TypeVar("SelfIVegetable", bound="IVegetable")


class Potato(Vegetable):
    __age: int

    def __init__(self):
        Vegetable.__init__(self, "Empty", " ")
        self.__age = 0

    def grow(self) -> SelfIVegetable:
        self.__age += 1
        if self.__age < 5:
            self.Sprite = " "
        elif self.__age < 8:
            self.Sprite = "p"
        elif self.__age < 15:
            self.Sprite = "P"
        elif self.__age < 19:
            self.Sprite = "£"
        else:
            self._die()
        return None
