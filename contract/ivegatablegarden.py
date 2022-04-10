from abc import ABC, abstractmethod
from contract.iemplacement import IEmplacement
from contract.ivegetable import IVegetable


class IVegetableGarden(ABC):
    @abstractmethod
    def emplacementXY(self, x: int, y: int) -> IEmplacement:
        ...

    @property
    def Width(self) -> int:
        ...

    @property
    def Height(self) -> int:
        ...

    @abstractmethod
    def sow(self, vegetable: IVegetable, x: int, y: int) -> None:
        ...

