import pygame
from tkinter import filedialog
import tkinter as tk
import os


class MediaPlayerController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        pygame.mixer.init()

    def on_select_folder(self):
        directory = self.view.get_root().directory = filedialog.askdirectory()
        self.model.add_songs_from_dir(directory)
        self.view.update_song_list(self.model.get_songs())

    def on_clear(self):
        self.model.get_songs().clear()
        self.view.update_song_list([])

    def play_song(self):
        if not self.model.is_paused:
            selected_index = self.view.song_list.curselection()
            if selected_index:
                self.model.current_song = self.view.song_list.get(selected_index[0])
                pygame.mixer.music.load(os.path.join(self.view.root.directory, self.model.current_song))
                self.view.label.config(text="Now playing: " + self.model.current_song)
                pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()
            self.model.is_paused = False

    def pause_song(self):
        pygame.mixer.music.pause();
        self.model.is_paused = True

    def next_song(self):
        try:
            self.view.song_list.selection_clear(0, tk.END)
            self.view.song_list.selection_set(self.model.songs.index(self.model.current_song) + 1)
            self.model.current_song = self.model.songs[self.view.song_list.curselection()[0]]
            self.play_song()
        except:
            pass

    def prev_song(self):
        try:
            self.view.song_list.selection_clear(0, tk.END)
            self.view.song_list.selection_set(self.model.songs.index(self.model.current_song) - 1)
            self.model.current_song = self.model.songs[self.view.song_list.curselection()[0]]
            self.play_song()
        except:
            pass
