from __future__ import annotations
from abc import ABC, abstractmethod
from contract.ivegatablegarden import IVegetableGarden


class IModel(ABC):
    @property
    def VegetableGarden(self) -> IVegetableGarden:
        ...

    @abstractmethod
    def getConfiguration(self, key: str) -> int | str:
        ...

    @abstractmethod
    def live(self) -> None:
        self.VegetableGarden.live()

    @property
    def Day(self) -> int:
        ...
