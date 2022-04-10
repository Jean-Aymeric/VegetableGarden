from abc import ABC, abstractmethod
from typing import TypeVar

SelfIVegetable = TypeVar("SelfIVegetable", bound="IVegetable")


class IVegetable(ABC):
    @property
    def Name(self) -> str:
        ...

    @property
    def Sprite(self) -> str:
        ...

    @abstractmethod
    def isAlive(self) -> bool:
        ...

    @abstractmethod
    def grow(self) -> SelfIVegetable:
        ...
