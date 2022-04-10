from model.vegetable import Vegetable
from typing import TypeVar

SelfIVegetable = TypeVar("SelfIVegetable", bound="IVegetable")


class Onion(Vegetable):
    __age: int

    def __init__(self):
        Vegetable.__init__(self, "Empty", " ")
        self.__age = 0

    def grow(self) -> SelfIVegetable:
        self.__age += 1
        if self.__age < 2:
            self.Sprite = " "
        elif self.__age < 4:
            self.Sprite = "o"
        elif self.__age < 7:
            self.Sprite = "O"
        elif self.__age < 9:
            self.Sprite = "Ô"
        else:
            self._die()
        return None
