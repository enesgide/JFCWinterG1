import tkinter as tk

from MediaPlayerModel import MediaPlayerModel
from MediaPlayerView import MediaPlayerView
from MediaPlayerController import MediaPlayerController


class Main:
    def __init__(self, root):
        self.model = MediaPlayerModel()
        self.view = MediaPlayerView(root, None)
        self.controller = MediaPlayerController(self.model, self.view)
        self.view.set_controller(self.controller)
        self.view.view_initialise()


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0,0)
    app = Main(root)
    root.mainloop()
