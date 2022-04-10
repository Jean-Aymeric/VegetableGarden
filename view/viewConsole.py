from contract.iview import IView
from contract.imodel import IModel
from contract.icontroller import IController
from contract.order import Order


class ViewConsole(IView):
    __model: IModel
    __controller: IController

    @property
    def Controller(self) -> IController:
        return self.__controller

    @Controller.setter
    def Controller(self, controller: IController) -> None:
        self.__controller = controller

    @property
    def Model(self) -> IModel:
        return self.__model

    @Model.setter
    def Model(self, model: IModel) -> None:
        self.__model = model

    def display(self) -> None:
        print("Day " + str(self.Model.Day) + "\nquit to exit the program.")
        for y in range(self.Model.VegetableGarden.Height + 2):
            for x in range(self.Model.VegetableGarden.Width + 2):
                if (x == 0) or (x == self.Model.VegetableGarden.Width + 1) or \
                        (y == 0) or (y == self.Model.VegetableGarden.Height + 1):
                    print("*", end="")
                else:
                    print (self.Model.VegetableGarden.emplacementXY(x-1, y-1).Vegetable.Sprite, end="")
            print("")
        if str.lower(input()) == "quit":
            self.Controller.performOrder(Order.QUIT)
