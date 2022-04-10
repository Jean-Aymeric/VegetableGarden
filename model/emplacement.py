from contract.iemplacement import IEmplacement
from contract.ivegetable import IVegetable
from model.emptyvegetable import EmptyVegetable


class Emplacement(IEmplacement):
    __vegetable: IVegetable

    def __init__(self):
        self.Vegetable = EmptyVegetable()

    @property
    def Vegetable(self) -> IVegetable:
        return self.__vegetable

    @Vegetable.setter
    def Vegetable(self, vegetable: IVegetable) -> None:
        self.__vegetable = vegetable

    def isEmpty(self) -> bool:
        return self.Vegetable is EmptyVegetable

    def manageGrow(self) -> IVegetable:
        self.Vegetable.grow()
        if not self.Vegetable.isAlive():
            self.Vegetable = EmptyVegetable()
