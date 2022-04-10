from typing import List
from contract.iemplacement import IEmplacement
from contract.ivegatablegarden import IVegetableGarden
from contract.ivegetable import IVegetable
from model.emplacement import Emplacement


class VegetableGarden(IVegetableGarden):
    __emplacements: List[List[Emplacement]]
    __width: int
    __height: int

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__emplacements = [[None] * width for _ in range(height)]
        for y in range(height):
            for x in range(width):
                self.__emplacements[y][x] = Emplacement()

    def emplacementXY(self, x: int, y: int) -> IEmplacement:
        return self.__emplacements[y][x]

    @property
    def Width(self) -> int:
        return self.__width

    @property
    def Height(self) -> int:
        return self.__height

    def sow(self, vegetable: IVegetable, x: int, y: int) -> None:
        self.emplacementXY(x, y).Vegetable = vegetable

    def grow(self) -> None:
        for y in range(self.Height):
            for x in range(self.Width):
                self.__emplacements[y][x].manageGrow()
