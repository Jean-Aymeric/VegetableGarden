from contract.imodel import IModel
from contract.iview import IView
from contract.icontroller import IController
from contract.order import Order
from time import sleep


class Controller(IController):
    __view: IView
    __model: IModel
    __running: bool

    @property
    def View(self) -> IView:
        return self.__view

    @View.setter
    def View(self, view: IView) -> None:
        self.__view = view
        view.Controller = self
        view.Model = self.__model

    @property
    def Model(self) -> IModel:
        return self.__model

    @Model.setter
    def Model(self, model: IModel) -> None:
        self.__model = model

    def start(self) -> None:
        self.__running = True
        while self.__running:
            self.View.display()
            self.Model.live()

    def performOrder(self, order: Order) -> None:
        if order == Order.QUIT:
            self.__running = False

