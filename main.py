from model import Model
from view import View
from controller import Controller

model = Model()
controller = Controller()
view = View(controller)

controller.configure(model, view)
#model.add_observer(view)



view.run()
