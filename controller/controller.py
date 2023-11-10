import time

from shared.action import Action
from shared.icontroller import IController
from shared.imodel import IModel
from shared.iview import IView


class Controller(IController):
    __view: IView
    __model: IModel
    __running: bool
    __pause: bool

    def __init__(self, view: IView, model: IModel):
        self.__view = view
        self.__model = model
        self.__view.setModel(self.__model)
        self.__view.setController(self)

    def getView(self) -> IView:
        return self.__view

    def getModel(self) -> IModel:
        return self.__model

    def start(self):
        self.__view.showGame()
        self.__running = True
        self.__pause = False
        self.__gameLoop()

    def __gameLoop(self):
        while self.__running:
            if not self.__pause:
                self.__model.moveMobiles()
            self.__view.showGame()
            time.sleep(0.0001)

    def performAction(self, action: Action):
        if action == Action.CLOSE:
            self.__running = False
        elif Action.PAUSE:
            self.__pause = not self.__pause
