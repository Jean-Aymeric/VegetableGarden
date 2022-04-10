from model.vegetable import Vegetable
from typing import TypeVar

SelfIVegetable = TypeVar("SelfIVegetable", bound="IVegetable")


class EmptyVegetable(Vegetable):
    def __init__(self):
        Vegetable.__init__(self, "Empty", " ")

    def grow(self) -> SelfIVegetable:
        return None
