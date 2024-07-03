import pygame
from tkinter import filedialog
import tkinter as tk
import asyncio
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

    async def startAuscultation(self):
        self.view.connection_label.config(text="Bluetooth Connection to Model: Pending")
        self.view.connection_label.config(foreground="yellow")
        await asyncio.ensure_future(self.model.connect_to_arduino())
        asyncio.sleep(30)
        while True:
            if self.model.connected():
                self.view.connection_label.config(text="Bluetooth Connection to Model: Connected")
                self.view.connection_label.config(foreground="green")
                return
            else:
                self.view.connection_label.config(text="Bluetooth Connection to Model: Inactive")
                self.view.connection_label.config(foreground="red")
                return



    async def endAuscultation(self):
        self.model.disconnect()
        await asyncio.sleep(2)
        self.view.connection_label.config(text="Bluetooth Connection to Model: Inactive")
        self.view.connection_label.config(foreground="red")
        print("auscultation ended")

