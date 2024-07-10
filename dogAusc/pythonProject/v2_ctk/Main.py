import tkinter as tk
import customtkinter
from async_tkinter_loop import async_mainloop
from DogAuscModel import DogAuscModel
from DogAuscView import DogAuscView
from DogAuscController import DogAuscController


class Main:
    def __init__(self, root):
        self.model = DogAuscModel()
        self.view = DogAuscView(root)
        self.controller = DogAuscController(self.model, self.view)
        self.view.set_controller(self.controller)
        self.view.init_side_frame()
        self.view.init_main_frame()
        


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title("Vet Stethoscope")
    app = Main(root)
    async_mainloop(root)
