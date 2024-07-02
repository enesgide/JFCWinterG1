import tkinter as tk

from DogAuscModel import DogAuscModel
from DogAuscView import DogAuscView
from DogAuscController import DogAuscController


class Main:
    def __init__(self, root):
        self.model = DogAuscModel()
        self.view = DogAuscView(root)
        self.controller = DogAuscController(self.model, self.view)
        self.view.set_controller(self.controller)
        self.view.view_initialise()


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = Main(root)
    root.mainloop()
