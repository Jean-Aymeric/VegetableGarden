from abc import ABC, abstractmethod

from contract.ivegetable import IVegetable


class IEmplacement(ABC):
    @abstractmethod
    def isEmpty(self) -> bool:
        ...

    @property
    def Vegetable(self) -> IVegetable:
        ...

    @Vegetable.setter
    def Vegetable(self, vegetable: IVegetable) -> None:
        ...
