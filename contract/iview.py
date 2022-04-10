from abc import ABC, abstractmethod

from contract.icontroller import IController
from contract.imodel import IModel


class IView(ABC):
    @abstractmethod
    def display(self) -> None:
        ...

    @property
    def Controller(self) -> IController:
        ...

    @Controller.setter
    def Controller(self, actionPerformer: IController) -> None:
        ...

    @property
    def Model(self) -> IModel:
        ...

    @Model.setter
    def Model(self, model: IModel) -> None:
        ...
