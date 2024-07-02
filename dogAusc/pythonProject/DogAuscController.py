import pygame
from tkinter import filedialog
import tkinter as tk
import os

class DogAuscController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pygame.mixer.init()

    def onTestS1(self):
        pass

    def onTestS2(self):
        pass

    def onTestS3(self):
        pass

    def onTestS4(self):
        pass

    def onLoadAudio(self):
        self.view.s1_label.config(text="Audio file for sensor 1: Wa")
        self.view.s2_label.config(text="Audio file for sensor 2: Wa")
        self.view.s3_label.config(text="Audio file for sensor 3: Wee")
        self.view.s4_label.config(text="Audio file for sensor 4: Woo")

    def onLoadPreset(self):
        pass

    def startAuscultation(self):
        pass

    def endAuscultation(self):
        pass

