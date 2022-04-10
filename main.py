from controller.controller import Controller
from model.model import Model
from model.onion import Onion
from model.potato import Potato
from model.salad import Salad
from model.tomato import Tomato
from view.viewConsole import ViewConsole

controller = Controller()
model = Model("conf/conf.json")
view = ViewConsole()
controller.Model = model
controller.View = view

model.VegetableGarden.sow(Tomato(), 0, 0)
model.VegetableGarden.sow(Salad(), model.VegetableGarden.Width - 1, 0)
model.VegetableGarden.sow(Potato(), 0, model.VegetableGarden.Height - 1)
model.VegetableGarden.sow(Onion(), model.VegetableGarden.Width - 1, model.VegetableGarden.Height - 1)

controller.start()
