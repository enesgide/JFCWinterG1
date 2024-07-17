import tkinter as tk
from async_tkinter_loop import async_mainloop
from DogAuscModel import DogAuscModel
from DogAuscView import DogAuscView
from DogAuscController import DogAuscController

# The main class, that serves as the running point for the whole application
class Main:

    # __init__(self, root)
    # initialises the model, view, and controller instances, and initialises the side and main frame components of the view

    # params: 
    # self = the class instance
    # root = the root Tk window

    # returns: None
    def __init__(self, root):
        self.model = DogAuscModel()
        self.view = DogAuscView(root)
        self.controller = DogAuscController(self.model, self.view)
        self.view.set_controller(self.controller)
        self.view.init_side_frame()
        self.view.init_main_frame()
        

# entry point, will be run if the script Main.py is run.
# sets up the root Tk window, initialises the Main instance, and runs the application's main loop using async_tkinter_loop's async_mainloop methodS
if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title("Vet Stethoscope")
    app = Main(root)
    async_mainloop(root)
