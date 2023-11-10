from tkinter import Tk, messagebox, Canvas, Event, PhotoImage, NW

from shared.action import Action
from shared.icontroller import IController
from shared.imodel import IModel
from shared.iview import IView


class ViewTkinter(IView):
    __model: IModel
    __controller: IController
    __window: Tk
    __canvas: Canvas
    __plane: int
    __planeImage: PhotoImage

    def __init__(self):
        self.__window = None
        self.__planeImage = None

    def __createWindow(self):
        self.__window = Tk()
        self.__window.title(self.__model.getFromKey("title"))
        self.__window.geometry(str(self.__model.getFromKey("width") * int(self.__model.getFromKey("zoom")))
                               + "x"
                               + str(self.__model.getFromKey("height") * int(self.__model.getFromKey("zoom"))))
        self.__canvas = Canvas(self.__window, bg=self.__model.getFromKey("background"))
        self.__canvas.pack(fill="both", expand=True)
        self.__window.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__window.bind("<Key>", self.__manageKeyboard)
        self.__planeImage = PhotoImage(file=self.__model.getFromKey("planeImage"))
        self.__plane = self.__canvas.create_image(self.__model.getPlaneX(),
                                                  self.__model.getPlaneY(),
                                                  image=self.__planeImage,
                                                  anchor=NW)

    def __onClosing(self):
        self.__controller.performAction(Action.CLOSE)

    def display(self, message) -> None:
        messagebox.showinfo(self.__model.getFromKey("title"), message)

    def setModel(self, model: IModel):
        self.__model = model

    def askYesNo(self, message: str) -> bool:
        return messagebox.askyesno(self.__model.getFromKey("title"), message)

    def setController(self, controller) -> None:
        self.__controller = controller

    def showGame(self):
        if self.__window is None:
            self.__createWindow()
            zoom = self.__model.getFromKey("zoom")
        self.__canvas.coords(self.__plane, self.__model.getPlaneX(), self.__model.getPlaneY())
        self.__window.update()

    def __manageKeyboard(self, event: Event):
        if event.keysym == self.__model.getFromKey("keyPause"):
            self.__controller.performAction(Action.PAUSE)
