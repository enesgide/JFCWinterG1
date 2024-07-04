import pygame
from tkinter import filedialog
import tkinter as tk
import asyncio
import os

NOTIFY_CHARACTERISTIC_UUID = "19b10001-e8f2-537e-4f6c-d104768a1216"

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
        pass

    def onLoadPreset(self):
        pass

    async def startAuscultation(self):
        pass

    async def endAuscultation(self):
        pass

