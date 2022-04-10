from __future__ import annotations
from contract.imodel import IModel
from model.configuration import Configuration
from model.vegetablegarden import VegetableGarden
from contract.ivegatablegarden import IVegetableGarden


class Model(IModel):
    __configuration: Configuration
    __vegetableGarden: VegetableGarden
    __day: int

    def __init__(self, configurationFileName: str):
        self.__day = 0;
        self.__configuration = Configuration(configurationFileName)
        self.__vegetableGarden = VegetableGarden(self.__configuration.Configuration["width"],
                                                 self.__configuration.Configuration["height"])

    @property
    def VegetableGarden(self) -> IVegetableGarden:
        return self.__vegetableGarden

    def getConfiguration(self, key: str) -> int | str:
        return self.__configuration.Configuration[key]

    @property
    def Day(self) -> int:
        return self.__day

    def live(self) -> None:
        self.__day += 1
        self.__vegetableGarden.grow()
