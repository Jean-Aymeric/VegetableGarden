from abc import ABC

from contract.ivegetable import IVegetable


class Vegetable(IVegetable, ABC):
    __name: str
    __sprite: str
    __alive:bool

    def __init__(self, name: str, sprite: str):
        self.Name = name
        self.Sprite = sprite
        self.__alive = True

    @property
    def Name(self) -> str:
        return self.__name

    @Name.setter
    def Name(self, name: str) -> None:
        self.__name = name

    @property
    def Sprite(self) -> str:
        return self.__sprite

    @Sprite.setter
    def Sprite(self, sprite: str) -> None:
        self.__sprite = sprite

    def isAlive(self) -> bool:
        return self.__alive

    def _die(self) -> None:
        self.__alive = False
