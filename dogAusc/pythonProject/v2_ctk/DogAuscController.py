import pygame
import tkinter as tk
from tkinter import filedialog
import os

from DogAuscPopup import DogAuscPopup
from PopupController import PopupController

class DogAuscController:
    def __init__(self, model, view):
        self.model = model
        self.view = view 
        pygame.mixer.init()

    def onTestHeart(self):
        pass

    def onTestLung(self):
        pass

    def onLoadAudio(self):
        popup = DogAuscPopup(self.view)
        popup_controller = PopupController(self.view, popup, self.model)
        popup.set_controller(popup_controller)
        popup.init_popup()

    def onLoadPreset(self):
        pass

    def startAuscultation(self):
        pass

    def endAuscultation(self):
        pass

    def play_audio(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    

