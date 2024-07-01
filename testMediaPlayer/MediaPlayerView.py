from tkinter import filedialog, Menu, Listbox, Button, Frame
import tkinter as tk


class MediaPlayerView:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.song_list = None

        self.root.title("Media Player")
        self.root.geometry("1280x720")

        self.label = tk.Label(self.root, text="Not currently playing a song.")

    def set_controller(self, controller):
        self.controller = controller

    def view_initialise(self):
        self.create_menu()
        self.create_song_list()
        self.create_control_buttons()

    def create_menu(self):
        menubar = Menu(self.root)
        organise_menu = Menu(menubar, tearoff=0)
        organise_menu.add_command(label='Select Folder', command=self.controller.on_select_folder)
        organise_menu.add_command(label='Clear', command=self.controller.on_clear)
        menubar.add_cascade(label='File', menu=organise_menu)
        self.root.config(menu=menubar)

    def update_song_list(self, songs):
        self.song_list.delete(0, tk.END)
        for song in songs:
            self.song_list.insert(tk.END, song)

    def create_song_list(self):
        self.song_list = Listbox(self.root, bg="black", fg="white", width=400, height=40)
        self.song_list.pack()

    def create_control_buttons(self):
        ctrl_frame = Frame(self.root)
        ctrl_frame.pack()

        play = Button(ctrl_frame, text="Play", command=self.controller.play_song)
        pause = Button(ctrl_frame, text="Pause", command=self.controller.pause_song)
        prev_btn = Button(ctrl_frame, text="Prev", command=self.controller.prev_song)
        next_btn = Button(ctrl_frame, text="Next", command=self.controller.next_song)

        play.grid(row=0, column=0, pady=10)
        pause.grid(row=0, column=1, pady=10)
        prev_btn.grid(row=0, column=2, pady=10)
        next_btn.grid(row=0, column=3, pady=10)

    def get_root(self):
        return self.root
